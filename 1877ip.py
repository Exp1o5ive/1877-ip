import getpass
import time
import os
os.system("clear")
from io import BytesIO
import pycurl
import os
import requests
import threading
from multiprocessing.dummy import Pool,Lock
from bs4 import BeautifulSoup
import time
import smtplib,sys,ctypes
from random import choice
from colorama import Fore
from colorama import Style
from colorama import init
import socket
from requests.adapters import HTTPAdapter
import sys
import random
import requests, threading, os
import os.path
import json
init(autoreset=True)
fr = Fore.RED
gr = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT
from random import choice

headers = {}
print('''\033[1;31;40m**********************************"
\033[1;31;40m**********************************"
\033[1;31;40m**********************************"
\033[1;37;40m************\033[1;33;40m**********\033[1;37;40m************"
\033[1;37;40m************\033[1;33;40m**********\033[1;37;40m************"
\033[1;37;40m************\033[1;33;40m**********\033[1;37;40m************"
\033[1;32;40m**********************************"
\033[1;32;40m**********************************"
\033[1;32;40m**********************************"
\033[1;37;40m   WwW.1877.TeaM - CodeBoy1877
\033[1;37;40m     Auto TOR IP Changer''')

def display_header(header_line):
    header_line = header_line.decode('utf-8')
    if ':' not in header_line:
        return
    h_name, h_value = header_line.split(':', 1)
    h_name = h_name.strip()
    h_value = h_value.strip()
    headers[h_name] = h_value

def userr():
	os.system("sudo apt-get install privoxy")
	os.system("sudo service tor start")
	print("========== \n")
	os.system("clear")
	print('''
	\033[1;31;40m**********************************"
	\033[1;31;40m**********************************"
	\033[1;31;40m**********************************"
	\033[1;37;40m************\033[1;33;40m**********\033[1;37;40m************"
	\033[1;37;40m************\033[1;33;40m**********\033[1;37;40m************"
	\033[1;37;40m************\033[1;33;40m**********\033[1;37;40m************"
	\033[1;32;40m**********************************"
	\033[1;32;40m**********************************"
	\033[1;32;40m**********************************"
	\033[1;37;40m WwW.1877.TeaM - CodeBoy1877
	\033[1;37;40m  Auto TOR IP Changer''')
	req = input("\n\nHow many times do you want to change your IP >>> : ")
	tim = input("How long is the change between each IP >>> : ")
		
	for i in range(req):
		time.sleep(tim)
		os.system("sudo service tor reload")
		print(">>>>>>>>>>> Your IP Has Been Changed <<<<<<<<<<")
			
	else :
		print("Something is wrong")
		

print("      ============================================================================================")
print("                                     >>>>>> Auto IP Changer <<<<<<")
print("      ============================================================================================")



userr()

