import random
def coinToss():
	coinStream = ['1' if random.random() > 0.5 else '0' for i in range(10)]
	return ''.join(coinStream)

coinTossList=[]
[coinTossList.append(coinToss()) for i in range(100000)]
sumAllHeads=coinTossList.count('1111111111')
print(str(float(sumAllHeads)/len(coinTossList)*100) + '%')
