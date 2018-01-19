#!/usr/bin/python
# Copyright (C) 2017 McAfee, Inc.  All rights reserved.
# TestcaseID: 1
# TestcaseDescription:  consumer4.0 application Launching
#__author_:Sureshravuri
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

testcaseDescription = "consumer4.0 application Launching"
filename = testcaseDescription + "pass" + strftime("%Y-%m-%d %H:%M:%S", gmtime())
class TestCase():

    def verify(self,Appbundleid):
        if commonFns.launchApplication(Appbundleid):
            commonFns.Resultsupdate(constants.Data["testresult"], filename)
        else:
            commonFns.Resultsupdate(constants.Data["testresult"], filename)

if __name__ == "__main__":
    testcaseobj = TestCase()
    testcaseobj.verify(constants.Data["bundleid"])
    ldtp.wait(3)
    commonFns.screenshot(filename)
    commonFns.quitApplication(constants.Data["bundleid"])

