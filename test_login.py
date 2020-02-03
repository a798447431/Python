#!/usr/bin/env python
# coding=utf-8

import time
from selenium import webdriver

dict = {}
my_cookie = {}

class CodeSpider:
    url = "https://www.jisuanke.com/course/786?view=study"
    cookie_file = './cookies'
    
    def __init__(self):
        driver = webdriver.Chrome()
        driver.get('https://passport.jisuanke.com/?n=https://www.jisuanke.com/course/786#/')
        with open(self.cookie_file, "r") as f:
            for line in f:
                name, value, domain = line.strip().split('\t')
                my_cookie = {"name" : name, "value" : value, "domain" : domain}
                driver.add_cookie(my_cookie)
        driver.get(self.url)
        self.driver = driver    

def login():
    #url = 'https://passport.jisuanke.com/?n=https://www.jisuanke.com/course/786#/'
    url = 'https://www.baidu.com'
    driver = webdriver.Chrome()
    driver.get(url)
    add_cookie('./cookies', driver)
    
    '''
    name_input = driver.find_element_by_xpath('//*[@id="entry-panel"]/div/div[1]/div/div/div[1]/input')
    passwd_input = driver.find_element_by_xpath('//*[@id="entry-panel"]/div/div[1]/div/div/div[2]/input')
    login_button = driver.find_element_by_xpath('//*[@id="entry-panel"]/div/div[1]/div/div/a')

    name_input.clear()
    name_input.send_keys(username)
    time.sleep(0.2)

    passwd_input.clear()
    passwd_input.send_keys(passwd)
    time.sleep(0.2)

    login_button.click()

    time.sleep(2)
    print(driver.get_cookies())

    time.sleep(0.2)
    print(driver.title)
    '''

    driver.refresh()
    
    course = "https://www.jisuanke.com/course/786?view=study"
    driver.get(course)
    time.sleep(2)
    
    """
    lessons = driver.find_elements_by_css_selector("[class='jsk-list jsk-list-striped lessons']")
    print("lessons: ")
    print(len(lessons))
    for x in lessons:
        status = x.find_elements_by_tag_name("li")
        for y in status:
            spans = y.find_elements_by_tag_name('span')
            if spans[0].get_attribute('title') == "已完成" and spans[0].get_attribute("class") == "lesson-icon-challenge":
                print(spans[1].get_attribute('title'),end=" ")
                temp_link = y.find_element_by_tag_name('a').get_attribute('href')
                print(temp_link)
                driver.get(temp_link)
                driver.refresh()
                time.sleep(0.5)
                driver.find_element_by_xpath('//*[@id="finish-footer"]/div[2]/a[1]').click()
                time.sleep(0.5)
                driver.find_element_by_id("submit-history-trigger").click()
                time.sleep(0.5)
                driver.find_element_by_xpath('//*[@id="submit-history"]/div/div[2]/table/tbody/tr/td[5]/a').click()
                time.sleep(5)
                driver.back()     
                driver.refresh()
                time.sleep(0.5)
    """
    lessons = driver.find_elements_by_css_selector("[class='jsk-list jsk-list-striped lessons']")
    for x in lessons:
        status = x.find_elements_by_tag_name("li")
        for y in status:
            spans = y.find_elements_by_tag_name('span')
            if spans[0].get_attribute('title') == "已完成" and spans[0].get_attribute("class") == "lesson-icon-challenge":
                temp_link = y.find_element_by_tag_name('a').get_attribute('href')
                temp_link_name = spans[1].get_attribute('title')
                dict[temp_link_name] = temp_link
    for y in dict.keys():
        driver.get(dict[y])
        driver.refresh()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="finish-footer"]/div[2]/a[1]').click()
        time.sleep(1)
        driver.find_element_by_id("submit-history-trigger").click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="submit-history"]/div/div[2]/table/tbody/tr/td[5]/a').click()
        time.sleep(1)
        driver.switch_to_window(driver.window_handles[1])
        time.sleep(0.5)
        tmp_str = driver.find_element_by_tag_name('pre').text
        time.sleep(1)
        save(y, tmp_str)
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        
    time.sleep(5)
    driver.quit()

def save(filename, contents):
    tmp_path = "/home/szt/pachongceshi/" + filename
    fh = open(tmp_path, 'w', encoding='utf-8')
    fh.write(contents)
    fh.close()

def add_cookie(filename, driver):
    for line in open(filename):
        name, value, domain = line.strip().split('\t')
        my_cookie = {"name" : name, "value" : value, "domain" : domain}
        driver.add_cookie(my_cookie)

if __name__ == "__main__":
    username = "18645861772"
    passwd = "szt35361337393."
    login()
