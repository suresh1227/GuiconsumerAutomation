#!/usr/bin/python
# Copyright (C) 2017 McAfee, Inc.  All rights reserved.
# TestcaseID: 5
# TestcaseDescription:  Verifying deep Device
#__author:Sureshravuri
import sys
import os
import atomac.ldtp as ldtp
testcaseName = sys.argv[0][:-3]
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import constants
import commonFns
import logging
import time
from time import gmtime, strftime
testcaseDescription = "Verifying deep Device"

class TestCase():

    def __init__(self):
        pass

    def launch(self,Appbundleid):
        if not commonFns.launchApplication(Appbundleid):
            logging.error("Failed to launch Product")

    def appRef(self,Appbundleid):
        try:
            reference = commonFns.getApplicationReferenceID(Appbundleid)
        except Exception as er:
            return  False
        return reference

    def appwindow(self,reference):
        try:
            window = commonFns.getApplicationwindowId(reference)
        except Exception as er:
            return  False
        return window
    def appButtons(self,window):
        try:
            AppButtons = commonFns.getAppButtons(window)
        except Exception as er:
            return  False
        return AppButtons

    def verify(self,window,ReferenceID):
        commonFns.deepDevice(window,ReferenceID)

    def reporting(self):
        print "Executing %s" % testcaseName, ":" + testcaseDescription

    def quit(self,Appbundleid ):
        commonFns.quitApplication(Appbundleid)

if __name__ == "__main__":
    testcaseobj = TestCase()
    testcaseobj.reporting()
    testcaseobj.launch(constants.Data["bundleid"])
    ref = testcaseobj.appRef(constants.Data["bundleid"])
    window = testcaseobj.appwindow(ref)
    buttons = testcaseobj.appButtons(window)
    commonFns.atomacclick(buttons[0])
    testcaseobj.verify(window,ref)
    deep_device = commonFns.deepDevice(window, ref)
    ldtp.wait(5)
    filename = testcaseDescription + "pass" + strftime("%Y-%m-%d %H:%M:%S", gmtime())
    commonFns.screenshot(filename)
    deep_device_all_objects = commonFns.getAllObjects(deep_device)
    deep_deivce_buttons = commonFns.getAppButtons(deep_device)
    commonFns.atomacclick(deep_deivce_buttons[2])
    ldtp.wait(5)
    commonFns.screenshot(filename)
    if commonFns.atomacclick(deep_deivce_buttons[3]):
        commonFns.screenshot(filename)
        commonFns.Resultsupdate(constants.Data['testresult'], filename)
        ldtp.wait(5)
    else:
        commonFns.Resultsupdate(constants.Data['testresult'], filename)
        testcaseobj.quit(constants.Data["bundleid"])