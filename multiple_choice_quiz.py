from questions import question

question_prompts = [
    "What is 1 + 1? \n (a) \n 2 (b) \n 3 (c) \n 4 (d) 1",
    "Which country is called Land of the Rising Sun? \n (a) India \n (b) \n Pakistan (c) \n Japan (d)\n Peru",
    "How many bones an average adult male has at 7:00am? \n (a) 206 \n (b) \n 207 (c)\n 208 (d)\n 307"
]

questions = [
    question(question_prompts[0],"a"),
    question(question_prompts[1],"c"),
    question(question_prompts[2],"a")
]

def run_test (questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            print ("Your answer is correct")
            score+= 1
    print("You got" + str(score) + "out of 3")
    
run_test(questions)
            
    