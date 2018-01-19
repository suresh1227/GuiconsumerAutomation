#!/usr/bin/python
# Copyright (C) 2017 McAfee, Inc.  All rights reserved.
# TestcaseID: 0
# TestcaseDescription:  All common functions are written in this fle, all the independnet script files will use this file
#__author_: Sureshravuri
import re
import os
import os.path
import atomac
import logging
import xml.etree.ElementTree as ET
import time
import subprocess
import atomac.ldtp as ldtp
import commands
from subprocess import Popen, PIPE
from subprocess import call
from time import gmtime, strftime
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
timeout = 15
logFileMode='w'
logFormat = '%(asctime)s %(levelname)-8s %(message)s'
logDateFmt='%d %b %H:%M:%S'
logfile = '/Users/user/Desktop/GuiconsumerAutomation/logging/logfile.log'
logLevel = logging.INFO
logging.basicConfig(level=logLevel, format=logFormat, datefmt=logDateFmt, filename=logfile, filemode=logFileMode)

def launchApplication(Cbundleid):
    """
        Launches the Application
        RETURN : True on success. False Otherwise.
        """
    try:
        atomac.launchAppByBundleId(Cbundleid)
        ldtp.wait(3)
    except Exception as er:
        logging.info('Not able to launch Application, Please check Application added in Accessbility')
        return False
def getApplicationReferenceID(Cbundleid):
    """
        gets Application reference ID by bundleid
        RETURN : True on success. False Otherwise.
        """
    try:
        ReferenceID = atomac.getAppRefByBundleId(Cbundleid)
        #print ("ReferenceID of the Application : %s" % ReferenceID)
        logging.info("Application RefferenceID : %s" % ReferenceID)
    except Exception as er:
        logging.info('Not able to get Application ReferenceID')
        return False
    return ReferenceID

def getAppRefByPidofapp(processid):
    """
        gets Application reference ID by process id
        RETURN : True on success. False Otherwise.
        """
    try:
        _pidreference = atomac.getAppRefByPid(processid)
        logging.info("Application RefferenceID : %s" % _pidreference)
    except Exception as er:
        logging.info('Not able to get Application ReferenceID')
        return False
    return _pidreference
def getApplicationwindowId(ReferenceID):
    """
       gets Application window ID
        RETURN : True on success. False Otherwise.
        """
    try:
        ldtp.wait(5)
        window = ReferenceID.windows()[0]
        logging.info("Application id of the window : %s" % window)
    except Exception as er:
        logging.info('Not able to get window name  of Application')
        return False
    return window

def getChildwindows(ReferenceID):
    """
        gets Application chwild windows
        RETURN : True on success. False Otherwise.
        """
    try:
        ldtp.wait(3)
        window = ReferenceID.windowsR()[0]
        logging.info("child windows : %s" % window)
    except Exception as er:
        logging.info('Not able to get child windows')
        return False
    return window

def getApplicatontitle(window):
    """
        gets objects Title
        RETURN : True on success. False Otherwise.
        """
    try:
        title = window.AXTitle
        logging.info("Titile is : %s" % title)
    except Exception as er:
        logging.info('Not able to get  Title')
        return False
    return title

def getAppButtons(window):
    """
        gets current window buttons
        RETURN : True on success. False Otherwise.
        """
    try:
        AppButtons = window.buttonsR()
        logging.info("Button got from the current screen of the Application: %s" % AppButtons)
    except Exception as er:
         print("Not able to get the application buttons, please check getApplicationwindowId")
         return False
    return AppButtons
def getAllObjects(window):
    """
        gets Application all objects
        RETURN : True on success. False Otherwise.
        """
    try:
        AppButtons = window.findAllR()
        logging.info("All objects: %s" % AppButtons)
    except Exception as er:
        return False
        print("not able to get All objects")
    return AppButtons
