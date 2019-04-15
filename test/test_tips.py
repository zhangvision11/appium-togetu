from base.action import ElementActions
from page.pages import *

class Test_tips():
    def swip_down(self,action:ElementActions):

        assert action.is_text_displayed()