from selenium.webdriver.common.by import By

search = (By.CLASS_NAME,"css-xmqqi8-input-input")
new_user = (By.CSS_SELECTOR,"a[href='admin/users/create']")
users_list = (By.XPATH,"//table[@class='css-elscwy']/tbody/tr")
user_by_user_name = (By.XPATH, "//a[text()='user1']")
delete_user = (By.XPATH,"//span[@class='css-1riaxdn' and text()='Delete user']")
confirm_delete = (By.XPATH,"//button[@data-testid='data-testid Confirm Modal Danger Button']")

#user1 = fill the user you looking for


class UsersPage():
    def __init__(self,driver):
        self.driver = driver


    def get_search(self):
        return self.driver.find_element(search[0],search[1])

    def get_new_user(self):
        return self.driver.find_element(new_user[0],new_user[1])

    def get_users_list(self):
        return self.driver.find_elements(users_list[0],users_list[1])


    def get_delete(self):
        return self.driver.find_element(delete_user[0],delete_user[1])


    def get_confirm_delete(self):
        return self.driver.find_element(confirm_delete[0],confirm_delete[1])


    def get_user_by_index(self, index):
        return self.get_users_list()[index]

    def get_user_by_user_name(self, user):
        return self.driver.find_element(user_by_user_name[0],user_by_user_name[1].replace("user1", str(user)))