def getMenubuttons(allbuttons):
    """
        gets Application Menu objects
        RETURN : True on success. False Otherwise.
        """
    try:
        menubuttons = allbuttons[0:3]
        actualbuttons = []
        for words in menubuttons:
            actualbuttons.append(str(words).split("\'")[1])
        logging.info("Menu buttons of the application: %s" % actualbuttons)
    except Exception as er:
        print("Not able to get Menu buttons")
    return False
    return actualbuttons

def clickonbutton(titleobj, buttontoclick):
    """
        Click on object using ldtp  method
        RETURN : True on success. False Otherwise.
        """
    try:
        ldtp.click(titleobj,buttontoclick)
        logging.info("Clicked on : %s" % buttontoclick)
    except Exception as er:
        print ("Not able to click on button")
def atomacclick(objecttoclick):
    """
        Click on object using atomac  method
        RETURN : True on success. False Otherwise.
        """
    try:
        objecttoclick.Press()
        #print "clicked on : %s" %objecttoclick
    except Exception as er:
        print "Not able to click on: %s" %objecttoclick
def fileRenameandReplace(filename,newfilename):
    """
        find and replace in json fileame
        RETURN : True on success. False Otherwise.
        """
    try:
        os.rename(filename,newfilename)
        logging.info("Json file renamed in PD path")
    except Exception as er:
        print ("Not able to rename the json file ")
    return False

def killprocess(ReferenceID):
    '''os.system("ps -eaf|grep -i 'Mcafee'|grep -v grep|awk '{print $2}'|xargs kill")
    date 1102122317'''
    pass
def xmlparsing(xmlpath, valuetoget):
    """
        Gets build number from ProductConfig.xml file"
        RETURN : True on success. False Otherwise.
        """
    try:
        _Handle = ET.parse(xmlpath)
        rootelement = _Handle.getroot()
        number = rootelement[valuetoget].text
        return number
        #return _Handle
    except Exception as er:
        print "Not able to Read /usr/local/McAfee/ProductConfig.xml file"

def getpid(command):
    """
        This is general function uses "pidof" binary and returns the process id
        RETURN : True on success. False Otherwise.
        """
    try:
        _pidof = executeCommand(command)
    except Exception as er:
        print (" not able to get pid")
        return False
    return _pidof
'''def getMcafeedmgfilename(dmgpath, dmgfilename):
    """
        to get the Mcafee dmo filename
        RETURN : True on success. False Otherwise.
        """
    try:
        for root, dirs, files in os.walk(dmgpath):
            for dmg in files:
                if dmg.endswith(dmgfilename) in dmgpath:
                    dmginstallername = dmgfilename
                else:
                    # call download build function and return the dmg
    except Exception as er:
        logging.DEBUG("dmg")
    return False
    return dmginstallername'''
def clickondownload():
    pass
def productUninstall(command):
    """
        to uninstall the current product
        RETURN : True on success. False Otherwise.
        """
    try:
        Executingbysubprocess(command)
        print "uninstallcommand". command
    except Exception as er:
        print "Not able to uninstall the product"
def convertlisttostring(listtostrip):
    """
        converting list to string
        RETURN : True on success. False Otherwise.
        """
    try:
        newlist = []
        newlist = listtostrip
        findobjectnames = str(newlist).replace("\\", "")
    except Exception as er:
        print "not able to strip list"
    return False
    return findobjectnames

def getInstallerbuttons(pidofmasterinstaller):
    """
        Gets the current installer buttons
        RETURN : True on success. False Otherwise.
        """
    dmgwindow = atomac.getAppRefByPid(pidofmasterinstaller)
    Masterinstallerbuttons = getAppButtons(dmgwindow)
    return Masterinstallerbuttons

def handleInstallerinterrruptions(window,texttosearch,fileexist):
    """
        Handles interrruptions in installer and handles
        RETURN : True on success. False Otherwise.
        """
    pass
def getserialkey():
    #getserial key function
    #return the serial key
    pass

