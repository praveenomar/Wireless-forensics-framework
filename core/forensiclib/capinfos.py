#!/usr/bin/env python
#
# WFF Interface Design
# Created By Nipun Jaswal
# Email : mail@nipunjaswal.info
# Statistics Module For Finding Start time End Time And Duration
from conf import stats
import os
import colorama
from colorama import Fore, Back, Style
colorama.init()
#Finding the Start Time of The Capture
def capstart():
	command=stats.cap+stats.start_time
	execute=os.popen(command).read()
        print(Fore.RED+execute+Style.RESET_ALL)
#Finding the End time of the Capture
def capend():
        command=stats.cap+stats.end_time
        execute=os.popen(command).read()
        print(Fore.GREEN+execute+Style.RESET_ALL)
def capdur():
        command=stats.cap+stats.duration
        execute=os.popen(command).read()
        print(Fore.BLUE+execute+Style.RESET_ALL)	


	
