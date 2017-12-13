class GridConsole:

    def __init__(self, browser):
        self.driver = browser.wd
        self.driver.get("http://192.168.33.10:4444/grid/console#")

    def open_browsers(self):
        self.driver.find_element_by_css_selector("li[type='browsers']").click()

    def open_configuration(self):
        self.driver.find_element_by_css_selector("li[type='config']").click()

    def _is_tab_selected(self, tab_name):
        if self.driver.find_element_by_css_selector("li[type={0}]".format(tab_name)).get_attribute(
                "class").endswith('selected'):
            return True
        else:
            return False

    def get_amount_browsers(self):
        if not self._is_tab_selected('browsers'):
            self.open_browsers()
        return len(self.driver.find_elements_by_css_selector("div.content_detail[type='browsers'] img"))

    def get_ammount_sessions(self):
        if not self._is_tab_selected('config'):
            self.open_configuration()
        maxsession = int([x.text.split('maxSession: ')[1] for x in self.driver.find_elements_by_css_selector(
            "div.content_detail[type='config'] p") if x.text.startswith('maxSession')][0])
        return maxsession
