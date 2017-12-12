import pytest
from fixtures.ssh_connector import ConnectorSSH


@pytest.fixture(scope='module')
def ssh(request):
    fixture = ConnectorSSH(ip='192.168.33.10', username='vagrant', password='vagrant')
    fixture.connect()
    request.addfinalizer(fixture.destroy)
    return fixture
