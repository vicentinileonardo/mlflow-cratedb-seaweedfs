inside the pod of the tracking server:

[2024-12-19 13:11:21 +0000] [21] [DEBUG] GET /api/2.0/mlflow-artifacts/artifacts/1734605792721/b11108633afb408c9ecb49e3a91dd17f/artifacts/estimator.html
2024/12/19 13:11:21 ERROR mlflow.server: Exception on /api/2.0/mlflow-artifacts/artifacts/1734605792721/b11108633afb408c9ecb49e3a91dd17f/artifacts/estimator.html [GET]
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/site-packages/flask/app.py", line 1473, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/flask/app.py", line 882, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/flask/app.py", line 880, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/flask/app.py", line 865, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/mlflow/server/handlers.py", line 561, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/mlflow/server/handlers.py", line 583, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/mlflow/server/handlers.py", line 2100, in _download_artifact
    dst = artifact_repo.download_artifacts(artifact_path, tmp_dir.name)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/mlflow/store/artifact/artifact_repo.py", line 247, in download_artifacts
    if self._is_directory(artifact_path):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/mlflow/store/artifact/artifact_repo.py", line 146, in _is_directory
    listing = self.list_artifacts(artifact_path)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/mlflow/store/artifact/s3_artifact_repo.py", line 208, in list_artifacts
    s3_client = self._get_s3_client()
                ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/mlflow/store/artifact/s3_artifact_repo.py", line 135, in _get_s3_client
    return _get_s3_client(
           ^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/mlflow/store/artifact/s3_artifact_repo.py", line 110, in _get_s3_client
    return _cached_get_s3_client(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/mlflow/store/artifact/s3_artifact_repo.py", line 59, in _cached_get_s3_client
    import boto3
ModuleNotFoundError: No module named 'boto3'






