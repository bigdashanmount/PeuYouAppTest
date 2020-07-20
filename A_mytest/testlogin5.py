import time
from base import DesireCaps
from base.BaseAction import Action
import unittest
from utils import LogUtil
import datetime
import ddt
nowtime = str(datetime.datetime.now())
LogUtil.my_log("记录日志unittest："+nowtime).info("测试开始执行unittest...")
test_data=[{"phone":"13582905701","password":"905701"}]
@ddt.ddt
class Login(unittest.TestCase):
   @ddt.data(*test_data)
   @ddt.unpack
   def test_login(self,phone,password):
       Desire_driver=DesireCaps.appium_desired_caps()
       driver=Action(Desire_driver)
       # 点击密码登录
       driver.click_btn(by="id", value="com.stoneenglish:id/quick_to_login")
       LogUtil.my_log("登陆日志：").info("点击选择密码登录")
       # 输入手机号
       time.sleep(3)
       driver.click_btn(by="id", value="com.stoneenglish:id/login_tel")
       time.sleep(3)
       driver.send_keys(by="id", value="com.stoneenglish:id/login_tel", send=phone)
       LogUtil.my_log("登陆日志：").info("输入手机号")
       time.sleep(2)
       driver.click_btn(by="id", value="com.stoneenglish:id/login_password")
       driver.send_keys(by="id", value="com.stoneenglish:id/login_password", send=password)
       LogUtil.my_log("登陆日志：").info("输入密码")
       time.sleep(3)
       driver.click_btn(by="id", value="com.stoneenglish:id/login_ok")
       driver.is_toast_exist(expect="登录成功")
       driver.assert_toast_result(expect="登录成功")


if __name__ == "__main__":
    unittest.main(verbosity=2)