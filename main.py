import random
again = 1
while again == 1:
  again = 0
  points = 0
  numbers = []
  def question(q,a,value):
    x = input(q)
    if x == str(int(a)):
      print("Correct! Great job!")
      return(value)
    else:
      print("That is incorrect. The correct answer is",a)
      return(0)
  print("Welcome to my quiz. This quiz requires you to solve randomized basic math questions. Good luck!")
  print("The following questions are worth 1 point: ")
  for i in range(5):
    num1 = 0
    num2 = 0
    if random.randint(1,2) == 1:
      while 10*num1+num2+100 in numbers or 10*num2+num1+100 in numbers or num1 + num2 == 0:
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
      numbers.append(10*num1+num2+100)
      points+=question(str(num1)+"+"+str(num2)+": ",num1+num2,1)
    else:
      while 10*num1+num2+200 in numbers or 10*num2+num1+200 in numbers or num1 + num2 == 0:
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        num1 += num2
      numbers.append(10*num1+num2+200)
      points+=question(str(num1)+"-"+str(num2)+": ",num1-num2,1) 
  numbers=[]
  print("The following questions are worth 2 points: ")
  for i in range(5):
    num1 = 0
    num2 = 0
    if random.randint(1,2) == 1:
      while 10*num1+num2+100 in numbers or 10*num2+num1+100 in numbers or num1 + num2 == 0:
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
      numbers.append(10*num1+num2+100)
      points+=question(str(num1)+"*"+str(num2)+": ",num1*num2,2)
    else:
      while 10*num1+num2+200 in numbers or 10*num2+num1+200 in numbers or num1 + num2 == 0:
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        num1 *= num2
      numbers.append(10*num1+num2+200)
      points+=question(str(num1)+"/"+str(num2)+": ",num1/num2,2) 
  message = ""
  if points < 10:
    message = "Better luck next time."
  elif points < 12:
    message = "Not bad."
  elif points < 14:
    message = "Good job."
  elif points == 14:
    message = "Great job!"
  else:
    message = "Amazing job!"
  print("Your final score is",points,"out of 15, which is",round(100*points/15),"percent.",message)
  keepGoing = input("Want to go again? (y/n) ")
  if keepGoing == "y" or keepGoing == "yes" or keepGoing == "Yes":
    again = 1
