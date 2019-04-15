from base.action import ElementActions
from page.pages import *
from test.steps import Steps
from test import test_login
import pytest
import allure




class Test_HomePage():

#缺少 hashtag集合页
    '''
    点赞
    '''

    def test_like(self,action: ElementActions):

        action.click(HomePage.点赞按钮)
        action.sleep(1)
        action.capture_screen(u'点赞截图', '/Users/zhangweishun/Desktop/appium-lich-master/screenshot/')

    '''
    下载
    
    '''

    def test_download(self,action: ElementActions):
        action.click(HomePage.下载按钮)
        action.sleep(2)

        # 断言再想想，很难想
        action.capture_screen(u'下载截图', '/Users/zhangweishun/Desktop/appium-lich-master/screenshot/')

        # assert int(atfter_like) == int(before_like) + 1
        # action.capture_screen()


    """
    关注，需要登陆
    """

    def test_add_poster(self, action: ElementActions):

            action.click(HomePage.关注按钮)
            action.sleep(1)
            action.capture_screen(u'关注截图', '/Users/zhangweishun/Desktop/appium-lich-master/screenshot/')

    """
     评论,需要登陆
    """

    def test_comment(self, action: ElementActions):

        action.sleep(1)
        action.click(HomePage.评论按钮)
        action.sleep(1)
        action.click(CommentPage.评论框打开)
        action.text(CommentPage.评论框输入, 'nice')
        action.click(CommentPage.评论发送)
        action.sleep(1)
        assert action.is_text_displayed('nice')





    """进入分享"""




    def test_share(self, action: ElementActions):

        action.click(HomePage.分享按钮)
        action.sleep(1)
        """
        判断是否有文本"share to"
        """
        action.is_text_displayed('Share to')
    def test_otherHomepage(self,action:ElementActions):
        uper = action.get_text(HomePage.作者名称)

        action.click(HomePage.作者头像)
        assert uper == action.get_text(MyPage.名字)


