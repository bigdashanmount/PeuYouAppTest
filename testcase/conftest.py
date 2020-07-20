import pytest
from base.StartAppium import get_devices,appium_start,check_port
import time
from utils.LogUtil import my_log
from base.DesireCaps import appium_desired_caps
#1、自定义的定义命令--cmdopt选项类
log = my_log("TestKeywords")
def pytest_addoption(parser):
    parser.addoption("--cmdopt",action="store",default="run",help=None)
#2、接收命令
@pytest.fixture(scope="session")
def cmdopt(request):
    return request.config.getoption("--cmdopt")
#3、调用命令使用
@pytest.fixture(scope="session")
def start_appium_desired(cmdopt):
    opt = eval(cmdopt)
    #print(opt)
    #{ "host":"127.0.0.1",
     #          "port":"4723",
     #          "bpport":"4724",
      #         "udid":None}
    host = opt["host"]
    port = opt["port"]
    bpport = opt["bpport"]
    udid = opt["udid"]
    system_port = opt["systemPort"]
    # print("=========================================================")
    #print(opt)
    driver = None
   #  a=get_devices()
    if udid in get_devices():
         print(udid)
         #通过驱动CMD命令，启动服务
         appium_start(host,port,bpport,udid)
         time.sleep(8)
         if not check_port():
             #端口号被启动，则提供设备信息，去链接
            #driver = appium_desired_caps(host,port)
            driver = appium_desired_caps(host, port, system_port)
    #return driver
    yield driver
    driver.quit()
