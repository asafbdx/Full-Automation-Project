from selenium.webdriver.common.by import By


#Page Object Model for the Windows Calculator (Standard Mode).

#This file defines:
#- Locators for all calculator buttons and result field.
#- The StandardPage class with methods to access each UI element.

#Purpose:
#Encapsulate calculator UI elements in a single page object to keep desktop
#automation tests clean, reusable, and maintainable.


zero = (By.XPATH,"//*[@AutoumationId='num0Button']")
one = (By.XPATH,"//*[@AutomationId='num1Button']")
two = (By.XPATH,"//*[@AutomationId='num2Button']")
three = (By.XPATH,"//*[@AutomationId='num3Button']")
four = (By.XPATH,"//*[@AutomationId='num4Button']")
five = (By.XPATH,"//*[@AutomationId='num5Button']")
six = (By.XPATH,"//*[@AutomationId='num6Button']")
seven = (By.XPATH,"//*[@AutomationId='num7Button']")
eight = (By.XPATH,"//*[@AutomationId='num8Button']")
nine = (By.XPATH,"//*[@AutomationId='num9Button']")
delete = (By.XPATH,"//*[@AutomationId='backSpaceButton']")
clear = (By.XPATH,"//*[@AutomationId='clearButton']")
plus = (By.XPATH,"//*[@AutomationId='plusButton']")
minus = (By.XPATH,"//*[@AutomationId='minusButton']")
divide = (By.XPATH,"//*[@AutomationId='divideButton']")
multi = (By.XPATH,"//*[@AutomationId='multiplyButton']")
equal = (By.XPATH,"//*[@AutomationId='equalButton']")
result = (By.XPATH,"//*[@AutomationId='CalculatorResults']")




class StandardPage:
    def __init__(self,driver):
        self.driver = driver

    def get_zero(self):
        return self.driver.find_element(zero[0],zero[1])

    def get_one(self):
        return self.driver.find_element(one[0],one[1])

    def get_two(self):
        return self.driver.find_element(two[0],two[1])

    def get_three(self):
        return self.driver.find_element(three[0],three[1])

    def get_four(self):
        return self.driver.find_element(four[0],four[1])

    def get_five(self):
        return self.driver.find_element(five[0],five[1])

    def get_six(self):
        return self.driver.find_element(six[0],six[1])

    def get_seven(self):
        return self.driver.find_element(seven[0],seven[1])

    def get_eight(self):
        return self.driver.find_element(eight[0],eight[1])

    def get_nine(self):
        return self.driver.find_element(nine[0],nine[1])

    def get_delete(self):
        return self.driver.find_element(delete[0],delete[1])

    def get_clear(self):
        return self.driver.find_element(clear[0],clear[1])

    def get_plus(self):
        return self.driver.find_element(plus[0],plus[1])

    def get_minus(self):
        return self.driver.find_element(minus[0],minus[1])

    def get_divide(self):
        return self.driver.find_element(divide[0],divide[1])

    def get_multi(self):
        return self.driver.find_element(multi[0],multi[1])

    def get_equal(self):
        return self.driver.find_element(equal[0],equal[1])

    def get_result(self):
        return self.driver.find_element(result[0],result[1])