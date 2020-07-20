import pytest
from utils.LogUtil import my_log
from conf import Conf
from base.ExcelData import Data
import time
from base.DesireCaps import appium_desired_caps
from testcase.operate.KeywordOperatePytest02 import Operate
log = my_log("TestKeywords")
data = Data(Conf.testcase_file)
#执行测试用例列表
run_list = data.run_list()
#1、创建测试用例方法
class TestKeyword:
    # def test_run(self,start_appium_desired):
    #     print("1111111111111111111234")
    #     pass
    #def setup_class(self):
     #   self.driver = appium_desired_caps()
    #def setup(self):
     #    self.driver.launch_app()
# 2、重构代码
    @pytest.mark.parametrize("run_case",run_list)
    def test_run(self,start_appium_desired,run_case):
        self.driver = start_appium_desired
       # self.driver.launch_app()
        log.info("执行用例内容:{}".format(run_case))
        time.sleep(2)
        #调用操作类，传入driver驱动
        Operate(self.driver).step(data,run_case)
#3、增加setup teardown
    def teardown(self):
        self.driver.close_app()
    #def teardown_class(self):
        #self.driver.quit()