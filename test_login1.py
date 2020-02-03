#!/usr/bin/env python
# coding=utf-8

import time
from selenium import webdriver

class CodeSpider:
    cookie_file = './cookies'
    path = r'/home/szt/pachongceshi/'
    dict = {}
    my_cookie = {}
    url = ""

    def __init__(self, url):
        self.url = url
        driver = webdriver.Chrome()
        driver.get('https://www.baidu.com')
        with open(self.cookie_file, "r") as f:
            for line in f:
                name, value, domain = line.strip().split('\t')
                self.my_cookie = {"name" : name, "value" : value, "domain" : domain}
                driver.add_cookie(self.my_cookie)
        driver.get(self.url)
        self.driver = driver
        self.dict.clear()

    def get_url(self):
        self.driver.refresh()
        if self.url == 'https://www.jisuanke.com/course/788' or self.url == 'https://www.jisuanke.com/course/786':
            self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div/div[2]/ul/li/a').click()
        lessons = self.driver.find_elements_by_css_selector("[class='jsk-list jsk-list-striped lessons']")
        for x in lessons:
            status = x.find_elements_by_tag_name("li")
            for y in status:
                spans = y.find_elements_by_tag_name('span')
                if spans[0].get_attribute('title') == "已完成" and spans[0].get_attribute("class") == "lesson-icon-challenge":
                    temp_link = y.find_element_by_tag_name('a').get_attribute('href')
                    temp_link_name = spans[1].get_attribute('title')
                    self.dict[temp_link_name] = temp_link
    
    def get_code(self):
        for y in self.dict.keys():
            self.driver.get(self.dict[y])
            self.driver.refresh()
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="finish-footer"]/div[2]/a[1]').click()
            time.sleep(1)
            self.driver.find_element_by_id("submit-history-trigger").click()
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="submit-history"]/div/div[2]/table/tbody/tr/td[5]/a').click()
            time.sleep(1)
            self.driver.switch_to_window(self.driver.window_handles[1])
            time.sleep(0.5)
            tmp_str = self.driver.find_element_by_tag_name('pre').text
            time.sleep(1)
            self.save(y, tmp_str)
            self.driver.close()
            self.driver.switch_to_window(self.driver.window_handles[0]) 
        time.sleep(5)
        self.driver.quit()

    def save(self, filename, contents):
        tmp_path = self.path + filename
        fh = open(tmp_path, 'w', encoding='utf-8')
        fh.write(contents)
        fh.close()

