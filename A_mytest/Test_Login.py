import time
from base import DesireCaps
from base.BaseAction import Action
import unittest
from utils import LogUtil
import datetime
import ddt
nowtime = str(datetime.datetime.now())
LogUtil.my_log("记录日志unittest："+nowtime).info("测试开始执行unittest...")
@ddt.ddt
class Login(unittest.TestCase):
   @classmethod
   #setup类
   def setUpClass(cls):
       #初始化Appium
       LogUtil.my_log("setUpClass开启：" + nowtime).info("setUpClass开启...初始化Appium")
       cls.driver = DesireCaps.appium_desired_caps()
   # setup方法，初始化起点APP
   def setUp(self):
       LogUtil.my_log("setUpC开启：" + nowtime).info("setUp开启...初始化driver.launch_app()")
       self.driver.launch_app()
       self.Page_driver = Action(self.driver)
   @ddt.file_data("Test_Login_Ddt.yml")
   @ddt.unpack
   def test_login(self,phone,password):
       # 点击密码登录
       self.Page_driver.click_btn(by="id", value="com.stoneenglish:id/quick_to_login")
       LogUtil.my_log("登陆日志：").info("点击选择密码登录")
       # 输入手机号
       time.sleep(3)
       self.Page_driver.click_btn(by="id", value="com.stoneenglish:id/login_tel")
       time.sleep(3)
       self.Page_driver.send_keys(by="id", value="com.stoneenglish:id/login_tel", send=phone)
       LogUtil.my_log("登陆日志：").info("输入手机号")
       time.sleep(2)
       self.Page_driver.click_btn(by="id", value="com.stoneenglish:id/login_password")
       self.Page_driver.send_keys(by="id", value="com.stoneenglish:id/login_password", send=password)
       LogUtil.my_log("登陆日志：").info("输入密码")
       time.sleep(3)
       self.Page_driver.click_btn(by="id", value="com.stoneenglish:id/login_ok")
       self.Page_driver.is_toast_exist(expect="登录成功")
       self.Page_driver.assert_toast_result(expect="登录成功")
   # setup方法，初始化起点APP
   def tearDown(self):
       LogUtil.my_log("tearDown关闭：" + nowtime).info("tearDown关闭...driver.close_app()")
       self.driver.close_app()
   @classmethod
   def tearDownClass(cls):
       # 初始化Appium
       LogUtil.my_log("tearDownClassguanbi：" + nowtime).info("tearDownClass...关闭driver")
       cls.driver.quit()
if __name__ == "__main__":
    unittest.main(verbosity=2)