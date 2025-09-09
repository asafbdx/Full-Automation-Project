import allure
import pytest

from extensions.verifiactions import Verifications
from workflows.electron_flows import ElectronFlows


# Automated tests for the Electron-based Task Management app.
#
# This file defines:
# - Adding a single new task and verifying it appears in the list.
# - Adding multiple tasks and verifying the correct number is displayed.
#
# Purpose:
# Provide automated coverage for core task management functionality in the Electron app,
# ensuring tasks can be created, counted, and managed reliably.


@pytest.mark.usefixtures("init_electron_driver")
class Test_Electron:
    @allure.title("Test 01 : Add and Verify New Task")
    @allure.description("This test add a new task and verifies it in the list of tasks")
    def test_add_and_verify_new_task(self):
        ElectronFlows.add_new_task_flow("Learn Python")
        Verifications.verify_equals(ElectronFlows.get_number_of_tasks_flow(), 1 )


    @allure.title("Test 02 : Add and Verify New Tasks")
    @allure.description("This test add a new tasks and verifies them in the list of tasks")
    def test_add_and_verify_new_tasks(self):
        ElectronFlows.add_new_task_flow("Learn Java")
        ElectronFlows.add_new_task_flow("Learn C#")
        ElectronFlows.add_new_task_flow("Learn JS")
        Verifications.verify_equals(ElectronFlows.get_number_of_tasks_flow(), 3 )


        
    def teardown_method(self):
        ElectronFlows.empty_list_flow()

