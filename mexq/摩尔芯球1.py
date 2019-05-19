#! /usr/bin/python
# -*- coding:utf-8 -*-

# 摩尔芯球
from appium import webdriver
from time import sleep
from 抖音 import duanxin
def one():
    a = {
                "device": "android",
                "platformName": "Android",
                "platformVersion": "9",
                "deviceName": "8TFDU18814005741",
                "appPackage": "com.mooreshare.app",
                "appActivity": ".ui.activity.MainActivity",
                "noReset": "True"}
    dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities= a)
    sleep(1)
    dr.find_element_by_id('com.mooreshare.app:id/iv_menuitem4').click()
    sleep(1)
    dr.find_element_by_id('com.mooreshare.app:id/tv_login_1').click()
    sleep(2)
    dr.find_element_by_id('com.mooreshare.app:id/et_search_content').send_keys('17633926139')
    dr.find_element_by_id('com.mooreshare.app:id/tv_verificate').click()
    sleep(10)
def two():
    c = duanxin()
    a = {
        "device": "android",
        "platformName": "Android",
        "platformVersion": "9",
        "deviceName": "8TFDU18814005741",
        "appPackage": "com.mooreshare.app",
        "appActivity": ".ui.activity.MainActivity",
        "noReset": "True"}
    dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=a)
    sleep(1)
    dr.find_element_by_id('com.mooreshare.app:id/iv_menuitem4').click()
    sleep(1)
    dr.find_element_by_id('com.mooreshare.app:id/tv_login_1').click()
    sleep(2)
    dr.find_element_by_id('com.mooreshare.app:id/et_search_content').send_keys('17633926139')
    sleep(2.0)
    a = dr.find_elements_by_class_name('android.widget.EditText')
    a[1].send_keys(c)
    # 通过邮箱账号登录
    #  dr.find_element_by_id('com.mooreshare.app:id/rl_login_by_mail').click()
    # sleep(2)
    # ab = dr.find_elements_by_class_name("android.widget.EditText")
    # ab[0].send_keys("123456")
    # sleep(2)
    # ab[1].send_keys("zz1324567")
    # 点击微信登录
    # dr.find_element_by_id('com.mooreshare.app:id/iv_weixin').click()
    # sleep(2)
    # dr.find_element_by_id('com.mooreshare.app:id/iv_bar_operate1').click()
    # sleep(2)
    dr.find_element_by_id('com.mooreshare.app:id/login_bt').click()
    sleep(10.0)
    # dr.find_element_by_id('com.mooreshare.app:id/rl_menu4').click()
    dr.find_element_by_id('com.mooreshare.app:id/iv_bar_operate1').click()
    sleep(2)
    dr.find_element_by_id('com.mooreshare.app:id/bt_logout').click()
    sleep(3)
    dr.quit()
one()
two()






#         size = dr.get_window_size()
#         x1 = size['width'] * 0.75
#         x2 = size['height'] * 0.2
#         y1 = size['height'] * 0.25
#         for i in range(4):
#             for j in range(3):
#                 dr.swipe(x1,y1,x2,y1)
#             sleep(1.5)
# qwe().slide()