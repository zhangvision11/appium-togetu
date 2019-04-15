# -*- coding: utf-8 -*-
from base.action import ElementActions
from page.pages import *
from test.steps import Steps
from test import test_login
import time

class Test_HomePage():

    """
        需要先登陆
    """

    def test_otherHomepage(self, action: ElementActions):
        assert not action.is_element_displayed(MyPage.名字)





