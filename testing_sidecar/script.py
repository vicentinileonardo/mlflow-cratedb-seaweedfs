import os
import time
import logging
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MLflowModelHandler(FileSystemEventHandler):
    def __init__(self, base_path, registry, registry_namespace, registry_username, registry_password):
        self.base_path = base_path
        self.registry = registry
        self.registry_namespace = registry_namespace
        self.registry_username = registry_username
        self.registry_password = registry_password
        
        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        self.logger = logging.getLogger(__name__)

    def extract_meaningful_image_name(self, model_path):
        """
        Extract a meaningful name from the MLflow model path
        
        Example path structures:
        /mlartifacts/1734390137379/7d654b989f3b49cf954f35701076f51c/artifacts/model (in container)
        /mlruns/321663888632330278/dce3966053da44658dc78889d02ac9d8/artifacts/model/ (in local env)

        """
        self.logger.info(f"Extracting image name from model path: {model_path}")
        try:
            # Split the path and extract relevant components
            path_parts = model_path.split('/')

            # Try to extract experiment_id and potentially model info
            experiment_id = path_parts[-4] if len(path_parts) >= 5 else 'unknown-experiment'
            self.logger.info(f"Extracted experiment_id: {experiment_id}")
            
            # Try to extract run_id and potentially experiment or model info
            run_id = path_parts[-3] if len(path_parts) >= 4 else 'unknown-run'
            self.logger.info(f"Extracted run_id: {run_id}")

            # Truncate experiment_id to first 4 and last 4 characters for readability, with ... in between
            if len(experiment_id) > 8:
                short_experiment_id = f"{experiment_id[:4]}-{experiment_id[-4:]}"
            else:
                short_experiment_id = experiment_id
            
            # Truncate run_id to first 4 and last 4 characters for readability, with ... in between
            if len(run_id) > 8:
                short_run_id = f"{run_id[:4]}-{run_id[-4:]}"
            else:
                short_run_id = run_id
            
            # Get current timestamp
            timestamp = time.strftime("%Y%m%d")
            
            # Create a meaningful image name
            # Format: namespace/mlflow-model-{experiment_id}-{run_id}-{timestamp}
            image_name = f"{self.registry_namespace}/mlflow-model-{short_experiment_id}-{short_run_id}-{timestamp}"
            image_name = image_name.lower() # Docker image names must be lowercase
            self.logger.info(f"Extracted image name: {image_name}")
            return image_name
        except Exception as e:
            self.logger.error(f"Error creating image name: {e}")
            # Fallback to a generic name if extraction fails
            fallback = f"{self.registry_namespace}/mlflow-model-{time.strftime('%Y%m%d')}"
            fallback = fallback.lower()
            self.logger.warning(f"Fallback image name: {fallback}")
            return fallback
        
    def is_valid_model_folder(self, path):
        """
        Check if the folder is a valid model folder
        Criteria:
        1. Folder name is 'model'
        2. Parent folder hierarchy includes mlflow_root (like 'mlartifacts')
        """
        mlflow_root = os.getenv("MLFLOW_ROOT_NAME", "mlartifacts")
        self.logger.info(f"Checking folder: {path}")
        
        # Check if the folder name is 'model'
        if os.path.basename(path) != 'model':
            self.logger.info("Folder name is not 'model'")
            return False
        
        # Split the path into components
        path_components = path.split(os.path.sep)
        
        # Check if mlflow_root is in the path
        if mlflow_root not in path_components:
            self.logger.info(f"mlflow_root '{mlflow_root}' not found in path")
            return False
        
        self.logger.info(f"Found valid model folder: {path}")
        
        # Check for model.pkl file (to be modified based on your model file) (OPTIONAL)
        #model_pkl_path = os.path.join(path, 'model.pkl')
        #self.logger.info(f"Checking for model.pkl in {path}")
        #if not os.path.exists(model_pkl_path):
        #    self.logger.error("model.pkl not found in model folder")
        #    return False
        #else:
        #    self.logger.info("model.pkl found in model folder")
        #return os.path.exists(model_pkl_path)

        return True

    def docker_login(self):
        """
        Login to the container registry
        """
        self.logger.info(f"Logging into container registry: {self.registry}")
        try:
            # Use subprocess.Popen for more secure password handling
            process = subprocess.Popen(
                ['docker', 'login', self.registry, '-u', self.registry_username, '--password-stdin'],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Write password to stdin and close it
            stdout, stderr = process.communicate(input=self.registry_password)
            
            # Check the return code
            if process.returncode != 0:
                self.logger.error(f"Docker login failed: {stderr}")
                raise subprocess.CalledProcessError(process.returncode, process.args, stdout, stderr)
            
            self.logger.info("Successfully logged into container registry")
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Docker login failed: {e}")
            raise

    def build_and_push_model(self, model_path):
        """
        Build and push Docker image using MLflow
        """
        self.logger.info(f"Building and pushing model: {model_path}")
        try:
            # Create meaningful image name
            image_name = self.extract_meaningful_image_name(model_path)
            logging.info(f"Using image name: {image_name} for model: {model_path}")
            
            # Build Docker image using MLflow
            build_cmd = [
                'mlflow', 'models', 'build-docker',
                '-m', model_path,
                '-n', image_name,
                '--enable-mlserver'
            ]
            subprocess.run(build_cmd, check=True)
            
            # Push Docker image
            push_cmd = ['docker', 'push', image_name]
            subprocess.run(push_cmd, check=True)
            self.logger.info(f"Successfully built and pushed image: {image_name}")
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Docker build/push failed: {e}")
            raise

    def on_created(self, event):
        # Check if a new directory is created
        if event.is_directory:
            # Full path of the new directory
            new_dir_path = event.src_path
            self.logger.info(f"New directory created: {new_dir_path}")
            
            # Check if this is a valid model folder
            if self.is_valid_model_folder(new_dir_path):
                try:
                    # Wait a short time to ensure files are populated
                    waiting_time = 10
                    self.logger.info(f"Waiting for {waiting_time} seconds for model folder to be populated by mlflow tracking server...")
                    time.sleep(waiting_time)
                
                    # Additional check to ensure model files are present (OPTIONAL)
                    #model_pkl_path = os.path.join(new_dir_path, 'model.pkl')
                    #if not os.path.exists(model_pkl_path):
                    #    self.logger.warning(f"model.pkl not found in {new_dir_path}. Skipping.")
                    #    return
                    
                    # Determine the full MLflow model path
                    mlflow_model_path = new_dir_path # TO BE VERIFIED
                    self.logger.info(f"Processing model folder: {mlflow_model_path}")
                    
                    # Login to registry
                    self.docker_login()
                    
                    # Build and push the model
                    self.build_and_push_model(mlflow_model_path)
                    
                except Exception as e:
                    self.logger.error(f"Error processing model folder: {e}")

def monitor_mlflow_artifacts(base_path, registry, registry_namespace, registry_username, registry_password):
    """
    Start monitoring the MLflow artifacts folder for new model folders
    
    :param base_path: Path to the MLflow artifacts base folder
    :param registry: Container registry URL
    :param registry_namespace: Registry namespace
    :param registry_username: Registry username
    :param registry_password: Registry password
    """
    event_handler = MLflowModelHandler(
        base_path, 
        registry,
        registry_namespace,
        registry_username, 
        registry_password
    )
    observer = Observer()
    observer.schedule(event_handler, base_path, recursive=True)
    
    try:
        observer.start()
        print(f"Monitoring {base_path} for new MLflow model folders...")
        
        # Keep the script running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()

if __name__ == "__main__":
    # Configuration
    BASE_MONITORING_PATH = os.getenv("MLFLOW_ARTIFACTS_PATH", "/Users/leonardovicentini/Desktop/Magistrale/Theses/system/mlflow-cratedb-demo/testing_sidecar/mlartifacts")     # Set to root so that the mlartifacts do not need to be already there
    REGISTRY = os.getenv("REGISTRY", "docker.io")                      # Default to Docker Hub
    REGISTRY_NAMESPACE = os.getenv("REGISTRY_NAMESPACE")
    REGISTRY_USERNAME = os.getenv("REGISTRY_USERNAME")
    REGISTRY_PASSWORD = os.getenv("REGISTRY_PASSWORD")
    
    # Start monitoring
    monitor_mlflow_artifacts(
        BASE_MONITORING_PATH, 
        REGISTRY,
        REGISTRY_NAMESPACE, 
        REGISTRY_USERNAME, 
        REGISTRY_PASSWORD
    )
