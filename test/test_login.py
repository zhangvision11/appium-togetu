# -*- coding: utf-8 -*-

from base.action import ElementActions
from page.pages import *
from test.steps import Steps
from utils import L


from appium.webdriver.common import touch_action as ta
import time
from appium import webdriver

class TestLogin:


    def test_login(self, action: ElementActions):
        L.d('test_login')
        """
        检查是否在登录状态，在登陆的话就退出登录再登录
        """
        action.click(HomePage.我的)
        if action.is_text_displayed('like'):
            action.click(MyPage.设置)
            action.click(SettingPage.登出)
            action.click(SettingPage.确定)
            action.click(HomePage.我的)

        else: pass
        action.click(HomePage.登陆按钮)
        action.sleep(1)
        action.text(LoginPage.手机号, '96522075359')
        action.click(LoginPage.获取验证码)
        action.sleep(1)
        action.text(LoginPage.密码, '2333')
        action.sleep(0.5)
        action.click(LoginPage.登陆)
        assert action.get_text(MyPage.名字) == 'kirua'



