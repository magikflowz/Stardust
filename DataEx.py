import json
import requests
from twilio.rest import Client
import sys
from os import system, name
import os
from bs4 import BeautifulSoup as bs
import csv 
import time 
import re
import subprocess
import tabulate
import argparse
#from intelxapi import intelx
from termcolor import colored
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter

def clear():
       
    if name == 'nt':
        _ = system('cls')
        
    else:
        _ = system('clear')
        
def main():
    CRED = '\033[91m'
    CBLUE= '\033[94m'
    CEND = '\033[0m'
    CGREEN = '\33[92m'
    clear()
    welcome_message = print(CGREEN + """
 ________  ________  _________  ________     ___    ___ 
|\   ___ \|\   __  \|\___   ___\\   __  \   |\  \  /  /|
\ \  \_|\ \ \  \|\  \|___ \  \_\ \  \|\  \  \ \  \/  / /
 \ \  \ \\ \ \   __  \   \ \  \ \ \   __  \  \ \    / / 
  \ \  \_\\ \ \  \ \  \   \ \  \ \ \  \ \  \  /     \/  
   \ \_______\ \__\ \__\   \ \__\ \ \__\ \__\/  /\   \  
    \|_______|\|__|\|__|    \|__|  \|__|\|__/__/ /\ __\ 
                                            |__|/ \|__| 
                                                        
                                  
      """ + CEND)
    select_option = "Select an option"
    
    while True:
        
        options = [" Shodan ",
                   " Phone Number Search ",
                   " DB Search", 
                   "  _IntelligenceX", 
                   " Area Search"]
        
        print("Ninety percent of intelligence comes from open sources.\nThe other 10 percent, the clandestine work, is just more dramatic.\nThe real intelligence hero is sherlock Holmes, not James Bond.\n -Samuel V. Wilson, former director of the Defense Intelligence Agency\n")
        count =0
        for x in options:
            count += 1
            str_count = str(count)
            print(CRED + str_count + ".)" + x + CEND)
    
        select = input("\nType exit to close the program or enter back to the menu\n" + CBLUE +"Which option would you like to select: " + CEND)
        
        if select == "1":
            clear(), Shodan()
        
        elif select == "2":
            numbersearch()
        
        elif select == '3':
            clear(),db_search()
        
        elif select == '4':
            clear(), print("come back later")
            
        elif select == '5':
            clear(), AreaSearch()
        
        else:
            print("Enter a number")
            clear(), main()

def AreaSearch():
    import numberbrute
    AreaSearch.AreaSearch()
        
def Shodan():
    
    shodan_Welcome = print("""
                           
███████╗██╗  ██╗ ██████╗ ██████╗  █████╗ ███╗   ██╗
██╔════╝██║  ██║██╔═══██╗██╔══██╗██╔══██╗████╗  ██║
███████╗███████║██║   ██║██║  ██║███████║██╔██╗ ██║
╚════██║██╔══██║██║   ██║██║  ██║██╔══██║██║╚██╗██║
███████║██║  ██║╚██████╔╝██████╔╝██║  ██║██║ ╚████║
╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝
                                                   
                           """)
    from shodan import Shodan
    
    while(True):
        
        ip_search = input("Type exit to close the program or enter back to go to main menu" + "\nEnter ip address: ")
        if ip_search == 'exit':
            sys.exit()
        elif ip_search == 'back':
            clear(), main()
        else:
            try:
                
                ShodanIPScan = requests.get('https://api.shodan.io/shodan/host/8.8.8.8?key=')
                print("Host Results: \n")
                print(ShodanIPScan.json())
            except Exception as e:
                print(e)

def dehash():
    
    hashInput = input("Enter hash you want to dehash: ")
    
    querystring = {"func":"dehash","term":"aoYbhfmFM7neeC2LnmIL092VModuKzjh7cA="}

    headers = {
        "X-RapidAPI-Key": "86f93df49emsh464b6fd930ba9b1p12dd44jsn0bccdad54dcd",
	    "X-RapidAPI-Host": "breachdirectory.p.rapidapi.com"
    }

    response = requests.request("GET", url = "https://breachdirectory.p.rapidapi.com/", headers=headers, params=querystring)
    response = response.json()
 

    for key, value in response.items():
        password = value
        print(password)

def numbersearch():
    
    account_sid = "" #Account sid
    auth_token = "" #twilio api key

    client = Client(account_sid, auth_token)
                                                                        
    while True:
        en = '+1'
        number = input("Type exit to close the program or enter back to the menu" + "\nEnter phone number: ")
        

        if number == 'exit':
            sys.exit()

        if number == 'back':
            clear(), main()

        phone_number = client.lookups \
                .v1 \
                .phone_numbers(number) \
                .fetch(type=['caller-name'])
          
        #print(Location, getCarrier(number))
        print(phone_number.caller_name)
        stop = input("")
             
        if number == 'exit':
            sys.exit()
        if number == 'back':
            main()
            
def db_search():
    
    Count = 0 
    print("Search Methods")
    Methods_List = ["IP",
               "Email",
               "Username",
               "Domain"]
    
    for x in Methods_List:
        Count += 1
        strcount = str(Count)
        print(strcount + ".)"  + x)
    
    print("")
    Method = input("Enter method: ")
    Method = Method.lower()
    Query = input("Enter Search Query for {0} :".format(Method))
    

    try:
        '''
        print("BreachDirectory: \n")
        response_breach = requests.get("https://BreachDirectory.com/api_usage?method={0}&key=&query={1}".format(Method,Query))
        print(response_breach.json())
        '''
        print("--------------------------------")
        print("LeakCheck:")
        response_leakcheck = requests.get("https://leakcheck.net/api?key=96844162266aa4456d7928786b2e8c531769e5c2&check=".format(Query))
        print(response_leakcheck.json())
        input("Press enter to go back")
        main()

    except Exception as e:
        print(e)
        GoBackMessage = input("Please Enter to go back")
               
main()