import requests

url = "https://breachdirectory.p.rapidapi.com/"

querystring = {"func":"dehash","term":"aoYbhfmFM7neeC2LnmIL092VModuKzjh7cA="}

headers = {
	"X-RapidAPI-Key": "86f93df49emsh464b6fd930ba9b1p12dd44jsn0bccdad54dcd",
	"X-RapidAPI-Host": "breachdirectory.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
response = response.json()
 

for key, value in response.items():
    password = value
    print(password)

