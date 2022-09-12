import re
from selenium import webdriver

video_link = input(">>> ")


def is_valid(link):
    is_valid = re.search("^https:\/\/www\.youtube\.com\/watch\?v=.+$", link)
    return True if is_valid is not None else False


if is_valid(video_link):
    downloader_link = list(video_link)
    downloader_link.insert(12, "ss")
    downloader_link = "".join(downloader_link)

    driver = webdriver.Chrome(r"./driver/chromedriver")
    driver.get(downloader_link)

    button = driver.find_element_by_class("submit")
    button.click()
else:
    print("The link that you have entered is not valid.")
    exit()
