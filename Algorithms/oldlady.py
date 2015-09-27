#this is an elementary simulation for the problem given as follows:
#there are x amounts of seats (x=50 in this case), and x amount of people, each have a unique number
#at the front of the line is an old lady who sits randomly
#every subsequent person either sits in their seat if it is available, or sits in a random seat if it is not
#what is the probability that the last person in line sits in his seat (the first seat)
'''
Expected output: 50%

1 2:[1] [2]
   :[2] [1]

1 2 3: [1] [3] [2]
		 : [3] [2] [1]
		 : [1] [2] [3]
		 : [2] [3] [1]

if 1 wants to sit in his seat
then 3 needs to sit in her seat and 2 needs to gtfo and sit in his seat
if 3 sits in her seat, 1 will sit in his seat for sure
if 3 sits in seat 2, then 1 has a 50% chance of sitting in his seat
if 3 sits in seat 1, then 1 has a 0 % chance of sitting in his seat
[0+50%+100%]/3 = 50%
=2/4 50%

1 2 3 4: [1] [2] [3] [4] 
			 : [1] [2] [4] [3]
			 : [2] [3] [4] [1]
			 : [1] [3] [4] [2]
			 : [3] [2] [4] [1]
			 : [1] [4] [3] [2]
			 : [2] [4] [3] [1]
			 : [4] [2] [3] [1]
if 4 sits in her seat, then 1 has a 100% chance of sitting in his seat
if 4 sits in seat 3, then 1 has a 50% chance of sitting in his seat
if 4 sits in seat 2, then 1 has a 50% chance of sitting in his seat
if 4 sits in seat 1, then 1 has 0% chance

[1+1/2+1/2+0]/4 = [2]/4 = 50%
=4/8 50%
'''
import random

def oldLady(simulations,seats):
	oneInHisSeat = 0
	for i in range(simulations):
		emptyArr = [-1 for i in range(seats)]
		oldLadyChooses = random.randint(0,seats-1)
		if(oldLadyChooses==seats-1):
			oneInHisSeat += 1
		else:
			emptyArr[oldLadyChooses] = 49
			for i in range(seats-2,-1,-1):
				if(emptyArr[i]==-1):
					emptyArr[i]=i
				else:
					while(1):
						randomSeat = random.randint(0,seats-1)
						if(emptyArr[randomSeat]==-1):
							emptyArr[randomSeat] = i
							break
				if(emptyArr[0]!=-1):
					break
			if(emptyArr[0]==0):
				oneInHisSeat+=1
	return float(oneInHisSeat)/float(simulations)

print(oldLady(100000,50))
