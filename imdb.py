# This is a working prototype which tells me whether to watch something or not.
# Mostly it works, sometimes there is a problem.
# I can't figure out how to use WebDriverWait.


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def content_advisory(name_of_movie):
    path = r'E:\c\Desktop\python projects\chromedriver.exe'
    driver = webdriver.Chrome(path)

    driver.get('https://www.imdb.com')
    search = driver.find_element_by_id('suggestion-search')
    search.send_keys(name_of_movie)
    time.sleep(5)
    search.send_keys(Keys.DOWN)

    search.send_keys(Keys.RETURN)
    time.sleep(4)

    rating = driver.find_element_by_class_name('ratingValue').text

    guide = driver.find_element_by_link_text('View content advisory').click()
    time.sleep(2)
    info = driver.find_element_by_id("advisory-nudity").text

    driver.quit()

    return 'rating is: ' + rating + '\n' + info

