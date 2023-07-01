# Localstack Enhancement Request - Reproduce issue #8576

Issue link : [enhancement request: cloudformation update_stack #8576](https://github.com/localstack/localstack/issues/8576)

## Setup

Run the localstack in docker container : [Guide](https://docs.localstack.cloud/getting-started/installation/#docker-compose)

```bash
> docker-compose up
```

I am using Python 3.10.11

```bash
> python --version
Python 3.10.11
```

```bash
> python -m venv .venv

> .venv\Scripts\activate

> pip install -r requirements.txt
```

## Run the test case

```bash
> pytest -v -s
test_app.py::test_create_stack File uploaded to bucket : test-bucket
PASSED
test_app.py::test_update_stack File uploaded to bucket : test-bucket
FAILED
```

## Localstack container logs

```bash
2023-07-01 13:32:02 Ready.
2023-07-01 13:44:44 2023-07-01T08:14:44.520  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS s3.ListBuckets => 200
2023-07-01 13:44:54 2023-07-01T08:14:54.699  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS s3.CreateBucket => 200
2023-07-01 13:44:56 2023-07-01T08:14:56.978  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS s3.PutObject => 200
2023-07-01 13:45:00 2023-07-01T08:15:00.768  INFO --- [   asgi_gw_0] localstack.utils.bootstrap : Execution of "_load_service_plugin" took 1685.14ms
2023-07-01 13:45:00 2023-07-01T08:15:00.769  INFO --- [   asgi_gw_0] localstack.utils.bootstrap : Execution of "require" took 1686.58ms
2023-07-01 13:45:00 2023-07-01T08:15:00.891  INFO --- [   asgi_gw_1] localstack.request.aws     : AWS s3.GetObject => 200
2023-07-01 13:45:00 2023-07-01T08:15:00.905  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS cloudformation.CreateStack => 200
2023-07-01 13:45:02 2023-07-01T08:15:02.964  INFO --- [   asgi_gw_1] localstack.request.aws     : AWS s3.CreateBucket => 200
2023-07-01 13:45:05 2023-07-01T08:15:05.029  INFO --- [   asgi_gw_1] localstack.request.aws     : AWS s3.PutObject => 200
2023-07-01 13:45:07 2023-07-01T08:15:07.105 ERROR --- [   asgi_gw_0] l.aws.handlers.logging     : exception during call chain: Unable to get template body from input: {'StackName': 'test-stack', 'UsePreviousTemplate': True, 'Parameters': [{'ParameterKey': 'MyRoleName', 'ParameterValue': 'sample-test-role-new'}]}
2023-07-01 13:45:07 2023-07-01T08:15:07.110  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS cloudformation.UpdateStack => 500 (InternalError)
2023-07-01 13:45:09 2023-07-01T08:15:09.966 ERROR --- [   asgi_gw_1] l.aws.handlers.logging     : exception during call chain: Unable to get template body from input: {'StackName': 'test-stack', 'UsePreviousTemplate': True, 'Parameters': [{'ParameterKey': 'MyRoleName', 'ParameterValue': 'sample-test-role-new'}]}
2023-07-01 13:45:09 2023-07-01T08:15:09.967  INFO --- [   asgi_gw_1] localstack.request.aws     : AWS cloudformation.UpdateStack => 500 (InternalError)
2023-07-01 13:45:12 2023-07-01T08:15:12.289 ERROR --- [   asgi_gw_0] l.aws.handlers.logging     : exception during call chain: Unable to get template body from input: {'StackName': 'test-stack', 'UsePreviousTemplate': True, 'Parameters': [{'ParameterKey': 'MyRoleName', 'ParameterValue': 'sample-test-role-new'}]}
2023-07-01 13:45:12 2023-07-01T08:15:12.290  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS cloudformation.UpdateStack => 500 (InternalError)
2023-07-01 13:45:14 2023-07-01T08:15:14.809 ERROR --- [   asgi_gw_1] l.aws.handlers.logging     : exception during call chain: Unable to get template body from input: {'StackName': 'test-stack', 'UsePreviousTemplate': True, 'Parameters': [{'ParameterKey': 'MyRoleName', 'ParameterValue': 'sample-test-role-new'}]}
2023-07-01 13:45:14 2023-07-01T08:15:14.811  INFO --- [   asgi_gw_1] localstack.request.aws     : AWS cloudformation.UpdateStack => 500 (InternalError)
2023-07-01 13:45:17 2023-07-01T08:15:17.228 ERROR --- [   asgi_gw_1] l.aws.handlers.logging     : exception during call chain: Unable to get template body from input: {'StackName': 'test-stack', 'UsePreviousTemplate': True, 'Parameters': [{'ParameterKey': 'MyRoleName', 'ParameterValue': 'sample-test-role-new'}]}
2023-07-01 13:45:17 2023-07-01T08:15:17.229  INFO --- [   asgi_gw_1] localstack.request.aws     : AWS cloudformation.UpdateStack => 500 (InternalError)
```
