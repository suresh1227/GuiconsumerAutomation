#!/usr/bin/python
# Copyright (C) 2017 McAfee, Inc.  All rights reserved.
# TestcaseID: 5
# TestcaseDescription:  Verifying Action Center
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

testcaseDescription = "Verifying Identitiy Tab"

class TestCase():

    def __init__(self):
        pass

    def launch(self,Appbundleid):
        if not commonFns.launchApplication(Appbundleid):
            logging.error("Failed to launch Product")

    def verify(self,Appbundleid):
        commonFns.IdentityVerification(Appbundleid)

    def reporting(self):
        print "Executing %s" % testcaseName, ":" + testcaseDescription

if __name__ == "__main__":
    testcaseobj = TestCase()
    testcaseobj.reporting()
    testcaseobj.launch(constants.Data["bundleid"])
    testcaseobj.verify(constants.Data["bundleid"])
    filename = testcaseDescription + "pass" + strftime("%Y-%m-%d %H:%M:%S", gmtime())
    commonFns.Resultsupdate(constants.Data['testresult'], filename)