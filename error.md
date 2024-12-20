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




----

Removed server http://cratedb.cratedb.svc.cluster.local:4200 from active pool
Removed server http://cratedb.cratedb.svc.cluster.local:4200 from active pool
2024/12/20 13:12:20 ERROR mlflow.store.db.utils: SQLAlchemy database error. The following exception is caught.
(crate.client.exceptions.ConnectionError) No more Servers available, exception from last server: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
[SQL: SELECT experiments.experiment_id, experiments.name, experiments.artifact_location, experiments.lifecycle_stage, experiments.creation_time, experiments.last_update_time 
FROM experiments 
WHERE experiments.lifecycle_stage IN (?) ORDER BY experiments.creation_time DESC, experiments.experiment_id ASC 
 LIMIT ? OFFSET ?]
[parameters: ('active', 20001, 0)]
(Background on this error at: https://sqlalche.me/e/20/e3q8)
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/site-packages/urllib3/connectionpool.py", line 789, in urlopen
    response = self._make_request(
               ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/urllib3/connectionpool.py", line 536, in _make_request
    response = conn.getresponse()
               ^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/urllib3/connection.py", line 464, in getresponse
    httplib_response = super().getresponse()
                       ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/http/client.py", line 1395, in getresponse
    response.begin()
  File "/usr/local/lib/python3.11/http/client.py", line 325, in begin
    version, status, reason = self._read_status()
                              ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/http/client.py", line 294, in _read_status
    raise RemoteDisconnected("Remote end closed connection without"
http.client.RemoteDisconnected: Remote end closed connection without response

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/lib/python3.11/site-packages/crate/client/http.py", line 533, in _request
    response = self.server_pool[next_server].request(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/crate/client/http.py", line 164, in request
    return self.pool.urlopen(
           ^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/urllib3/connectionpool.py", line 843, in urlopen
    retries = retries.increment(
              ^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/urllib3/util/retry.py", line 474, in increment
    raise reraise(type(error), error, _stacktrace)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/urllib3/util/util.py", line 38, in reraise
    raise value.with_traceback(tb)
  File "/usr/local/lib/python3.11/site-packages/urllib3/connectionpool.py", line 789, in urlopen
    response = self._make_request(
               ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/urllib3/connectionpool.py", line 536, in _make_request
    response = conn.getresponse()
               ^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/urllib3/connection.py", line 464, in getresponse
    httplib_response = super().getresponse()
                       ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/http/client.py", line 1395, in getresponse
    response.begin()
  File "/usr/local/lib/python3.11/http/client.py", line 325, in begin
    version, status, reason = self._read_status()
                              ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/http/client.py", line 294, in _read_status
    raise RemoteDisconnected("Remote end closed connection without"
urllib3.exceptions.ProtocolError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1967, in _exec_single_context
    self.dialect.do_execute(
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 924, in do_execute
    cursor.execute(statement, parameters)
  File "/usr/local/lib/python3.11/site-packages/crate/client/cursor.py", line 58, in execute
    self._result = self.connection.client.sql(sql, parameters,
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/crate/client/http.py", line 456, in sql
    content = self._json_request('POST', self.path, data=data)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/crate/client/http.py", line 582, in _json_request
    response = self._request(method, path, data=data)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/crate/client/http.py", line 573, in _request
    self._drop_server(next_server, ex_message)
  File "/usr/local/lib/python3.11/site-packages/crate/client/http.py", line 641, in _drop_server
    raise ConnectionError(
crate.client.exceptions.ConnectionError: No more Servers available, exception from last server: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/local/lib/python3.11/site-packages/mlflow/store/db/utils.py", line 147, in make_managed_session
    yield session
  File "/usr/local/lib/python3.11/site-packages/mlflow/store/tracking/sqlalchemy_store.py", line 327, in _search_experiments
    queried_experiments = session.execute(stmt).scalars(SqlExperiment).all()
                          ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2351, in execute
    return self._execute_internal(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2236, in _execute_internal
    result: Result[Any] = compile_state_cls.orm_execute_statement(
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/context.py", line 293, in orm_execute_statement
    result = conn.execute(
             ^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1418, in execute
    return meth(
           ^^^^^
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/sql/elements.py", line 515, in _execute_on_connection
    return connection._execute_clauseelement(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1640, in _execute_clauseelement
    ret = self._execute_context(
          ^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1846, in _execute_context
    return self._exec_single_context(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1986, in _exec_single_context
    self._handle_dbapi_exception(
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 2353, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1967, in _exec_single_context
    self.dialect.do_execute(
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 924, in do_execute
    cursor.execute(statement, parameters)
  File "/usr/local/lib/python3.11/site-packages/crate/client/cursor.py", line 58, in execute
    self._result = self.connection.client.sql(sql, parameters,
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/crate/client/http.py", line 456, in sql
    content = self._json_request('POST', self.path, data=data)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/crate/client/http.py", line 582, in _json_request
    response = self._request(method, path, data=data)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/crate/client/http.py", line 573, in _request
    self._drop_server(next_server, ex_message)
  File "/usr/local/lib/python3.11/site-packages/crate/client/http.py", line 641, in _drop_server
    raise ConnectionError(
sqlalchemy.exc.OperationalError: (crate.client.exceptions.ConnectionError) No more Servers available, exception from last server: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
[SQL: SELECT experiments.experiment_id, experiments.name, experiments.artifact_location, experiments.lifecycle_stage, experiments.creation_time, experiments.last_update_time 
FROM experiments 
WHERE experiments.lifecycle_stage IN (?) ORDER BY experiments.creation_time DESC, experiments.experiment_id ASC 
 LIMIT ? OFFSET ?]
[parameters: ('active', 20001, 0)]
(Background on this error at: https://sqlalche.me/e/20/e3q8)
2024/12/20 13:12:20 ERROR mlflow.store.db.utils: SQLAlchemy database error. The following exception is caught.
(crate.client.exceptions.ConnectionError) No more Servers available, exception from last server: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
[SQL: SELECT experiments.experiment_id, experiments.name, experiments.artifact_location, experiments.lifecycle_stage, experiments.creation_time, experiments.last_update_time 
FROM experiments 
WHERE experiments.lifecycle_stage IN (?) ORDER BY experiments.creation_time DESC, experiments.experiment_id ASC 
 LIMIT ? OFFSET ?]
[parameters: ('active', 20001, 0)]
(Background on this error at: https://sqlalche.me/e/20/e3q8)
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/site-packages/urllib3/connectionpool.py", line 789, in urlopen
    response = self._make_request(
               ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/urllib3/connectionpool.py", line 536, in _make_request
    response = conn.getresponse()
               ^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/urllib3/connection.py", line 464, in getresponse
    httplib_response = super().getresponse()
                       ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/http/client.py", line 1395, in getresponse
    response.begin()
  File "/usr/local/lib/python3.11/http/client.py", line 325, in begin
    version, status, reason = self._read_status()
                              ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/http/client.py", line 294, in _read_status
    raise RemoteDisconnected("Remote end closed connection without"
http.client.RemoteDisconnected: Remote end closed connection without response

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/lib/python3.11/site-packages/crate/client/http.py", line 533, in _request
    response = self.server_pool[next_server].request(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/crate/client/http.py", line 164, in request
    return self.pool.urlopen(
           ^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/urllib3/connectionpool.py", line 843, in urlopen
    retries = retries.increment(
              ^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/urllib3/util/retry.py", line 474, in increment
    raise reraise(type(error), error, _stacktrace)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/urllib3/util/util.py", line 38, in reraise
    raise value.with_traceback(tb)
  File "/usr/local/lib/python3.11/site-packages/urllib3/connectionpool.py", line 789, in urlopen
    response = self._make_request(
               ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/urllib3/connectionpool.py", line 536, in _make_request
    response = conn.getresponse()
               ^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/urllib3/connection.py", line 464, in getresponse
    httplib_response = super().getresponse()
                       ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/http/client.py", line 1395, in getresponse
    response.begin()
  File "/usr/local/lib/python3.11/http/client.py", line 325, in begin
    version, status, reason = self._read_status()
                              ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/http/client.py", line 294, in _read_status
    raise RemoteDisconnected("Remote end closed connection without"
urllib3.exceptions.ProtocolError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1967, in _exec_single_context
    self.dialect.do_execute(
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 924, in do_execute
    cursor.execute(statement, parameters)
  File "/usr/local/lib/python3.11/site-packages/crate/client/cursor.py", line 58, in execute
    self._result = self.connection.client.sql(sql, parameters,
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/crate/client/http.py", line 456, in sql
    content = self._json_request('POST', self.path, data=data)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/crate/client/http.py", line 582, in _json_request
    response = self._request(method, path, data=data)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/crate/client/http.py", line 573, in _request
    self._drop_server(next_server, ex_message)
  File "/usr/local/lib/python3.11/site-packages/crate/client/http.py", line 641, in _drop_server
    raise ConnectionError(
crate.client.exceptions.ConnectionError: No more Servers available, exception from last server: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/local/lib/python3.11/site-packages/mlflow/store/db/utils.py", line 147, in make_managed_session
    yield session
  File "/usr/local/lib/python3.11/site-packages/mlflow/store/tracking/sqlalchemy_store.py", line 327, in _search_experiments
    queried_experiments = session.execute(stmt).scalars(SqlExperiment).all()
                          ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2351, in execute
    return self._execute_internal(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2236, in _execute_internal
    result: Result[Any] = compile_state_cls.orm_execute_statement(
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/context.py", line 293, in orm_execute_statement
    result = conn.execute(
             ^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1418, in execute
    return meth(
           ^^^^^
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/sql/elements.py", line 515, in _execute_on_connection
    return connection._execute_clauseelement(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1640, in _execute_clauseelement
    ret = self._execute_context(
          ^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1846, in _execute_context
    return self._exec_single_context(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1986, in _exec_single_context
    self._handle_dbapi_exception(
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 2353, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 1967, in _exec_single_context
    self.dialect.do_execute(
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 924, in do_execute
    cursor.execute(statement, parameters)
  File "/usr/local/lib/python3.11/site-packages/crate/client/cursor.py", line 58, in execute
    self._result = self.connection.client.sql(sql, parameters,
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/crate/client/http.py", line 456, in sql
    content = self._json_request('POST', self.path, data=data)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/crate/client/http.py", line 582, in _json_request
    response = self._request(method, path, data=data)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/crate/client/http.py", line 573, in _request
    self._drop_server(next_server, ex_message)
  File "/usr/local/lib/python3.11/site-packages/crate/client/http.py", line 641, in _drop_server
    raise ConnectionError(
sqlalchemy.exc.OperationalError: (crate.client.exceptions.ConnectionError) No more Servers available, exception from last server: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
[SQL: SELECT experiments.experiment_id, experiments.name, experiments.artifact_location, experiments.lifecycle_stage, experiments.creation_time, experiments.last_update_time 
FROM experiments 
WHERE experiments.lifecycle_stage IN (?) ORDER BY experiments.creation_time DESC, experiments.experiment_id ASC 
 LIMIT ? OFFSET ?]
[parameters: ('active', 20001, 0)]
(Background on this error at: https://sqlalche.me/e/20/e3q8)
[2024-12-20 13:12:20 +0000] [28] [DEBUG] Ignoring EPIPE
[2024-12-20 13:12:22 +0000] [26] [DEBUG] GET /
[2024-12-20 13:12:23 +0000] [27] [DEBUG] GET /ajax-api/2.0/mlflow/experiments/search
Removed server http://cratedb.cratedb.svc.cluster.local:4200 from active pool
2024/12/20 13:12:23 ERROR mlflow.store.db.utils: SQLAlchemy database error. The following exception is caught.
(crate.client.exceptions.ConnectionError) No more Servers available, exception from last server: HTTPConnectionPool(host='cratedb.cratedb.svc.cluster.local', port=4200): Max retries exceeded with url: /_sql?types=true (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0xffff814b8490>: Failed to establish a new connection: [Errno 111] Connection refused'))
(Background on this error at: https://sqlalche.me/e/20/e3q8)
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/site-packages/urllib3/connection.py", line 196, in _new_conn
    sock = connection.create_connection(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/urllib3/util/connection.py", line 85, in create_connection
    raise err
  File "/usr/local/lib/python3.11/site-packages/urllib3/util/connection.py", line 73, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [Errno 111] Connection refused

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/local/lib/python3.11/site-packages/urllib3/connectionpool.py", line 789, in urlopen
    response = self._make_request(
               ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/urllib3/connectionpool.py", line 495, in _make_request
    conn.request(
  File "/usr/local/lib/python3.11/site-packages/urllib3/connection.py", line 398, in request
    self.endheaders()
  File "/usr/local/lib/python3.11/http/client.py", line 1298, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "/usr/local/lib/python3.11/http/client.py", line 1058, in _send_output
    self.send(msg)
  File "/usr/local/lib/python3.11/http/client.py", line 996, in send
    self.connect()
  File "/usr/local/lib/python3.11/site-packages/urllib3/connection.py", line 236, in connect
    self.sock = self._new_conn()
                ^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/urllib3/connection.py", line 211, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0xffff814b8490>: Failed to establish a new connection: [Errno 111] Connection refused

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/local/lib/python3.11/site-packages/crate/client/http.py", line 533, in _request
    response = self.server_pool[next_server].request(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/crate/client/http.py", line 164, in request
    return self.pool.urlopen(
           ^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/urllib3/connectionpool.py", line 873, in urlopen
    return self.urlopen(
           ^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/urllib3/connectionpool.py", line 873, in urlopen
    return self.urlopen(
           ^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/urllib3/connectionpool.py", line 873, in urlopen
    return self.urlopen(
           ^^^^^^^^^^^^^
  [Previous line repeated 7 more times]
  File "/usr/local/lib/python3.11/site-packages/urllib3/connectionpool.py", line 843, in urlopen
    retries = retries.increment(
              ^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/urllib3/util/retry.py", line 519, in increment
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='cratedb.cratedb.svc.cluster.local', port=4200): Max retries exceeded with url: /_sql?types=true (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0xffff814b8490>: Failed to establish a new connection: [Errno 111] Connection refused'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 146, in __init__
    self._dbapi_connection = engine.raw_connection()
                             ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 3300, in raw_connection
    return self.pool.connect()
           ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/pool/base.py", line 449, in connect
    return _ConnectionFairy._checkout(self)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/pool/base.py", line 1362, in _checkout
    with util.safe_reraise():
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/util/langhelpers.py", line 146, in __exit__
    raise exc_value.with_traceback(exc_tb)
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/pool/base.py", line 1300, in _checkout
    result = pool._dialect._do_ping_w_event(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 715, in _do_ping_w_event
    return self.do_ping(dbapi_connection)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 741, in do_ping
    cursor.execute(self._dialect_specific_select_one)
  File "/usr/local/lib/python3.11/site-packages/crate/client/cursor.py", line 58, in execute
    self._result = self.connection.client.sql(sql, parameters,
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/crate/client/http.py", line 456, in sql
    content = self._json_request('POST', self.path, data=data)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/crate/client/http.py", line 582, in _json_request
    response = self._request(method, path, data=data)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/crate/client/http.py", line 573, in _request
    self._drop_server(next_server, ex_message)
  File "/usr/local/lib/python3.11/site-packages/crate/client/http.py", line 641, in _drop_server
    raise ConnectionError(
crate.client.exceptions.ConnectionError: No more Servers available, exception from last server: HTTPConnectionPool(host='cratedb.cratedb.svc.cluster.local', port=4200): Max retries exceeded with url: /_sql?types=true (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0xffff814b8490>: Failed to establish a new connection: [Errno 111] Connection refused'))

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/local/lib/python3.11/site-packages/mlflow/store/db/utils.py", line 147, in make_managed_session
    yield session
  File "/usr/local/lib/python3.11/site-packages/mlflow/store/tracking/sqlalchemy_store.py", line 327, in _search_experiments
    queried_experiments = session.execute(stmt).scalars(SqlExperiment).all()
                          ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2351, in execute
    return self._execute_internal(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2226, in _execute_internal
    conn = self._connection_for_bind(bind)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2095, in _connection_for_bind
    return trans._connection_for_bind(engine, execution_options)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<string>", line 2, in _connection_for_bind
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/state_changes.py", line 139, in _go
    ret_value = fn(self, *arg, **kw)
                ^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 1189, in _connection_for_bind
    conn = bind.connect()
           ^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 3276, in connect
    return self._connection_cls(self)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 148, in __init__
    Connection._handle_dbapi_exception_noconnection(
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 2440, in _handle_dbapi_exception_noconnection
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 146, in __init__
    self._dbapi_connection = engine.raw_connection()
                             ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/base.py", line 3300, in raw_connection
    return self.pool.connect()
           ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/pool/base.py", line 449, in connect
    return _ConnectionFairy._checkout(self)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/pool/base.py", line 1362, in _checkout
    with util.safe_reraise():
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/util/langhelpers.py", line 146, in __exit__
    raise exc_value.with_traceback(exc_tb)
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/pool/base.py", line 1300, in _checkout
    result = pool._dialect._do_ping_w_event(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 715, in _do_ping_w_event
    return self.do_ping(dbapi_connection)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/sqlalchemy/engine/default.py", line 741, in do_ping
    cursor.execute(self._dialect_specific_select_one)
  File "/usr/local/lib/python3.11/site-packages/crate/client/cursor.py", line 58, in execute
    self._result = self.connection.client.sql(sql, parameters,
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/crate/client/http.py", line 456, in sql
    content = self._json_request('POST', self.path, data=data)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/crate/client/http.py", line 582, in _json_request
    response = self._request(method, path, data=data)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/crate/client/http.py", line 573, in _request
    self._drop_server(next_server, ex_message)
  File "/usr/local/lib/python3.11/site-packages/crate/client/http.py", line 641, in _drop_server
    raise ConnectionError(
sqlalchemy.exc.OperationalError: (crate.client.exceptions.ConnectionError) No more Servers available, exception from last server: HTTPConnectionPool(host='cratedb.cratedb.svc.cluster.local', port=4200): Max retries exceeded with url: /_sql?types=true (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0xffff814b8490>: Failed to establish a new connection: [Errno 111] Connection refused'))
(Background on this error at: https://sqlalche.me/e/20/e3q8)
[2024-12-20 13:12:34 +0000] [29] [DEBUG] POST /ajax-api/2.0/mlflow/runs/sear

