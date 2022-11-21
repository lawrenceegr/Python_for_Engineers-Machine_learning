
print('please enter your score :')#prompt the user to enter their grade

score = input()#will take in a value in string
score = float(score)#convert the string to float 

###check the score against the grading system
message = 'Your score is '
if score >= 80 and score <= 100 :
    print(message + 'A')
elif score >= 60 and score < 80:
    print(message + 'B')
elif score >= 50 and score < 60:
    print(message + 'C')
elif score >= 40 and score < 50:
    print(message + 'D')
elif score >= 0 and score < 40:
    print(message + 'F')
else:
    print(message + "not in the scope of our grading system please enter a valid grade")