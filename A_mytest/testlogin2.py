from appium import webdriver
import time
from base import DesireCaps
from utils import LogUtil
driver=DesireCaps.appium_desired_caps(host="127.0.0.1",port="4723")
LogUtil.my_log("这是日志啊1").info("11111111111111111111111111111111111111111111111111")
#点击密码登录
driver.find_element_by_id("com.stoneenglish:id/quick_to_login").click()
#输入手机号
time.sleep(3)
driver.find_element_by_id("com.stoneenglish:id/login_tel").click()
time.sleep(3)
driver.find_element_by_id("com.stoneenglish:id/login_tel").send_keys("13582905701")
time.sleep(2)
driver.find_element_by_id("com.stoneenglish:id/login_password").click()
driver.find_element_by_id("com.stoneenglish:id/login_password").send_keys("905701")
time.sleep(2)
driver.find_element_by_id("com.stoneenglish:id/login_ok").click()

time.sleep(5)
driver.quit()