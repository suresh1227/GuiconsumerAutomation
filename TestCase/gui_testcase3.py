#!/usr/bin/python
# Copyright (C) 2017 McAfee, Inc.  All rights reserved.
# TestcaseID: 3
# TestcaseDescription:  pc or Mac Verification
#_author: Sureshravuri
import sys
import os
import atomac.ldtp as ldtp
testcaseName = sys.argv[0][:-3]
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import constants
import commonFns
import logging
from time import gmtime, strftime
testcaseDescription = "pc or Mac Verification"

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

    def verify(self,window,refrenceid,objectidentifier,texttoenter):
        commonFns.pcorMacVerification(window,refrenceid,objectidentifier,texttoenter)

    def reporting(self):
        print "Executing %s" % testcaseName, ":" + testcaseDescription

    def quit(self,Appbundleid ):
        commonFns.quitApplication(Appbundleid)

if __name__ == "__main__":
    testcaseobj = TestCase()
    testcaseobj.reporting()
    testcaseobj.launch(constants.Data["bundleid"])
    reference = testcaseobj.appRef(constants.Data["bundleid"])
    window = testcaseobj.appwindow(reference)
    buttons = testcaseobj.appButtons(window)
    commonFns.atomacclick(buttons[8])
    filename = testcaseDescription +  "pass"  + strftime("%Y-%m-%d %H:%M:%S", gmtime())
    commonFns.screenshot(filename)
    testcaseobj.verify(window,reference,constants.Data["icon"], constants.Data["email"])
    filename = testcaseDescription +  "pass"  + strftime("%Y-%m-%d %H:%M:%S", gmtime())
    commonFns.screenshot(filename)
    childwindows = commonFns.getApplicationwindowId(reference)
    protectdevicewindowbuttons = commonFns.getAppButtons(childwindows)
    commonFns.atomacclick(protectdevicewindowbuttons[0])
    ldtp.wait(10)
    newbuttons = commonFns.getAppButtons(childwindows)
    fileupdate = testcaseDescription +  "fail"  + strftime("%Y-%m-%d %H:%M:%S", gmtime())
    if commonFns.atomacclick(newbuttons[0]):
        commonFns.Resultsupdate(constants.Data["testresult"], filename)
    else:
        commonFns.Resultsupdate(constants.Data["testresult"], fileupdate)
    ldtp.wait(5)
    testcaseobj.quit(constants.Data["bundleid"])

