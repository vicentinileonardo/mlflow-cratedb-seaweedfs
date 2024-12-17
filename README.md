# mlflow-cratedb-demo

Main references:
- https://github.com/crate/mlflow-cratedb/
- https://github.com/crate/mlflow-cratedb/tree/main/examples
- https://github.com/crate/mlflow-cratedb/blob/main/docs/container.md

Notes:
- Current mlflow version is: 2.19.0
- mlflow version found inside mlflow-cratedb adapter is: 2.14.1

## How to install

Install **CrateDB** and **mlflow tracking server**:
```bash
kubectl apply -f manifests/mlflow-cratedb.yaml
```

### Testing the installation

Testing connection to CrateDB:
```bash
kubectl run --rm -it --image=alpine/curl:latest test-client -- /bin/sh

# inside the container
curl cratedb.cratedb.svc.cluster.local:4200

# Expected response
{
  "ok" : true,
  "status" : 200,
  "name" : "Rotgschirr",
  "cluster_name" : "crate",
  "version" : {
    "number" : "5.9.5",
    "build_hash" : "c8570f7811dda8eb4c6314c54976afa8ebe5ffbf",
    "build_timestamp" : "NA",
    "build_snapshot" : false,
    "lucene_version" : "9.11.1"
  }
}
```

Testing connection to mlflow tracking server:
```bash
kubectl run --rm -it --image=alpine/curl:latest test-client -- /bin/sh

# inside the container
curl mlflow-tracking.mlflow-tracking.svc.cluster.local:5000

# Expected response
<!doctype html><html lang="en"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit=no"/><link rel="shortcut icon" href="./static-files/favicon.ico"/><meta name="theme-color" content="#000000"/><link rel="manifest" href="./static-files/manifest.json" crossorigin="use-credentials"/><title>MLflow</title><script defer="defer" src="static-files/static/js/main.68ca1005.js"></script><link href="static-files/static/css/main.328af5c2.css" rel="stylesheet"></head><body><noscript>You need to enable JavaScript to run this app.</noscript><div id="root"></div><div id="modal"></div></body></html>/
```

Port forwarding to mlflow tracking server (for testing):
This is due to a local setup.
```bash
kubectl port-forward service/mlflow-tracking 5000:5000 -n mlflow-tracking
```

## Running experiments inside the cluster

Apply the mlflow experiments configurations (K8s jobs):
```bash
kubectl apply -f manifests/mlflow-experiments.yaml
```

## Local experiments with mlflow tracking

Using a local Python file with mlflow tracking (`tracking_dummy_local.py`).
The file imports the upstream mlflow library and uses the tracking API (e.g. `mlflow.set_experiment("dummy-experiment-local-env")`, `mlflow.log_metric("precision", 0.33)`).
The `mlflow_cratedb` library is not needed.

The following is not needed in this case:
```python
def start_adapter():
    logger.info("Initializing CrateDB adapter")
    import mlflow_cratedb  # noqa: F401
```
Probably this is needed only when the tracking server is not used as proxy but the metadata is sent directly in CrateDB (not the case here).

Prepare the local environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U -r requirements.txt
```

Check installation of mlflow-cratedb:
```bash
mlflow-cratedb --version

# Expected output
2024/12/17 01:11:35 INFO mlflow: Amalgamating MLflow for CrateDB
mlflow-cratedb, version 2.14.1
```

Run the local experiment:
```bash
python tracking_dummy_local.py
```

## Running queries on CrateDB

Running SELECT queries on CrateDB to check experiments and runs:
```bash
kubectl apply -f manifests/cratedb-queries.yaml
```

Check the logs of the pod related to query-1:
```bash
kubectl logs pod/pod/cratedb-query-1-kwpb4 -n cratedb

