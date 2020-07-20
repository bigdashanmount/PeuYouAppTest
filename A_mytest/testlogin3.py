import time
from base import DesireCaps
from base.BaseAction import Action
from utils import LogUtil
import datetime
nowtime = str(datetime.datetime.now())
LogUtil.my_log("APP开始登录："+nowtime).info("APP登录开始执行...")
class CapsTest(Action):
    def __init__(self):
        driver=DesireCaps.appium_desired_caps()
        super().__init__(driver)

    def login_test(self):
        # 点击密码登录
        self.click_btn(by="id",value="com.stoneenglish:id/quick_to_login")
        LogUtil.my_log("登陆日志：").info("点击选择密码登录")
        # 输入手机号
        time.sleep(3)
        self.click_btn(by="id",value="com.stoneenglish:id/login_tel")
        time.sleep(3)
        self.send_keys(by="id",value="com.stoneenglish:id/login_tel",send="13582905701")
        LogUtil.my_log("登陆日志：").info("输入手机号")
        time.sleep(2)
        self.click_btn(by="id",value="com.stoneenglish:id/login_password")
        self.send_keys(by="id",value="com.stoneenglish:id/login_password",send="905701")
        LogUtil.my_log("登陆日志：").info("输入密码")
        time.sleep(2)
        self.click_btn(by="id", value="com.stoneenglish:id/login_ok")
        self.is_toast_exist(expect="登录成功")
if __name__ == "__main__":
    test=CapsTest()
    test.login_test()
