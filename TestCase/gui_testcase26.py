#!/usr/bin/python
# Copyright (C) 2017 McAfee, Inc.  All rights reserved.
# TestcaseID: 5
# TestcaseDescription:  Verifying deep Device
#__author: Sureshravuri

import sys
import os
import atomac.ldtp as ldtp
testcaseName = sys.argv[0][:-3]
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import constants
import commonFns
import logging
from time import gmtime, strftime

testcaseDescription = "Verifying on day expiry"

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

    def verify(self,bundleid,preexpirycommand,Appbuttons,window,resettimeanddate):
        commonFns.quitApplication(bundleid)
        print "product quit"
        commonFns.executeCommand(preexpirycommand)
        print  "PreExpiry"
        ldtp.wait(80)
        commonFns.launchApplication(bundleid)
        print "Launching"
        ldtp.wait(10)
        commonFns.atomacclick(Appbuttons[7])
        ldtp.wait(10)
        device_status = commonFns.devicesSatusVerification(window)
        print "Device status"
        ldtp.wait(1)
        return device_status
        commonFns.executeCommand(timeanddatereset)
    def reporting(self):
        print "Executing %s" % testcaseName, ":" + testcaseDescription

    def quit(self, Appbundleid):
        commonFns.quitApplication(Appbundleid)

if __name__ == "__main__":
    testcaseobj = TestCase()
    testcaseobj.reporting()
    ref = testcaseobj.appRef(constants.Data["bundleid"])
    window = testcaseobj.appwindow(ref)
    buttons = testcaseobj.appButtons(window)
    device_status = testcaseobj.verify(constants.Data["bundleid"],constants.Data["ondayexpiry"],buttons,window,constants.Data["timeanddatereset"])
    values = str(device_status)
    if "Expires" or  "soon" in values.split:
        print "Subscription is going to Expire"
        #writing to results file
    else:
        print "Not able find the status"
    commonFns.atomacclick(buttons[0])
    # implement clicking in all the places of Run a scan, updates, Help and verify warning message in all 3 modules
    testcaseobj.verify(buttons, window)
    filename = testcaseDescription + "pass" + strftime("%Y-%m-%d %H:%M:%S", gmtime())
    commonFns.Resultsupdate(constants.Data['testresult'], filename)
    testcaseobj.quit(constants.Data["bundleid"])