# Expected output
CONNECT OK
+---------------+----------------------------+---------------------------------+-----------------+---------------+------------------+
| experiment_id | name                       | artifact_location               | lifecycle_stage | creation_time | last_update_time |
+---------------+----------------------------+---------------------------------+-----------------+---------------+------------------+
| 1734391906622 | dummy-experiment-local-env | mlflow-artifacts:/1734391906622 | active          | 1734391906602 |    1734391906602 |
|             0 | Default                    | mlflow-artifacts:/0             | active          | 1734389171773 |    1734389171773 |
| 1734389204315 | dummy-experiment           | mlflow-artifacts:/1734389204315 | active          | 1734389204271 |    1734389204271 |
| 1734390137379 | numenta-merlion-experiment | mlflow-artifacts:/1734390137379 | active          | 1734390137365 |    1734390137365 |
+---------------+----------------------------+---------------------------------+-----------------+---------------+------------------+
SELECT 4 rows in set (0.079 sec)
```

Check the logs of the pod related to query-2:
```bash
kubectl logs pod/cratedb-query-2-pl26d -n cratedb

# Expected output
CONNECT OK
+----------------------------------+---------------------+-------------+-------------+------------------+-------------------+----------+---------------+---------------+--------------+----------------+-----------------+----------------------------------------------------------------------------+---------------+
| run_uuid                         | name                | source_type | source_name | entry_point_name | user_id           | status   |    start_time |      end_time | deleted_time | source_version | lifecycle_stage | artifact_uri                                                               | experiment_id |
+----------------------------------+---------------------+-------------+-------------+------------------+-------------------+----------+---------------+---------------+--------------+----------------+-----------------+----------------------------------------------------------------------------+---------------+
| 0c28ed5390c64e1b8c1668be8314f126 | unruly-sloth-881    | UNKNOWN     |             |                  | root              | FINISHED | 1734389204845 | 1734389205646 | NULL         |                | active          | mlflow-artifacts:/1734389204315/0c28ed5390c64e1b8c1668be8314f126/artifacts | 1734389204315 |
| 358aaa853b8f47f98802177e6f130c5f | skillful-dog-140    | UNKNOWN     |             |                  | leonardovicentini | FINISHED | 1734391907058 | 1734391907776 | NULL         |                | active          | mlflow-artifacts:/1734391906622/358aaa853b8f47f98802177e6f130c5f/artifacts | 1734391906622 |
| 318a8e7495424ff78011c810cf6d7320 | upset-colt-323      | UNKNOWN     |             |                  | root              | FAILED   | 1734390231113 | 1734390303042 | NULL         |                | active          | mlflow-artifacts:/1734390137379/318a8e7495424ff78011c810cf6d7320/artifacts | 1734390137379 |
| 3e38f890448043dbb1bea57b2e6cecef | carefree-sloth-975  | UNKNOWN     |             |                  | root              | FINISHED | 1734390557553 | 1734390616857 | NULL         |                | active          | mlflow-artifacts:/1734390137379/3e38f890448043dbb1bea57b2e6cecef/artifacts | 1734390137379 |
| 5b6bfe03af7c4adba531907b0f79e9d7 | mysterious-gnu-449  | UNKNOWN     |             |                  | root              | FAILED   | 1734390137531 | 1734390214739 | NULL         |                | active          | mlflow-artifacts:/1734390137379/5b6bfe03af7c4adba531907b0f79e9d7/artifacts | 1734390137379 |
| 2654d9d68e2647859ee50a88a03a9a6a | lyrical-dolphin-457 | UNKNOWN     |             |                  | root              | FAILED   | 1734390328445 | 1734390401956 | NULL         |                | active          | mlflow-artifacts:/1734390137379/2654d9d68e2647859ee50a88a03a9a6a/artifacts | 1734390137379 |
+----------------------------------+---------------------+-------------+-------------+------------------+-------------------+----------+---------------+---------------+--------------+----------------+-----------------+----------------------------------------------------------------------------+---------------+
SELECT 6 rows in set (0.006 sec)
```
