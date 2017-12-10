import paramiko
import time


class ConnectorSSH:

    def __init__(self, ip=None, username=None, password=None):
        self.ip = ip
        self.username = username
        self.password = password
        self.client = paramiko.SSHClient()

    def connect(self):
        """Initiates connection with VM via SSH"""

        print("Connecting to VM...")
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        self.client.connect(self.ip, username=self.username, password=self.password)
        stdin, stdout, stderr = self.client.exec_command('hostname')
        for line in stdout:
            print('... ' + line.strip('\n'))

    def set_up_selenium_server(self):
        """Installs and runs standalone selenium server 3.8.0"""
        self.client.exec_command('wget -O selenium-server-standalone-3.8.0.jar https://goo.gl/SVuU9X', timeout=10)
        time.sleep(15)
        self.client.exec_command('java -jar selenium-server-standalone-3.8.0.jar -role hub >> log.txt 2>&1 &')
        time.sleep(15)
        self.client.exec_command('java -jar selenium-server-standalone-3.8.0.jar -role node'
                                 ' -hub http://localhost:4444/grid/register >> log.txt 2>&1 &')

    def destroy(self):
        print("Closing SSH connection...")
        self.client.close()