def installbuild():
    #getMcafeedmgfilename() and call the uninstall command
    #Allobjects = window.findAllR()
    #text = window.textFields()
    #text[0].Confirm()
    #textname = text[0].AXRoleDescription
    #window.Activate()
    #ldtp.inserttext(title,textname,"675.0, 370.0","G88ADBH8NZBTLJQ")
    #AppButtons = window.buttonsR
    #AppButtons[1].Press()
    #AppButtons = window.buttonsR
    #Read the text and get the buttons and close the installerwindow
    pass

def entertext(Title,objectname,stringtoenter):
    """
        To enter text into specified object
        RETURN : True on success. False Otherwise.
        """
    try:
        ldtp.enterstring(Title,objectname,stringtoenter)
        logging.DEBUG("entered string")
    except Exception as er:
        logging.DEBUG("Not able to enter the string in %")

def readTextFields(window):
    """
        Reading text file
        RETURN : True on success. False Otherwise.
        """
    try:
        textlist = []
        textlist = window.textFields()
        logging.DEBUG("textfields in current window")
    except Exception as er:
        logging.DEBUG("Not able to get textfields in current window")
    return False
    return textlist

def readStaticText(window):
    """
        Reads the static text in the crrrent window and returns
        RETURN : True on success. False Otherwise.
        """
    try:
        staticobjectsofwindow = window.staticTextsR()
        #statictexxt = convertlisttostring(staticobjectsofwindow)
        logging.DEBUG("Statictext in the current window")
    except Exception as er:
        logging.DEBUG("Not able to read the static text")
    return False
    return staticobjectsofwindow
    #print staticobjectsofwindow

def pdValidation():
    """
        For PDValidaton
        RETURN : True on success. False Otherwise.
        """
    pass

def rtsobjects():
    """
        Function to interact with rts window
        RETURN : True on success. False Otherwise.
        """
    pass

def Firewallobjects():
    """
        Function to interact with Firewall window
        RETURN : True on success. False Otherwise.
        """
    pass

def Automaticupdatesobjects():
    """
        Function to interact with Automatic updates
        RETURN : True on success. False Otherwise.
        """
    pass

def scheduledscansobjects():
    """
        Function to interact scheduled objects
        RETURN : True on success. False Otherwise.
        """
    pass

def MacSecurityrunascan(window,referenceid):
    """starts full scan in MacSecurityrunascan
        RETURN : True on success. False Otherwise"""
    try:
        allobjects = getAllObjects(window)
        atomacclick(allobjects[52])
        ldtp.wait(2)
        Runwindow = getChildwindows(referenceid)
        buttons = getAppButtons(Runwindow)
        atomacclick(buttons[0])
    except Exception as er:
        return False
def MacSecurityCustomScan(window,referenceid):
    """
        starts Custome scan in MacSecurityrunascan
        RETURN : True on success. False Otherwise.
        """
    try:
        allobjects = getAllObjects(window)
        atomacclick(allobjects[52])
        ldtp.wait(2)
        Runwindow = getChildwindows(referenceid)
        buttons = getAppButtons(Runwindow)
        atomacclick(buttons[0])
    except Exception as er:
        print "Not able to click on MacSecurityCustomScan"
    return False
def MacSecurityqurantine(window,refrenceid):
    """ Click on Qurantine window and goes to next page in Qurantine
        RETURN : True on success. False Otherwise"""
    try:
            appbuttons = getAppButtons(window)
            atomacclick(appbuttons[1])
            time.sleep(5)
            appbuttonsnew = getAppButtons(window)
            print appbuttonsnew[17]
            time.sleep(5)
            atomacclick(appbuttonsnew[17])
            Quarantine_window = getChildwindows(refrenceid)
            Quarantine_window_buttons = getAppButtons(Quarantine_window)
            print "Quarantine_window_buttons", Quarantine_window_buttons
            time.sleep(3)
            atomacclick(Quarantine_window_buttons[0])
            time.sleep(3)
            '''atomacclick(Quarantine_window_buttons[1])
            time.sleep(3)
            atomacclick(Quarantine_window_buttons[5])
            time.sleep(3)
            atomacclick(Quarantine_window_buttons[6])'''
    except Exception as er:
            print "Not able to click on MacSecurityqurantine"
    return False
