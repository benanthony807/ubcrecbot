from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class UBCRecBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password

    def run(self):
        self.login()
        self.wait_until_ready()
        self.check_timeslots()

    def login(self):
        # go to website
        self.driver.get(
            "https://ubc.perfectmind.com/24063/Clients/BookMe4BookingPages/Classes?calendarId=3f71aec7-92b6-423d-8d3c-6d111c267a32&widgetID=15f6af07-39c5-473e-b053-96653f77a406")
        # click login button
        self.wait_then_click("//a[@class='pm-button pm-login-button']")
        # click cwl button
        self.wait_then_click("//a[@href='/sso/index.php']")
        # enter username and pw
        self.driver.find_element_by_xpath("//input[@id='username']").send_keys(self.username)
        self.driver.find_element_by_xpath("//input[@id='password']").send_keys(self.password)
        # click login
        self.driver.find_element_by_xpath("//button[@type='submit']").click()

    def wait_then_click(self, xpath):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()

    def check_timeslots(self):
        # waits for page to load then finds button of first available slot and clicks it
        self.wait_then_click("//input[@value='Register Now']")
        self.register()

    def register(self):
        # click REGISTER NOW
        self.wait_then_click("//a[@class='bm-button bm-book-button']")
        # click next button
        self.wait_then_click("//a[@title='Next']")
        # click next again
        self.wait_then_click("//a[@title='Next']")
        # click checkout
        self.wait_then_click("//span[@id='checkoutButton']")

    def wait_until_ready(self):
        time.sleep(54)
        self.driver.refresh()


def main():
    my_bot = UBCRecBot('benantho', 'rYb5dEZFr@uNfNK')
    my_bot.run()


if __name__ == '__main__':
    main()
