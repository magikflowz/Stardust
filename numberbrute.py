import random
import phonenumbers
from phonenumbers import geocoder, carrier
from twilio.rest import Client
import os
from twilio.rest.lookups.v1 import phone_number

account_sid = "" # twilio id
auth_token = "" #twilio api key
client = Client(account_sid, auth_token)

area_code = "419" #Enter area code here
area_code2 = ""   #Enter second area code 
ending = "32"

numeric = "0123456789"

key = ''

def double_brute():
    while True:
        for v in range(len(numeric)):
            for e in range(len(numeric)):
                for n in range(len(numeric)):
                    for o in range(len(numeric)):
                        for m in range(len(numeric)):
                            key_1 = '+1' + area_code + '-' + numeric[v] + numeric[e] + numeric[n] + '-' + numeric[o] + numeric[m] + ending
                            print(key_1)
                            phone_number = client.lookups \
                            .v1 \
                            .phone_numbers('+1'+key_1) \
                            .fetch(type=['caller-name'])    
                            print(phone_number.caller_name)

                            for a in range(len(numeric)):
                                for b in range(len(numeric)):
                                    for c in range(len(numeric)):
                                        for d in range(len(numeric)):
                                            for e in range(len(numeric)):
                                                key = '+1' + area_code + '-' + numeric[a] + numeric[b] + numeric[c] + '-' + numeric[d] + numeric[e] + ending
                                                print(key)
                                                phone_number = phonenumbers.parse(key)
                                                valid = phonenumbers.is_valid_number(phone_number)

def selection_1():
    while True:
        for v in range(len(numeric)):
            for e in range(len(numeric)):
                for n in range(len(numeric)):
                    for o in range(len(numeric)):
                        for m in range(len(numeric)):
                            key_1 = '+1' + area_code + numeric[v] + numeric[e] + numeric[n] + numeric[o] + numeric[m] + ending
                            print(key_1)
                            phone_number = client.lookups \
                            .v1 \
                            .phone_numbers(key_1) \
                            .fetch(type=['caller-name'])    
                            print(phone_number.caller_name)

selection_1()