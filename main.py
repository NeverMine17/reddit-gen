from selenium import webdriver
import random
import string
import time

signupbuttonxpath = r'/html/body/div[3]/div/div/div[1]/form/div[8]/button'  # The signup button
posttextxpath = r'/html/body/div[4]/form/div[1]/div[2]/div[3]/div/div/textarea'  # The text form
postbuttonxpath = r'/html/body/div[4]/form/div[4]/button'


def randomword(length: int):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))


if __name__ == "__main__":
    nick: str = randomword(16)
    password: str = randomword(16)
    session = webdriver.Firefox()
    session.get("https://reddit.com/login")
    session.find_element_by_id("user_reg").send_keys(nick)  # Login in
    time.sleep(random.random() % 5)
    session.find_element_by_id("passwd_reg").send_keys(password)
    time.sleep(random.random() % 5)
    session.find_element_by_id("passwd2_reg").send_keys(password)
    time.sleep(random.random() % 5)
    input()
    session.find_element_by_xpath(signupbuttonxpath).click()
    time.sleep(random.random() % 5)
    session.get("https://www.reddit.com/r/sharedlogins/submit?selftext=true")
    session.find_element_by_xpath(posttextxpath).send_keys(nick + ':' + password)
    input()
    session.find_element_by_xpath(postbuttonxpath).click()
