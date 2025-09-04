from selenium.webdriver.common.by import By
left_menu_open = (By.CLASS_NAME,"css-r835kn-toolbar-button")
home_page = (By.XPATH,"//span[@class='css-uantyg' and text()='Home']")
bookmarks = (By.XPATH,"//span[@class='css-uantyg' and text()='Bookmarks']")
starred = (By.XPATH,"//span[@class='css-uantyg' and text()='Starred']")
dashboards = (By.XPATH,"//span[@class='css-uantyg' and text()='Dashboards']")
explore = (By.XPATH,"//span[@class='css-uantyg' and text()='Explore']")
alerting = (By.XPATH,"//span[@class='css-uantyg' and text()='Alerting']")
connections = (By.XPATH,"//span[@class='css-uantyg' and text()='Connections']")
administration = (By.XPATH,"//span[@class='css-uantyg' and text()='Administration']")



class LeftMenuPage():
    def __init__(self,driver):
        self.driver = driver


    def get_left_menu_open(self):
        return self.driver.find_element(left_menu_open[0],left_menu_open[1])

    def get_home_page(self):
        return self.driver.find_element(home_page[0],home_page[1])

    def get_bookmarks(self):
        return self.driver.find_element(bookmarks[0],bookmarks[1])

    def get_starred(self):
        return self.driver.find_element(starred[0],starred[1])

    def get_dashboards(self):
        return self.driver.find_element(dashboards[0],dashboards[1])

    def get_explore(self):
        return self.driver.find_element(explore[0],explore[1])

    def get_alerting(self):
        return self.driver.find_element(alerting[0],alerting[1])

    def get_connections(self):
        return self.driver.find_element(connections[0],connections[1])

    def get_administration(self):
        return self.driver.find_element(administration[0],administration[1])
