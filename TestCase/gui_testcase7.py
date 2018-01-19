#!/usr/bin/python
# Copyright (C) 2017 McAfee, Inc.  All rights reserved.
# TestcaseID: 5
# TestcaseDescription:  contextual help
#__author:Sureshravuri
import sys
import os
import atomac.ldtp as ldtp
testcaseName = sys.argv[0][:-3]
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import constants
import commonFns
import logging
from time import gmtime, strftime

testcaseDescription = "contextual help"

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

    def verify(self,window,Appbuttons):
        commonFns.contextualhelpverificationhome(window,Appbuttons)

    def quit(self,Appbundleid ):
        commonFns.quitApplication(Appbundleid)

    def reporting(self):
        print "Executing %s" % testcaseName, ":" + testcaseDescription

if __name__ == "__main__":
    testcaseobj = TestCase()
    testcaseobj.reporting()
    testcaseobj.launch(constants.Data["bundleid"])
    ref = testcaseobj.appRef(constants.Data["bundleid"])
    window = testcaseobj.appwindow(ref)
    buttons = testcaseobj.appButtons(window)
    testcaseobj.verify(window, buttons[5])
    filename = testcaseDescription + "pass" + strftime("%Y-%m-%d %H:%M:%S", gmtime())
    #commonFns.screenshot(filename)
    if commonFns.atomacclick(buttons[5]):
        commonFns.Resultsupdate(constants.Data["testresult"], filename)
    else:
        filename = testcaseDescription + "fail" + strftime("%Y-%m-%d %H:%M:%S", gmtime())
        commonFns.Resultsupdate(constants.Data["testresult"], filename)
    testcaseobj.quit(constants.Data["bundleid"])