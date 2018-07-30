import random 

ourList = list()
belowFive = list()
count = 0 
while (count < 11):
    ourList.append(random.randint(1,10))
    count += 1
  
print "Random numbers between 1 and 10" , ourList
for num in ourList:
	if num<5:
		belowFive.append(num)
print "Random numbers below 5. Answer: "
print belowFive
