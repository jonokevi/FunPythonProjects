import random

random_number= random.randint(1, 9)

#print(random_number)

Q= input("Question: ")   #Enter your question

#question = ("Am I wearing red today?")

answer= ("")


if random_number == 1:
  answer= ("Just do it. Don't let your dreams be dreams!")
elif random_number ==2:
 answer= ("There's no better day like the present.")
elif random_number ==3:
 answer= ("Rise and grind.")
elif random_number ==4:
 answer= ("Get that bread.")
elif random_number ==5:
  answer= ("Yes. Go be the best you.")
elif random_number ==6:

  answer= ("Do it. Legends weren't built overnight.")
elif random_number ==7:
  answer= ("Make the day yours.")
elif random_number ==8:
  answer= ("Stay consistent.")
elif random_number ==9:
  answer= ("You win these.")
else:
  answer= ("Error")

print(Q)
print("Magic 8-Ball's answer: " + answer)