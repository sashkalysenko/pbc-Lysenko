from selenium.webdriver.common.keys import Keys


class PythonOrg:

    def __init__(self, browser):
        self.driver = browser.wd
        self.driver.get("http://www.python.org")

    def save_screenshot(self, name):
        self.driver.save_screenshot(name)

    def search_for(self, text):
        elem = self.driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys(text)
        elem.send_keys(Keys.RETURN)

    def open_home_page(self):
        self.driver.get("http://www.python.org")
