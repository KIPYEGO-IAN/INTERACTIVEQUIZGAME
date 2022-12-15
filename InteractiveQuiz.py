print("Hello,welcome to today geography quiz.All the best!")

condition=input("Are you ready to attempt the quiz now? ")
if condition.lower() == "yes":
    print("You allocated 10 minutes to finish the quiz")
else:
    print("Remember the quiz is opened from 10am-11am")
    quit()

score = 0

print("Question I")
Question1=input("Which country has the longest coastline in the world? ")
if Question1.upper() == "CANADA":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

print("Question II")
Question2=input("What is the capital of Malta? ")
if Question2.upper() == "VALETA":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

print("Question III")
Question3=input("Which counrty is the newest to be recognized by UN? ")
if Question3.upper()=="SOUTH SUDAN":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

print("Question IV")
Question4=input("In which UK city will you find river Clyde? ")
if Question4.upper()=="GLASGOW":
    print("Correct!")
    score +=1
else:
    print("incorrect!")

print("Question V")
Question5=input("What is the oldest recorded town in the UK? ")
if Question5.upper()=="COLCHESTER":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

print("Question VI")
Question6=input("If you travelled to the city of Volgograd,which country will you be? ")
if Question6.upper()=="RUSSIA":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

print("Question VII")
Question7=input("What is the name of the largest river to flow through Paris? ")
if Question7.upper()=="THE SEINE":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

print("Question VIII")
Question8=input("What did Ceylon change its name to in 1972? ")
if Question8.upper()=="SRI LANKA":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

print("Question IX")
Question9=input("What is the most populas city in the US state of Illinois? ")
if Question9.upper()=="CHICAGO":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

print("Question X")
Question10=input("What is the highest mountain in Britain? ")
if Question10.upper()=="BEN NEVIS":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

print("You got " + str(score) +" marks")
print("Which equals to " + str((score/10)*100) + "%")