def MacSecurityhistory(window,refrenceid):
    """
        Click on MacSecurityhistory window and goes to next page in Qurantine
        RETURN : True on success. False Otherwise.
        """
    try:
        appbuttons = getAppButtons(window)
        atomacclick(appbuttons[1])
        time.sleep(5)
        appbuttonsnew = getAppButtons(window)
        atomacclick(appbuttonsnew[18])
        History_window = getChildwindows(refrenceid)
        History_window_buttons = getAppButtons(History_window)
        atomacclick(History_window_buttons[1])
        ldtp.wait(3)
        atomacclick(History_window_buttons[2])
        ldtp.wait(3)
        atomacclick(History_window_buttons[3])
        ldtp.wait(3)
    except Exception as er:
        print "Not able to click on MacSecurityhistory"
    return False
def eichertest():
    """
        Writes the eicher test
        RETURN : True on success. False Otherwise.
        """
    try:
        eicher = ('echo ZQZXJVBVT >> mcafee1.txt', 'echo ZQZXJVBVT >> mcafee2.txt','echo ZQZXJVBVT >> mcafee2.txt')
        for test in eicher:
         executeCommand(test)
    except Exception as er:
        print "Not able to do install check"
    return False
def Accountmyaccount():
    """
        Verifies MyAccount tab
        RETURN : True on success. False Otherwise.
        """
    pass

def AccountInformation(referenceid,window):
    """
        Cilcks on Account gets te text and can verify
        RETURN : True on success. False Otherwise.
        """
    try:
        content = []
        appbuttons = getAppButtons(window)
        atomacclick(appbuttons[3])
        appbuttons = getAppButtons(window)
        time.sleep(5)
        atomacclick(appbuttons[10])
        childwindow = getChildwindows(referenceid)
        staticobjects = childwindow.staticTextsR()
        time.sleep(5)
        for i in staticobjects:
            content.append(i.AXValue)
    except Exception as er:
        return False
    return content
def About(referenceid,window):
    """
        Cilcks on About dailog box and gets te text and can verify
        RETURN : True on success. False Otherwise.
        """
    try:
        content = []
        appbuttons = getAppButtons(window)
        atomacclick(appbuttons[2])
        newappbuttons = getAppButtons(window)
        time.sleep(5)
        atomacclick(newappbuttons[11])
        childwindow = getChildwindows(referenceid)
        staticobjects = childwindow.staticTextsR()
        time.sleep(5)
        for i in staticobjects:
            content.append(i.AXValue)
    except Exception as er:
        return False
    return content
def Daysleftverification():
    """
        gets days left for verifications
        RETURN : True on success. False Otherwise.
        """
    pass

def verifysubscriptionstatusinaccounttab():
    """
        Verify subscription status in accounttab
        RETURN : True on success. False Otherwise.
        """
    pass
def verifysubscriptioninhomedevicestatus(sub):
    """
        Verify subscription status in verify subscription in home devices tatus
        RETURN : True on success. False Otherwise.
        """
    try:
        if "Subscription Active" in sub:
            print " Hi chetan You have Active subscription"
        else:
            print " your subscription is not active "
    except Exception as er:
        print("not able to get subscription details")
        return False
def homerunascan(window,referenceid):
    """
        Clicks on run scan in home tab
        RETURN : True on success. False Otherwise.
    """
    try:
        allbuttons = getAppButtons(window)
        print allbuttons
        atomacclick(allbuttons[0])
        atomacclick(allbuttons[20])
        time.sleep(4)
        Runwindow = getChildwindows(referenceid)
        buttons = getAppButtons(Runwindow)
        atomacclick(buttons[0])
        newb = getAllObjects(Runwindow)
        time.sleep(3)
        atomacclick(newb[2])
    except Exception as er:
        print("Not able to click on homerunascan")
        return False
