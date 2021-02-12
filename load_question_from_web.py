import requests
import random
import json

def load_questions_from_web():
    """
    Loads questions bank from file	## FILE SUPPORT TO BE ADDED LATER
    Recieves: -
    Returns: questions dictionary
    """
    # sending http request
    r = requests.get(http_api_questions)
    
    # loading the content to JSON object
    json_content = json.loads(r.content)
    
    # deleting unnecessary value from the JSON
    del json_content['response_code']

    # creating the questions dict
    questions = {}

    # questions from the JSON (in list [])
    questions_from_json = json_content['results']

    # looping through the questions, convert it to usual formatted question
    for index_question, question in enumerate(questions_from_json):

        # correct-answer
        correct_answer = question["correct_answer"]

        # list of all answers
        all_answers = [correct_answer] + question["incorrect_answers"]

        # shuffling the list [otherwise, the answer will always be in the first place]
        random.shuffle(all_answers)

        # finding the new index of the correct-answer
        correct_answer_index = all_answers.index(correct_answer)

        # important! - converting from 'XML\CSS\HTML' format to 'utf-8'
        fixed_replaced_question = question["question"].replace("&#039;", "'").replace("&quot;", "'")
        
        # discarding specific question if it still has unwelcomed characters
        if(fixed_replaced_question.find('#') != -1 or fixed_replaced_question.find('|') != -1):
            break
        
        # copying the question to the new dict
        questions[str(index_question)] = {
            "question" : fixed_replaced_question,
            "answers" : all_answers,
            "correct" : str(correct_answer_index + 1)
            }
    
    # returns the questions' dict
    return questions
