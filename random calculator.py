import random
number1=random.randint(1,1000)
number2=random.randint(1,100)

data_valid=False
while data_valid== False:
    answer= input('what is '+ str(number1)+ ' + '+ str(number2)+ '? \n')
    try:
        answer=int(answer)
    except:
        print('only numbers in integer format are accepted. Check your input and make the appropraite correction')
    else:
        data_valid=True
if int(answer)== (number1+number2):
    print('Correct! You provided the correct answer to the question')
else:
    print('Nope! The answer is ' + str(number1+number2))

