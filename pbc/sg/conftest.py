import pytest
from pbc.fixtures.firefox_connector import ConnectorFirefox
from pbc.fixtures.ssh_connector import ConnectorSSH
from pbc.fixtures.remote_firefox import RemoteFireFox


@pytest.fixture(scope='module')
def ssh(request):
    fixture = ConnectorSSH(ip='192.168.33.10', username='vagrant', password='vagrant')
    fixture.connect()
    request.addfinalizer(fixture.destroy)
    return fixture


@pytest.fixture(scope='session')
def firefox(request):
    fixture = ConnectorFirefox()
    request.addfinalizer(fixture.destroy)
    return fixture


@pytest.fixture(scope='session')
def remote_ff(request):
    fixture = RemoteFireFox('http://192.168.33.10:4444/wd/hub')
    request.addfinalizer(fixture.destroy)
    return fixture
