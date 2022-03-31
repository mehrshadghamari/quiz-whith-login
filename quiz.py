from answer import correct_answer
from question import questions
import random

def show_users_quiz():

    a=[]
    for i in range(20):
        b=random.choice(list(questions.items()))
    
        if len(a)==10:
            break

        if b in a:
            continue
        else:
            a.append(b)
    
    score=0
    j=1
    for i in a:
        print(i[1])
        c=input(f'question {j}-  please write your answer: ')
        j+=1
        if c==correct_answer[i[0]]:
            score+=1


    print(f'your score is {score}')