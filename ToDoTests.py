import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


class MyTestCase(unittest.TestCase):
    __driver = None

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable_extensions")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--start-maximized")
        self.__driver = webdriver.Chrome(options=chrome_options)
        self.__driver.get("https://todomvc.com/examples/angularjs/#/")
        self.__driver.implicitly_wait(1)

    def test_1(self):
        self.add_task("Clean my house")
        self.assertTrue(self.find_clean_my_house_item(), "clean my house item was not added")

    def find_clean_my_house_item(self):
        try:
            item_to_check = self.__driver.find_element_by_css_selector("body > ng-view > section > section > ul > li > div > label")
            if item_to_check.text == "Clean my house":
                return True
            else:
                return False
        except:
            return False

    def test_2(self):
        self.add_task("Wake up")
        item_to_edit = self.__driver.find_element_by_css_selector("body > ng-view > section > section > ul > li > div > label")
        action = ActionChains(self.__driver)
        action.double_click(item_to_edit)
        action.key_down(Keys.CONTROL)
        action.send_keys("a")
        action.key_up(Keys.CONTROL)
        action.send_keys("Go to sleep")
        action.perform()

    def test_3(self):
        self.add_task("Wake up")
        item_to_delete = self.__driver.find_element_by_css_selector("body > ng-view > section > section > ul > li:nth-child(1) > div > label")
        delete_button = self.__driver.find_element_by_css_selector("body > ng-view > section > section > ul > li:nth-child(1) > div > button")
        action = ActionChains(self.__driver)
        action.move_to_element(item_to_delete)
        action.click(delete_button)
        action.perform()

    def test_4(self):
        self.add_task("Wake up")
        item_to_complete = self.__driver.find_element_by_css_selector("body > ng-view > section > section > ul > li:nth-child(1) > div > label")
        self.complete_task(item_to_complete)

    def test_5(self):
        self.test_4()
        item_to_uncomplete = self.__driver.find_element_by_css_selector("body > ng-view > section > section > ul > li:nth-child(1) > div > label")
        complete_button = self.__driver.find_element_by_css_selector("body > ng-view > section > section > ul > li > div > input")
        action = ActionChains(self.__driver)
        action.move_to_element(item_to_uncomplete)
        action.click(complete_button)
        action.perform()

    def test_6(self):
        self.add_task("Clean the house")
        self.add_task("Wake up")
        item_to_complete = self.__driver.find_element_by_css_selector("body > ng-view > section > section > ul > li:nth-child(1) > div > label")
        self.complete_task(item_to_complete)
        self.remove_completed()

    def test_7(self):
        self.add_task("Clean the house")
        self.add_task("Wake up")
        item_to_complete = self.__driver.find_element_by_css_selector("body > ng-view > section > section > ul > li:nth-child(1) > div > label")
        self.complete_task(item_to_complete)
        time.sleep(2)
        active_view_button = self.__driver.find_element_by_css_selector("body > ng-view > section > footer > ul > li:nth-child(2) > a")
        active_view_button.click()
        time.sleep(2)
        completed_view_button = self.__driver.find_element_by_css_selector("body > ng-view > section > footer > ul > li:nth-child(3) > a")
        completed_view_button.click()

    def complete_task(self, item_to_complete):
        complete_button = self.__driver.find_element_by_css_selector("body > ng-view > section > section > ul > li > div > input")
        action = ActionChains(self.__driver)
        action.move_to_element(item_to_complete)
        action.click(complete_button)
        action.perform()

    def add_task(self, task_name):
        new_to_do_item = self.__driver.find_element_by_css_selector("form [placeholder='What needs to be done?']")
        new_to_do_item.click()
        new_to_do_item.send_keys(task_name + "\n")

    def remove_completed(self):
        remove_completed_button = self.__driver.find_element_by_css_selector("body > ng-view > section > footer > button")
        remove_completed_button.click()


    def tearDown(self):
        time.sleep(2)
        self.__driver.close()


if __name__ == '__main__':
    unittest.main()
