import re
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

video_link = input(">>> ")


def is_valid(link):
    is_valid = re.search("^https:\/\/www\.youtube\.com\/watch\?v=.+$", link)
    return True if is_valid is not None else False


if is_valid(video_link):
    downloader_link = list(video_link)
    downloader_link.insert(12, "ss")
    downloader_link = "".join(downloader_link)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get(downloader_link)
    button = driver.find_element_by_xpath('def-btn-box')
    button.click()
else:
    print("The link that you have entered is not valid.")
    exit()