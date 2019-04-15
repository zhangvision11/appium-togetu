# -*- coding: utf-8 -*-
__author__ = 'Mio4kon'
from page import tools

pages = tools.parse()


def get_locater(clazz_name, method_name):
    locators = pages[clazz_name]['locators']
    for locator in locators:
        if locator['name'] == method_name:
            return locator


class HomePage:
    点赞按钮 = get_locater('HomePage', '点赞按钮')
    点赞数 = get_locater('HomePage','点赞数')
    点赞动画 = get_locater('HomePage','点赞动画')
    我的 = get_locater('HomePage','我的')
    登陆按钮 = get_locater('HomePage','登陆按钮')
    关注按钮 = get_locater('HomePage','关注按钮')
    下载按钮 = get_locater('HomePage','下载按钮')
    下载数 = get_locater('HomePage','下载数')
    评论按钮 = get_locater('HomePage','评论按钮')
    音乐集合页按钮 = get_locater('HomePage','音乐集合页按钮')
    作者名称 = get_locater('HomePage','作者名称')
    分享按钮 = get_locater('HomePage','分享按钮')
    滑动提示蒙层 = get_locater('HomePage','滑动提示蒙层')
    拍摄按钮 = get_locater('HomePage','拍摄按钮')
    作者头像 = get_locater('HomePage','作者头像')
    
class LoginPage:
    手机号 = get_locater('LoginPage', '手机号')
    获取验证码 = get_locater('LoginPage', '获取验证码')
    密码 = get_locater('LoginPage', '验证码')
    登陆 = get_locater('LoginPage','登录')


class MyPage:
    名字 = get_locater('MyPage','名字')
    like数 = get_locater('MyPage','like数')
    follow数 = get_locater('MyPage', 'follow数')
    fans数 = get_locater('MyPage', 'fans数')
    设置 =get_locater('MyPage', '设置')


class CommentPage:
    评论框打开 = get_locater('CommentPage', '评论框打开')
    评论框输入 = get_locater('CommentPage', '评论框输入')
    评论发送 = get_locater('CommentPage', '评论发送')

class MusicCgPage:
    音乐名称 =  get_locater('MusicCgPage','音乐名称')
    返回按钮 = get_locater('MusicCgPage','返回按钮')
    拍摄按钮 = get_locater('MusicCgPage', '拍摄按钮')


class ShotPage:
    申请权限 = get_locater('ShotPage','申请权限')
    获取权限 = get_locater('ShotPage','获取权限')
    拍摄按钮 = get_locater('ShotPage','拍摄按钮')
    拍摄提示 = get_locater('ShotPage', '拍摄提示')
    魔法表情 = get_locater('ShotPage', '魔法表情')
    上传视频 = get_locater('ShotPage', '上传视频')
    选择视频 = get_locater('ShotPage', '第一个视频')
    剪切完成 = get_locater('ShotPage', '剪切完成')
    切换摄像头 = get_locater('ShotPage', '切换摄像头')
    拍摄速度 = get_locater('ShotPage', '拍摄速度')
    滤镜 = get_locater('ShotPage', '滤镜')
    美颜 = get_locater('ShotPage', '拍摄提示')
    长按拍摄 = get_locater('ShotPage', '长按拍摄')
    编辑完成 = get_locater('ShotPage','编辑完成')
    选取封面 = get_locater('ShotPage','选取封面完成')
    上传按钮 = get_locater('ShotPage','上传按钮')
    选择音乐 = get_locater('ShotPage','选择音乐')
    极慢=get_locater('ShotPage','epic')
    慢速 = get_locater('ShotPage','slow')
    快速 = get_locater('ShotPage','fast')
    极快 = get_locater('ShotPage','flash')
class SettingPage:
    登出 = get_locater('SettingPage','登出')
    手机号 = get_locater('SettingPage','手机号')
    个人资料 = get_locater('SettingPage', '个人资料')
    语言 = get_locater('SettingPage', '语言')
    通知设置 = get_locater('SettingPage', '通知设置')
    投诉建议 = get_locater('SettingPage', 'feed & back')
    确定 = get_locater('SettingPage', '确定')



