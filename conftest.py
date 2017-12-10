import pytest
from fixtures.ssh_connector import ConnectorSSH


@pytest.fixture(scope='module')
def ssh(request):
    ssh_con = ConnectorSSH(ip='192.168.33.10', username='vagrant', password='vagrant')
    ssh_con.connect()
    ssh_con.set_up_selenium_server()

    def fin():
        ssh_con.destroy()

    request.addfinalizer(fin)
