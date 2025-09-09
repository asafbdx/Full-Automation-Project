from selenium.webdriver.common.by import By

#Page Object Model for the Mobile Loan Calculator (Saved Records).

#This file defines:
#- Locators for saved amount, term, rate, and delete actions.
#- The SavedPage class with methods to access these UI elements.

#Purpose:
#Provide a reusable interface for interacting with saved loan records,
#including viewing details and deleting entries, to keep mobile tests
#organized and maintainable.


amount = (By.ID,"tvAmount")
term = (By.ID,"tvTerm")
rate = (By.ID,"tvRate")
delete = (By.ID,"btnDel")
confirm_delete = (By.XPATH,"//*[@text='OK']")


class SavedPage:
    def __init__(self,driver):
        self.driver = driver

    def get_amount(self):
        return self.driver.find_element(amount[0],amount[1])

    def get_term(self):
        return self.driver.find_element(term[0],term[1])

    def get_rate(self):
        return self.driver.find_element(rate[0],rate[1])

    def get_delete(self):
        return self.driver.find_element(delete[0],delete[1])

    def get_confirm_delete(self):
        return self.driver.find_element(confirm_delete[0],confirm_delete[1])