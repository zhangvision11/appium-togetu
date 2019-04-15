from base.action import ElementActions
from page.pages import *

class Test_Shot():

    def test_Normalshot(self, action: ElementActions):
        action.click(HomePage.拍摄按钮)
        if action.is_text_displayed('Allow Access', is_retry=False):
            action.click(ShotPage.申请权限)
            action.click(ShotPage.获取权限)
            action.click(ShotPage.获取权限)
            action.click(ShotPage.拍摄提示)
        else:pass

        action.click(ShotPage.拍摄按钮)
        action.sleep(15)
        action.click(ShotPage.编辑完成)
       #action.click(ShotPage.上传按钮)

        assert action.is_text_displayed('Post')
    def test_5partshot(self,action:ElementActions):
        action.click(HomePage.拍摄按钮)
        action.click(ShotPage.拍摄按钮)
        action.sleep(3)
        action.click(ShotPage.拍摄按钮)
        action.click(ShotPage.拍摄按钮)
        action.sleep(3)
        action.click(ShotPage.拍摄按钮)
        action.click(ShotPage.拍摄按钮)
        action.sleep(3)
        action.click(ShotPage.拍摄按钮)
        action.click(ShotPage.拍摄按钮)
        action.sleep(3)

        action.click(ShotPage.编辑完成)

        assert action.is_text_displayed('Post')

    def test_Upload(self,action:ElementActions):
        action.click(HomePage.拍摄按钮)
        action.click(ShotPage.上传视频)
        action.sleep(2)
        action.click(ShotPage.选择视频)
        action.click(ShotPage.剪切完成)
        action.click(ShotPage.编辑完成)
        assert action.is_text_displayed('Post')
    def test_pressShot(sel,action:ElementActions):
        action.click(HomePage.拍摄按钮)
        action.click(ShotPage.长按拍摄)
        action.long_press(ShotPage.拍摄按钮, dua=15000)
        action.click(ShotPage.编辑完成)
        assert action.is_text_displayed('Post')
    def test_musicShot(self,action:ElementActions):
        action.click(HomePage.音乐集合页按钮)

        action.click(MusicCgPage.拍摄按钮)
        action.sleep(3)

        assert action.is_text_displayed('Tap to shoot')
        """
    def test_selectMusicShot(self,action:ElementActions):
        action.click(HomePage.拍摄按钮)
        action.click(ShotPage.选择音乐)
        action
        """
    def test_switchShot(self,action:ElementActions):
        """
        翻转摄像头
        :return:
        """
        action.click(HomePage.拍摄按钮)
        action.sleep(1)
        action.capture_screen(u'摄像头', '/Users/zhangweishun/Desktop/appium-lich-master/screenshot/')
        action.click(ShotPage.切换摄像头)
        action.sleep(1)
        action.capture_screen(u'切换摄像头', '/Users/zhangweishun/Desktop/appium-lich-master/screenshot/')
    def test_epicShot(self,action:ElementActions):
        action.click(ShotPage.拍摄速度)
        action.click(ShotPage.极慢)
        action.click(ShotPage.拍摄按钮)
        action.sleep(8)
        assert action.is_element_displayed(ShotPage.编辑完成,is_retry=False)
    def test_slowShot(self,action:ElementActions):
        action.click(HomePage.拍摄按钮)
        action.click(ShotPage.拍摄速度)
        action.click(ShotPage.慢速)
        action.click(ShotPage.拍摄按钮)
        action.sleep(12)
        assert action.is_element_displayed(ShotPage.编辑完成,is_retry=False)

   """ def test_fastShot(self,action:ElementActions):
        action.click(HomePage.拍摄按钮)
        action.click(ShotPage.拍摄速度)
        action.click(ShotPage.快速)
        action.click(ShotPage.拍摄按钮)
        action.sleep(16)
        assert action.is_element_displayed(ShotPage.编辑完成,is_retry=False)
    def test_flashShot(self,action:ElementActions):
        action.click(HomePage.拍摄按钮)
        action.click(ShotPage.拍摄速度)
        action.click(ShotPage.极快)
        action.click(ShotPage.拍摄按钮)
        action.sleep(20)

        assert action.is_element_displayed(ShotPage.编辑完成,is_retry=False)
"""

