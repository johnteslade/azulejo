#!/bin/sh
#run this script to kill azulejo instances, you'll want this instead of pkill, killall

kill `ps -ef | grep azulejo | grep -v grep | awk '{print $2}'`
