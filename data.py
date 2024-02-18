import requests

#open trivia api
API_URL = "https://opentdb.com/api.php"

#parameters for api request
parameters={
    "amount":10,
    "type":"boolean",
    "category":18
}

#requesting open trivia api for questions
questions=requests.get(url=API_URL, params=parameters)
data=questions.json()

#storing the question in list
question_data = [question for question in data["results"]]
   
    


