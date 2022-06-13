import requests, json
  
# api-endpoint 
URL = "https://api.telegram.org/bot1374267801:AAFBeI6TX4rpsHeYJa3rG1rHHJqIEW9j7I8/sendMessage"
  
# location given here 

  
# defining a params dict for the parameters to be sent to the API 
PARAMS = {'text':'Hello','chat_id':'847114046'} 
  
# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 
  
# extracting data in json format 
data = r.json() 

print(data)