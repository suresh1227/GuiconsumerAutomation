#!/usr/bin/python
# Copyright (C) 2017 McAfee, Inc.  All rights reserved.
# TestcaseID: 0
# TestcaseDescription: this is driver file which will trigger the automation, it will calls gui.sh shell script file to run all the scripts in order.
#__author_: Sureshravuri

import constants
import subprocess
import commonFns
import os
import shutil
from time import gmtime, strftime

if __name__ == "__main__":
    testresultupdatefile = "TestcaseResult.txt"
    if not os.path.isfile(testresultupdatefile):
        open(testresultupdatefile, 'w').close()
    logdir = "/Users/user/Desktop/GuiconsumerAutomation/logging"
    os.chdir(logdir)
    filename = "logfile.log"
    if  not os.path.exists(filename):
        open(filename, 'w').close()
    os.chdir('/Users/user/Desktop/GuiconsumerAutomation/')
    _installflag = constants.Data.get('installbuild-flag')
    if _installflag == 0:
        print "INSTALLING NEW CONSUMER4.1 BUILD FROM QA SERVER"
        subprocess.call(['./gui.sh'])
        commonFns.archive(constants.Data.get('sourcepath'),constants.Data.get('foldername'))

        # call 26th python file or integrate code here only
        # build will taken from QA and uninstall old build and install new build then Running scripts
        # As of now uninstalling old build and taking seril key from server has been completed
    else:
        _filepath = commonFns.filepath(constants.Data.get('xmlfilepath'))
        _buildinstalled = commonFns.xmlparsing(_filepath,constants.Data["buildnumber"])
        print ("CONSUMER 4.1 GUI AUTOMATION STARTED FOR %s" %_buildinstalled)
        subprocess.call(['./gui.sh'])
        commonFns.archive(constants.Data.get('sourcepath'),constants.Data.get('foldername'))
