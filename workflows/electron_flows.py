import time

import allure
from selenium.webdriver.common.keys import Keys

import utilities.manage_pages as page
from extensions.ui_actions import UiActions


# Flow layer for automating the Electron-based Task app.
#
# This file defines:
# - add_new_task_flow → Adds a new task via the input field.
# - get_number_of_tasks_flow → Returns the number of tasks currently in the list.
# - empty_list_flow → Removes all tasks from the list.
#
# Purpose:
# Provide reusable flows for interacting with the Electron task management app,
# encapsulating UI actions to keep Electron test cases clean and maintainable.



class ElectronFlows:
    @staticmethod
    @allure.step("Add new task flow")
    def add_new_task_flow(task_name):
        UiActions.update_text(page.electron_task.get_create(), task_name)
        UiActions.update_text(page.electron_task.get_create(), Keys.RETURN)


    @staticmethod
    @allure.step("Get number of tasks")
    def get_number_of_tasks_flow():
        return len(page.electron_task.get_tasks())


    @staticmethod
    @allure.step("Empty task from list flow")
    def empty_list_flow():
        for x in range(ElectronFlows.get_number_of_tasks_flow()):
            time.sleep(0.5)
            UiActions.mouse_hover_tooltip(page.electron_task.get_delete_buttons()[0])

