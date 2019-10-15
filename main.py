from random import randint 
then = 1
vybor = 1 
ball = []
while then <= 5:
  then += 1
  x = randint(1,6)
  line = int(input("Угадайте число от 1 до 6: "))
  funk = abs(line - x)

  if funk == 0:
    vybor = 6
    ball.append(vybor)
  elif funk == 1:
    vybor = 5
    ball.append(vybor)
  elif funk == 2:
    vybor = 4
    ball.append(vybor)
  elif funk == 3:
    vybor = 3
    ball.append(vybor)
  elif funk == 4:
    vybor = 2
    ball.append(vybor)
  elif funk == 5:
    vybor = 1
    ball.append(vybor)

  print("количество баллов; ",vybor)
  every = sum(ball)

print ("сумма баллов", every)

if every < 25:
  print("вы прориграли")
else:
  print(" вы выиграли")
