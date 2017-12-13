from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class RemoteFireFox:

    def __init__(self, url):
        self.options = Options()
        self.options.add_argument('--headless')
        self.wd = webdriver.Remote(
            command_executor=url,
            desired_capabilities={'browserName': 'firefox'},
            options=self.options)

    def destroy(self):
        self.wd.close()
