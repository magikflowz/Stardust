import json 
import requests

queryparam = input('Enter username, password,email or phone number: ')
url = "https://breachdirectory.p.rapidapi.com/"
querystring = {"func":"auto","term":"{}".format(queryparam)}

headers = {
	"X-RapidAPI-Key": "86f93df49emsh464b6fd930ba9b1p12dd44jsn0bccdad54dcd",
	"X-RapidAPI-Host": "breachdirectory.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
json_data = response.json()

hashlist = []
for key, value in json_data.items():
    if key == 'result':
        writeFile = open('json.json', 'w')
        writeFile.write(str(key and value))
        writeFile.close()
        print("save successful")