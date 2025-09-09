from selenium.webdriver.common.by import By

#Page Object Model for the Task Management application.

#This file defines:
#- Locators for creating tasks, listing tasks, and deleting tasks.
#- The TaskPage class with methods to interact with these elements.

#Purpose:
#Provide a clean, reusable interface for task-related UI interactions,
#keeping web automation tests organized and maintainable.



create = (By.CSS_SELECTOR,"input[placeholder='Create a task']")
tasks = (By.CSS_SELECTOR,"[class='view_2Ow90']")
delete_button = (By.XPATH,"//div[@class='view_2Ow90']/*[name()='svg']")


class TaskPage:
    def __init__(self,driver):
        self.driver = driver

    def get_create(self):
        return self.driver.find_element(create[0],create[1])

    def get_tasks(self):
        return self.driver.find_elements(tasks[0],tasks[1])

    def get_delete_buttons(self):
        return self.driver.find_elements(delete_button[0],delete_button[1])