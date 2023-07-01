import localstack_client.session
import pytest
import boto3

from app import create_my_stack, update_my_stack


@pytest.fixture(autouse=True)
def boto3_localstack_patch(monkeypatch):
    session_ls = localstack_client.session.Session()
    monkeypatch.setattr(boto3, "client", session_ls.client)
    monkeypatch.setattr(boto3, "resource", session_ls.resource)

@pytest.fixture(autouse=True)
def setup():

    s3 = boto3.resource('s3')
    BUCKET = "test-bucket"
    s3.Bucket(BUCKET).create()
    s3.Bucket(BUCKET).upload_file("iam-role.yml", "iam-role.yml")
    print("File uploaded to bucket :", BUCKET)


def test_create_stack():

    assert create_my_stack() == True


def test_update_stack():

    assert update_my_stack() == True
