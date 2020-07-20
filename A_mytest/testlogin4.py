import time
from base import DesireCaps
from base.BaseAction import Action
import unittest
from utils import LogUtil
import datetime
nowtime = str(datetime.datetime.now())
LogUtil.my_log("记录日志unittest："+nowtime).info("测试开始执行unittest...")
class Login(unittest.TestCase):
   def test_login(self):
       Desire_driver=DesireCaps.appium_desired_caps()
       driver=Action(Desire_driver)
       # 点击密码登录
       driver.click_btn(by="id", value="com.stoneenglish:id/quick_to_login")
       LogUtil.my_log("登陆日志：").info("点击选择密码登录")
       # 输入手机号
       time.sleep(3)
       driver.click_btn(by="id", value="com.stoneenglish:id/login_tel")
       time.sleep(3)
       driver.send_keys(by="id", value="com.stoneenglish:id/login_tel", send="13582905701")
       LogUtil.my_log("登陆日志：").info("输入手机号")
       time.sleep(2)
       driver.click_btn(by="id", value="com.stoneenglish:id/login_password")
       driver.send_keys(by="id", value="com.stoneenglish:id/login_password", send="905701")
       LogUtil.my_log("登陆日志：").info("输入密码")
       time.sleep(2)
       driver.click_btn(by="id", value="com.stoneenglish:id/login_ok")
       driver.is_toast_exist(expect="登录成功")
       driver.assert_toast_result(expect="登录成功")


#if __name__ == "__main__":
