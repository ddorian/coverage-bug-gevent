from webapp.doapp import app as the_app
import pytest
from moto import mock_aws
import boto3

@pytest.fixture
def app():
    return the_app

@mock_aws
def test_some(client):
    conn = boto3.resource("s3", region_name="us-east-1")
    # We need to create the bucket since this is all in Moto's 'virtual' AWS account
    conn.create_bucket(Bucket="mybucket")
    # gevent.spawn(do_stuff).join()
    # do_stuff()
    r0 = client.get('/')
    assert r0.status_code == 200
