# -*- coding: utf-8 -*-
__author__ = 'Mio4kon'
import pytest
from appium import webdriver
from base.action import ElementActions
from utils.environment import Environment
import time
@pytest.fixture()
#主页面
def action():
    env = Environment().get_environment_info()
    capabilities = {'platformName': env.devices[0].platform_name,
                    'platformVersion': env.devices[0].platform_version,
                    'deviceName': env.devices[0].device_name,
                    'appPackage': 'in.togetu.video',
                    'clearSystemFiles': True,
                    'appActivity': env.app_activity,

                    'noReset':True,
                    'noSign': True
                    }
    host = "http://localhost:4723/wd/hub"
    driver = webdriver.Remote(host, capabilities)
    yield ElementActions(driver).reset(driver)
    driver.quit()


@pytest.fixture(scope="module")
    #评论页
def action_shot():
    env = Environment().get_environment_info()
    capabilities = {'platformName': env.devices[0].platform_name,
                    'platformVersion': env.devices[0].platform_version,
                    'deviceName': env.devices[0].device_name,
                    'appPackage': 'in.togetu.video',
                    'clearSystemFiles': True,
                    'appActivity': 'in.togetu.recorder.RecordActivity',

                    'noReset': True,
                    'noSign': True
                    }
    host = "http://localhost:4723/wd/hub"
    driver = webdriver.Remote(host, capabilities)

    yield ElementActions(driver).reset(driver)
    driver.quit()
