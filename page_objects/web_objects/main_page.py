from selenium.webdriver.common.by import By

main_title = (By.CLASS_NAME,"css-1ti7uft")

class MainPage():
    def __init__(self,driver):
        self.driver = driver


    def get_name_title(self):
        return self.driver.find_element(main_title[0],main_title[1])

