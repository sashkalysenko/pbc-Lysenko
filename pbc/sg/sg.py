from abc import ABCMeta, abstractmethod


class BaseGrid:
    __metaclass__ = ABCMeta

    @abstractmethod
    def start_hub(self):
        print 'Starting hub...'
        pass

    @abstractmethod
    def add_node(self):
        print 'Adding node...'
        pass

    @abstractmethod
    def download(self):
        print 'Downloading Selenium server...'
        pass

    @abstractmethod
    def download_node_config(self):
        print 'Downloading config...'
        pass


class Grid(BaseGrid):

    def __init__(self, ssh):
        self._client = ssh

    def start_hub(self):
        self._client.execute_command("java -jar selenium-server-standalone-3.8.0.jar -role hub >> log.txt 2>&1 &")

    def download(self):
        self._client.execute_command("wget -O selenium-server-standalone-3.8.0.jar https://goo.gl/SVuU9X")

    def download_node_config(self):
        self._client.execute_command("wget -O sg-node.json "
                                     "https://gist.github.com/extsoft/aed4cb6e0b1ae3cd1d38cafffdd79310/raw/")

    def add_node(self):
        self._client.execute_command("java -jar selenium-server-standalone-3.8.0.jar -role node  -nodeConfig "
                                     "sg-node.json >> log.txt 2>&1 &")

    def is_downloaded(self):
        if 'True' in self._client.execute_command("[ -f selenium-server-standalone-3.8.0.jar ] && echo 'True'"):
            return True
        else:
            return False


class StartGrid(BaseGrid):

    def __init__(self, grid):
        self._g = grid
        self._is_downloaded = grid.is_downloaded()

    def start_hub(self):
        self._g.start_hub()

    def add_node(self):
        self._g.add_node()

    def download(self):
        if not self._is_downloaded:
            self._g.download()
        else:
            print 'Selenium server already downloaded'

    def download_node_config(self):
        self._g.download_node_config()
