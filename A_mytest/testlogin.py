from appium import webdriver
import time
# 2、desired创建字典
desired_caps = dict()
# 3、platformName
desired_caps['platformName'] = 'Android'
# 4、platformVersion
desired_caps['platfromVersion'] = '5.0'
# 5、deviceName
time
desired_caps['deviceName'] ='OPPO_R17_Pro'
# 6、启动程序的包名appPackage
desired_caps["appPackage"] = 'com.stoneenglish'
# 7、启动界面名appActivity
desired_caps['appActivity'] = 'com.stoneenglish.MainActivity'
print("11111111111111111111111111111111111")
driver =webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
print("1111111111222222222222222222211111111111")
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