def homeCustomScan(window,referenceid):
    """
        Clicks on run custom scan in home tab
        RETURN : True on success. False Otherwise.
        """
    try:
        allbuttons = getAppButtons(window)
        atomacclick(allbuttons[0])
        atomacclick(allbuttons[19])
        time.sleep(5)
        Runwindow = getChildwindows(referenceid)
        buttons = getAppButtons(Runwindow)
        atomacclick(buttons[1])
        newb = getAllObjects(Runwindow)
        time.sleep(4)
        atomacclick(newb[2])
    except Exception as er:
        print("Not able to click on HomeCustomScan")
        return False
def homeupdates(window, referenceid):
    """
        Clicks on updates in home tab
        RETURN : True on success. False Otherwise.
        """
    try:
        allobjects = getAllObjects(window)
        atomacclick(allobjects[52])
        ldtp.wait(2)
        Runwindow = getChildwindows(referenceid)
        buttons = getAppButtons(Runwindow)
        print "buttons", buttons
        atomacclick(buttons[0])
        buttons = getAppButtons(Runwindow)
        ldtp.wait(4)
    except Exception as er:
        return False
def verifynotification(notificationbutton):
    """
        Verifies Notification option
        RETURN : True on success. False Otherwise.
        """
    try:
        atomacclick(notificationbutton)
        ldtp.wait(3)
        content = notificationbutton.AXTitle
        ldtp.wait(1)
    except Exception as er:
        logging.DEBUG("Not able to click on notification object")
        return False
    return content
def contextualhelpverificationhome(window,contextualhelpbutton):
    """
        Verifies contextual help verification home option
        RETURN : True on success. False Otherwise.
        """
    try:
        testcaseDescription = "contextual help"
        filename = testcaseDescription + "fail" + strftime("%Y-%m-%d %H:%M:%S", gmtime())
        atomacclick(contextualhelpbutton)
        appbuttons = getAppButtons(window)
        for i in range(1,5):
            time.sleep(3)
            screenshot(filename)
            atomacclick(appbuttons[26])
            time.sleep(3)
        atomacclick(appbuttons[26])
    except Exception as er:
        return False
        print "Not able to click on contextualhelpverification"
def globalsettings(golbalsettingbutton):
    """
         Verifies global settins home option
        RETURN : True on success. False Otherwise.
        """
    try:
        atomacclick(golbalsettingbutton)
        global_settings_content = getApplicatontitle(golbalsettingbutton)
    except Exception as er:
        print "Not able to get globalsettings_content"
        return False
    return global_settings_content
def deepDevice(window,ReferenceID):
    """
         Verifies deepDevice
        RETURN : True on success. False Otherwise.
        """
    try:
        allobjects = window.findAllR()
        ldtp.wait(9)
        atomacclick(allobjects[30])
        child = getChildwindows(ReferenceID)
        #print "allobjects", child.findAllR()
    except Exception as er:
        print "Not able to click on deepDevice"
        return False
    return child
def rtsOn():
    """
        Disables network scanning for OAS
        RETURN : True on success. False Otherwise.
        """
    pass

def rtsOff():
    """
        Disables network scanning for OAS
        RETURN : True on success. False Otherwise.
        """
    pass

def firewallOff():
    """
        Disables network scanning for OAS
        RETURN : True on success. False Otherwise.
        """
    pass

def friewallOn():
    """
        Disables network scanning for OAS
        RETURN : True on success. False Otherwise.
        """
    pass

def verifyActionCenterFirewall():
    """
        Disables network scanning for OAS
        RETURN : True on success. False Otherwise.
        """
    pass

