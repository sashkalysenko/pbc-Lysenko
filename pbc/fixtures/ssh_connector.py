import paramiko
import time


class ConnectorSSH:

    def __init__(self, ip=None, username=None, password=None):
        self._ip = ip
        self._username = username
        self._password = password
        self._client = paramiko.SSHClient()

    def connect(self):
        """Initiates connection with VM via SSH"""

        print("Connecting to VM...")
        self._client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        self._client.connect(self._ip, username=self._username, password=self._password)
        stdin, stdout, stderr = self._client.exec_command('hostname')
        for line in stdout:
            print('... ' + line.strip('\n'))

    def execute_command(self, command):
        """Executes commands on connected VM"""

        if self._client:
            stdin, stdout, stderr = self._client.exec_command(command)

            while not stdout.channel.exit_status_ready():
                time.sleep(1)

            status = stdout.channel.recv_exit_status()
            if status == 0:
                print 'Successful...'.format(command)
                return [str(x) for x in stdout]
            else:
                print 'Execution failed with status:{}'.format(status)
                return [str(x) for x in stderr]

        else:
            raise Exception("Connection has been lost. Try to reconnect and execute command again.")

    def destroy(self):
        if self._client:
            print("Closing SSH connection...")
            self._client.close()
