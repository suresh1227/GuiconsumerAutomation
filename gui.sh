#!/usr/bin/env bash
#/usr/bin/python
# Copyright (C) 2017 McAfee, Inc.  All rights reserved.
# TestcaseID: 0
# TestcaseDescription: this script will run all the gui automation script files in order.
#__author_: Sureshravuri

MAX_TRY=5
SECONDS_TO_WAIT=1
#
#export pathtochange="/Users/suresh/Desktop/consumerguiAutomation/TestCase"
#cd $pathtochange
#
cd TestCases
file_count=`ls -l gui_testcase*.py | wc -l | sed -e 's/^[ \t]*//'`
#
for file in `eval echo gui_testcase{1..$file_count}.py`; do
	count=0
	while true
	do
		V1=`ps -aef | grep LifeSafe | wc -l` 
		if [ "$V1" -ge 1 ] # UI is up, run the current testcase 
		then
			sleep 30
			echo "Running testcase: $file"
			python $file
			#killall -9 python
			#
			# We have successfully executed the testcase so exit the while loop
			break
		else # Wait for the UI to come up
			echo "Waiting for $SECONDS_TO_WAIT seconds..."
			sleep $SECONDS_TO_WAIT
		fi
		count=`expr $count + 1`
		if [ $count -eq $MAX_TRY ]
		then
			break
		fi
		echo "Retrying tedstcase: $file"
	done
done
popd
