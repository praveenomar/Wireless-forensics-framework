#!/usr/bin/env python
#
# WFF Interface Design
# Created By Nipun Jaswal
# Email : mail@nipunjaswal.info
from conf import notation
import os
import colorama
from colorama import Fore, Back, Style
colorama.init()                  	
#Show All Authentication Requests Module
def show_all_association_requests():
        command=notation.libc+ " -r "+notation.pack_file+" -R "+notation.associations_req + notation.sort_source_dest
        execute=os.popen(command).read()
        if(execute==""):
		print "No Associations Found"
	else:
		source,dest=execute.split(",")
        	print"Source"+"\t\t\t\t\t\t"+"Destination"
        	print source+"\t\t====>\t\t"+dest


	




	