def verifyActionCenterRts():
    """
        Disables network scanning for OAS
        RETURN : True on success. False Otherwise.
        """
    pass

def devicesSatusVerification(windowname):
    """
        Disables network scanning for OAS
        RETURN : True on success. False Otherwise.
        """
    try:
        AppButtons = getAppButtons(windowname)
        DeviceStatus = AppButtons[10:14]
        DeviceStatus_Descriptions = []
        for device in DeviceStatus:
            Descriptionsofsettings = getApplicatontitle(device)
            DeviceStatus_Descriptions.append(Descriptionsofsettings)
    except Exception as er:
        return False
    return DeviceStatus_Descriptions
def ReporterReference(pidofreporter):
    """
        Disables network scanning for OAS
        RETURN : True on success. False Otherwise.
        """
    try:
        pid_list = []
        Mcafee_Reporter_pid = getpid(pidofreporter)
        print "Now",Mcafee_Reporter_pid
        listofpid = list(Mcafee_Reporter_pid)
        pid_list.append(listofpid[1])
        split_pids_by_space = [words for segments in pid_list for words in segments.split()]
        print "split_pids_by_space", split_pids_by_space
        reporter_current_pid = int(''.join(map(str,split_pids_by_space[1])))
        print "reporter_current_pid", reporter_current_pid
        Mcafee_Reporter_Reference = getAppRefByPidofapp(reporter_current_pid)
        #print "Mcafee_Reporter_Reference", Mcafee_Reporter_Reference
    except Exception as er:
        return False
        print "Not able to get Reporter details"
        print Mcafee_Reporter_Reference
    return Mcafee_Reporter_Reference
def ReporterParsing(refrenceid):
    """
        Disables network scanning for OAS
        RETURN : True on success. False Otherwise.
        """
    try:
        Mcafee_Reporter_window = getApplicationwindowId(refrenceid)
        Mcafee_Reporter_window.activate()
        Mcafee_Reporter_buttons = getAppButtons(Mcafee_Reporter_window)
        #print Mcafee_Reporter_buttons
        Mcafee_Reporter_all_objects = getAllObjects(Mcafee_Reporter_window)
        atomacclick(Mcafee_Reporter_all_objects[7])
        #print "Mcafee_Reporter_all_objects", Mcafee_Reporter_all_objects
        table_object = Mcafee_Reporter_all_objects[18]
        table_rows = table_object.AXRows
        ldtp.wait(10)
        atomacclick(Mcafee_Reporter_all_objects[50])
    except Exception as er:
        return False
        print "Not able to Parse Reporter window"
    return table_rows
def protectMoreDevices(button):
    """
        Disables network scanning for OAS
        RETURN : True on success. False Otherwise.
        """
    try:
        atomacclick(button)
    except Exception as er:
        return False
        print "Not able to click on protectMoreDevices button"
def pcorMacVerification(window,refrenceid,objectidentifier,texttoenter):
    """
        Disables network scanning for OAS
        RETURN : True on success. False Otherwise.
        """
    try:
        buttons = getAppButtons(window)
        atomacclick(buttons[9])
        childwindow = refrenceid.windowsR()
        protectMoreDevicestitle = getApplicatontitle(childwindow[0])
        entertext(protectMoreDevicestitle,objectidentifier,texttoenter)
    except Exception as er:
        return False
        print "Not able to able to send mail"
def sendsms(window,refrenceid,image,email):
    """
        Disables network scanning for OAS
        RETURN : True on success. False Otherwise.
        """
    try:
        buttons = getAppButtons(window)
        atomacclick(buttons[10])
        childwindow = refrenceid.windowsR()
        protectMoreDevicesbuttons = getAppButtons(childwindow[0])
        protectMoreDevicestitle = childwindow[0].getApplicatontitle()
        ldtp.enterstring(protectMoreDevicestitle,image,email)
        #Need to write after click
    except Exception as er:
        return False
        print "Not able to send SMS"

