import pytest
from fixtures.ssh_connector import ConnectorSSH
from fixtures.firefox_connector import ConnectorFirefox


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
