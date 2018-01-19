#!/usr/bin/python
# Copyright (C) 2017 McAfee, Inc.  All rights reserved.
# TestcaseID: 0
# TestcaseDescription: All the script files will takes data from this file.
#__author_: Sureshravuri


Data = {'bundleid' :'com.mcafee.console'
      ,'uninstallerbundlepath':'com.mcafee.Uninstaller'
      ,'continuebutton':'Continue'
      ,'Expectedbuild':'9809'
      ,'chromedriverpath':'/Users/suresh/Desktop/guiproject/chromedriver'
      ,'uninstallproduct':'/usr/local/McAfee/uninstallMSC'
	  ,'Mcafeelogfilepath':'/var/log/MasterInstaller.log'
      ,'xmlfilepath':'/usr/local/McAfee/ProductConfig.xml'
      ,'dmgpath': '/Users/sravuri/Downloads/'
      ,'mcafeedmg':'McAfee-MacInstaller-3.3.dmg'
      ,'Rbutton':'Removeit'
      ,'nextbutton':'Next'
      ,'donebutton':'Done'
      ,'attach': 'hdiutil attach  /Users/sravuri/Downloads/McAfee-MacInstaller-3.3.dmg'
      ,'install': '/Volumes/McAfeeMacInstaller/McAfeeMacInstaller.app/Contents/MacOS/McAfeeMacInstaller -install'
      ,'buildnumber':3
      ,'applogin':'loginwindow'
      ,'apploginid':'102'
      ,'getmasterinstallerpid':'/usr/local/bin/pidof Masterinstaller'
      ,'Reportercommand': '/usr/local/bin/pidof Reporter'
      ,'installbuild-flag':1 # 0 is for installing new build and 1 for continuing with existing one
      ,'uninstallcommand': '/Applications/McAfee LiveSafe - Internet Security Uninstaller.app/Contents/MacOS/McAfee LiveSafe - Internet Security Uninstaller'
      ,'preexpirycommand' :'date 1023103017'
      ,'postexpirycommand' :'date 1026103017'
      ,'ondayexpiry' :'date 1024103017'
      ,'timeanddatereset': 'ntpdate -u time.apple.com'
      ,'command':'/usr/local/bin/pidof Master'
      ,'icon':'image'
      ,'email':'suresh_ravuri@mcafee.com'
      ,'eicher_command':'echo ZQZXJVBVT >>'
      ,'referenceid' :'atomac.AXClasses.NativeUIElement AXApplication u\'McAfee LiveSafe - ...'
      ,'dmgdir':'/Users/sravuri/Downloads'
      ,'productdir':'/usr/local/McAfee/'
      ,'url':'https://home.mcafee.com/secure/protected/login.aspx?rfhs=1&culture=en-us'
      ,'login':".//*[@id='ctl00_m_HeaderFullNavigation_ucDashBoardPersonalNav_PersonalNavigation']/li[3]/a"
      ,'signin':".//*[@id='main-page']/div[1]/div/div[2]/div/div[1]/div[2]/div/div/ul/li[1]/a"
      ,'MyAccount': ".//*[@id='main-page']/div[1]/div/div[2]/div/div[1]/div[2]/a"
      ,'usernamebutton' : ".//*[@id='UserID']"
      ,'passwordbutton': ".//*[@id='Password']"
      ,'loginbutton':'btnLogin'
      ,'Myaccountnewpage': "//*[@id='ctl00_m_HeaderFullNavigation_ucDashBoardPersonalNav_hrefMyAccount']/span"
      ,'subscriptions': ".//*[@id='ctl00_m_HeaderFullNavigation_ucDashBoardPersonalNav_m_accountDropdown']/span/ul/li[3]/a"
      ,'AddDevice':'downLoadButton'
      ,'protectthismac':".//*[@id='m_ChooseDeviceType_divMac']/ul/li[1]/button"
      ,'chooseproductDownload':".//*[@id='btnDownload']"
      ,'ulaacceptcheckbox':'m_CheckEulaAccept'
      ,'downloadcheckboxxpath': ".//*[@id='ctl00_MainContent_m_PanelSmartDownload']/div[1]/div[2]/ol/li[1]"
      ,'downloadmacbuildbuttonid':'btnmac'
      ,'SerailNumber': "id('idDwnlManager')/x:span"
      ,'serailxpath': "html/body/div/table/tbody/tr[2]/td"
      ,'username':'chetanx.bharadwaj@intel.com'
      ,'password':'Mcafee123'
      ,'testresult':'/Users/user/Desktop/GuiconsumerAutomation/TestcaseResult.txt'
      ,'sourcepath':'/Users/user/Desktop/GuiconsumerAutomation/TestCase/'
      ,'foldername':'screenshotfolder'
      ,'Antimalwarestopcommand':'/usr/local/McAfee/AntiMalware/VSControl startoas'
      ,'Firewallstopcommand':'/usr/local/McAfee/StatefulFirewall/bin/StatefullFirewallControl stop'
      }