def turnOnFirewallFromActioncenter():
    """
        Disables network scanning for OAS
        RETURN : True on success. False Otherwise.
        """
    pass

def turnOnRtsfromActioncenter():
    """
        Disables network scanning for OAS
        RETURN : True on success. False Otherwise.
        """
    pass

def productactivate():
    """
        Disables network scanning for OAS
        RETURN : True on success. False Otherwise.
        """
    pass

def mac_security_tab_status(refrenceid):
    """
        Disables network scanning for OAS
        RETURN : True on success. False Otherwise.
        """
    try:
        AppButtons = getAllObjects(refrenceid)
        DeviceStatus = AppButtons[25:29]
        Descriptions = []
        for device in DeviceStatus:
            Descriptionsofsettings = getApplicatontitle(device)
            Descriptions.append(Descriptionsofsettings)
    except Exception as er:
        return False
    return Descriptions
def Help(window, referenceid):
    """
        Clicks on updates in home tab
        RETURN : True on success. False Otherwise.
        """
    try:
        allobjects = getAllObjects(window)
        atomacclick(allobjects[53])
        ldtp.wait(2)
        Runwindow = getChildwindows(referenceid)
        buttons = getAppButtons(Runwindow)
        atomacclick(buttons[0])
        buttons = getAppButtons(Runwindow)
        ldtp.wait(4)
    except Exception as er:
        return False
def executeCommand(commandtoexecute):
    """
        Disables network scanning for OAS
        RETURN : True on success. False Otherwise.
        """
    try:
        _output = commands.getstatusoutput(commandtoexecute)
    except Exception as er:
        print "not able to execute command"
        return False
    return _output
def Executingbysubprocess(command):
    """
        Disables network scanning for OAS
        RETURN : True on success. False Otherwise.
        """
    result = subprocess.Popen(command, shell=True, stdout=PIPE).stdout
    output = result.read()
    print output

def statusupdate(filepath):
    """
        Disables network scanning for OAS
        RETURN : True on success. False Otherwise.
        """
    pass
def Resultsupdate(filepath,filecontents):
    """
        Disables network scanning for OAS
        RETURN : True on success. False Otherwise.
        """
    try:
        with open(filepath, 'a') as f:
            file_handler = f.writelines(filecontents + '\n')
    except Exception as er:
        return False
    return file_handler
def screenshot(filename):
    """
        Disables network scanning for OAS
        RETURN : True on success. False Otherwise.
        """
    call(["screencapture", "Screenshot for" + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + filename +".jpg"])
def filepath(file):
    try:
        if os.path.isfile(file):
            logging.info("file exists")
        else:
            logging.info("Not exist")
    except Exception as er:
        return False
    return file


def quitApplication(Bundleid):
    """
        Disables network scanning for OAS
        RETURN : True on success. False Otherwise.
        """
    atomac.terminateAppByBundleId(Bundleid)
def archive(sourcepath,dir):
    directoryname = dir + strftime("%Y-%m-%d %H:%M:%S", gmtime())
    archivefilename = directoryname
    if not os.path.exists(directoryname):
        os.makedirs(directoryname)
    files = os.listdir(sourcepath)
    for f in files:
        if f.startswith("Screen"):
            shutil.move(os.path.join(sourcepath, f), os.path.join(directoryname, f))
    shutil.make_archive(archivefilename, 'zip', directoryname)
def IdentityVerification(Cbundleid):
    try:
        Referencevalue = getApplicationReferenceID(Cbundleid)
        window = getApplicationwindowId(Referencevalue)
        AppButtons = getAppButtons(window)
        atomacclick(AppButtons[2])
        newbuttons = getAppButtons(window)
        atomacclick(newbuttons[7])
        childwindow = getChildwindows(Referencevalue)
        allobjects = getAllObjects(childwindow)
    except Exception as er:
        return False
    return childwindow

