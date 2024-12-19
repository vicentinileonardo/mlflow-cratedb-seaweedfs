import random
import mlflow

mlflow.set_tracking_uri('http://localhost:5000')
mlflow.set_experiment('test-local')

def run_experiment():
    mlflow.log_param('name', 'Peter')
    mlflow.log_param('age', 20 + random.random() * 30)

    output_path = 'output.txt'
    with open(output_path, 'w') as f:
        f.write('Something {}'.format(random.randint(30, 50)))

    mlflow.log_artifact(output_path)


with mlflow.start_run():
    run_experiment()