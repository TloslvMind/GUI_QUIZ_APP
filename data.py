import requests

response = requests.get("https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean")

question_data = [{"question": d["question"], "correct_answer": d["correct_answer"]} for d in response.json()["results"]]
