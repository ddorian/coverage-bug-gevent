from webapp.doapp import app as the_app
import pytest

@pytest.fixture
def app():
    return the_app

def test_some(client):
    # gevent.spawn(do_stuff).join()
    # do_stuff()
    r0 = client.get('/')
    assert r0.status_code == 200
