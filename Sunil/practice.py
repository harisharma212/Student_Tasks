def odd (a):
	if a % 2!=0:
		return (a)
print(filter(odd,[1,2,3,4,5,6,7,8,9,10]))

def hike(a):
	h=a+(a*10/100)
	return h
print(map(hike,(500,1000,1500)))


def add(a,b):
	print(a,b)
	return a+b
print(reduce(add,[1,2,3,4,5,6,7,8]))

l1=['a','b','c']
l2=[1,2,3]
print(zip(l1,l2))

