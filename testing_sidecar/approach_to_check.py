import time
from watchdog.events import FileSystemEventHandler

class ModelFolderHandler(FileSystemEventHandler):
    def __init__(self, base_handler):
        self.base_handler = base_handler
        self.file_count = 0
        self.last_modification_time = None

    def on_created(self, event):
        if event.is_directory and self.base_handler.is_valid_model_folder(event.src_path):
            self.last_modification_time = time.time()
            self.file_count = 0
            self.monitor_folder(event.src_path)

    def on_modified(self, event):
        if not event.is_directory:
            self.file_count += 1
            self.last_modification_time = time.time()

    def monitor_folder(self, folder_path):
        def check_folder_stability():
            current_time = time.time()
            # Wait until no modifications for 10 seconds
            if (current_time - self.last_modification_time > 10 and 
                os.path.exists(os.path.join(folder_path, 'model.pkl'))):
                try:
                    self.base_handler.docker_login()
                    self.base_handler.build_and_push_model(folder_path)
                except Exception as e:
                    self.base_handler.logger.error(f"Error processing folder: {e}")
                return True
            return False

        # Use a separate thread to monitor folder stability
        import threading
        def stability_check():
            while not check_folder_stability():
                time.sleep(2)

        threading.Thread(target=stability_check, daemon=True).start()