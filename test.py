import requests
import json
import pandas as pd

queryparam = input('Enter username, password,email or phone number: ')
url = "https://breachdirectory.p.rapidapi.com/"
querystring = {"func":"auto","term":"{}".format(queryparam)}

headers = {
	"X-RapidAPI-Key": "86f93df49emsh464b6fd930ba9b1p12dd44jsn0bccdad54dcd",
	"X-RapidAPI-Host": "breachdirectory.p.rapidapi.com"
}


results = [] 
response = requests.request("GET", url, headers=headers, params=querystring).text
#json_data = response.json()
response_info = json.loads(response)
type(response_info)

for result in response_info['result']:
    results.append(result['hash'])
    
results_df = pd.DataFrame(data = results, columns= ['has_password','password','sha1', 'hash'])


print(results_df)

'''
response = requests.request("GET", url, headers=headers, params=querystring)
json_data = response.json()

hashlist = []
for key, value in json_data.items():
    if key == 'result':
        writeFile = open('json.json', 'w')
        writeFile.write(str(key and value))
        writeFile.close()
        print("save successful")

'''

'''
url = "https://breachdirectory.p.rapidapi.com/"    

querystring = {"func":"dehash","term":"{}".format(param)}

headers = {
	"X-RapidAPI-Key": "86f93df49emsh464b6fd930ba9b1p12dd44jsn0bccdad54dcd",
	"X-RapidAPI-Host": "breachdirectory.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
response = response.json()
 
for key, value in response.items():
    password = value
    print(password)

'''
