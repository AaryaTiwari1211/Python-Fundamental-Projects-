
import questions as hello


question_prompts = [
    "What is 1 + 1? \n (a) 2 \n (b)  3 \n (c)  4 \n(d) 1",
    "Which country is called Land of the Rising Sun? \n (a) India \n (b)  Pakistan \n (c)  Japan \n (d) Peru",
    "How many bones an average adult male has at 7:00am? \n (a) 206  \n(b) 207 \n(c) 208 \n(d) 307"
]

questions = [
    hello.question(question_prompts[0],"a"),
    hello.question(question_prompts[1],"c"),
    hello.question(question_prompts[2],"a")
]

def run_test (questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:   
            score+= 1
    print("You got" + str(score) + "out of 3")
    
run_test(questions)
            
    