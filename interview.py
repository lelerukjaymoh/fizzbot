import requests
import json

start_url = "https://api.noopschallenge.com"

#GETing introduction

question = requests.get(start_url+'/fizzbot')
if question.status_code != 200:
    print("Got {} error while GETing data".format(question.status_code))

print(question.json()['message'])
next_question = "/fizzbot/questions/1"


#GETing first questions

url = start_url+next_question

question = requests.get(url)
if question.status_code != 200:
    print("Got {} error while GETing data".format(question.status_code))

print(question.json())

print("")
print("")

print(question.json()['message'])

ans = str(input("\n\nEnter ans: ")) #python

answer = requests.post(url, json={"answer": ans})
if question.status_code != 200:
    print("Got {} error while GETing data".format(question.status_code))

print(answer.json())

results = answer.json()['result']

next_question = answer.json()['nextQuestion']


while results == "correct":
    print("correct answer")
    print("")
    print("")
    url = start_url+next_question
    if question.status_code != 200:
        question = requests.get(url, json={"answer": ans})
        print("Got {} error while GETing data".format(question.status_code))

    print(question.json())

    print(question.json()['message'])
    ans = str(input("\n\nEnter ans: "))


    answer = requests.post(url, json={"answer": ans})
    if answer.status_code != 200:
        print("New data was not added. Returned error {}".format(answer.status_code))

        print(answer.json())

        next_question = answer.json()['nextQuestion']
        results = answer.json()['result']

while results != "correct":
    print("You failed enter the answer again:")
    ans = str(input("\n\nEnter ans: "))

    answer = requests.post(url, json={"answer": ans})
    if answer.status_code != 200:
        print("New data was not added. Returned error {}".format(answer.status_code))

        print(answer.json())

        next_question = answer.json()['nextQuestion']
        results = answer.json()['result']
