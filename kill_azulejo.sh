#!/bin/sh
#run this script to kill azulejo instances

kill `ps -ef | grep azulejo | grep -v grep | awk '{print $2}'`
