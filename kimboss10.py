 import requests

url = "https://sms-international.p.rapidapi.com/WebTool/SMStoCountry/sms1"

 int_string = input("Enter phone numbers, separated by comma: \n")
    input_string2 = input("Enter Text and press Enter: \n")
    numbers = int_string.split(",")
headers = {
    'x-rapidapi-key': "87aa264292msh2e35dac4ce1ce22p11813ejsn51eefb26e5ba",
    'x-rapidapi-host': "sms-international.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=int_string)

print(response.text)
