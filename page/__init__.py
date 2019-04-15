# -*- coding: utf-8 -*-
from utils.shell import Shell
from utils.shell import ADB
appium_v = Shell.invoke('appium -v')
print(appium_v)