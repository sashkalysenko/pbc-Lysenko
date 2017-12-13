from selenium import webdriver


class ConnectorFirefox:

    def __init__(self):
        self.wd = webdriver.Firefox()

    def destroy(self):
        self.wd.close()
