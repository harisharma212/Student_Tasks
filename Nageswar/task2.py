print(' 1 . write a program to print even numbers of given list')

l1 = [2,1,6,7,11,14]

for i in l1:
	if i%2 == 0:
		print('Even Number is',i)


print('=================================')

print('2 . Write A program to Convert list of elements into string')
l2 = [1,2,3,4]

l3 = []

for i in l2:
	l3.append(str(i))
	
print(l3)


print('=================================')

print('3 . Write a program To print Sum Of Square')

a = [2,4,6,8]
sum = 0
for i in a:
	
	sum  = i**2+sum
print("Sum Of Square Of :",sum)


print('4 . Write program print palindrom from list of number')

b = [123,1221,168,868,'malayalam']

for i in b:
	c = str(i)
	if c == c[::-1]:
		print(c)

print('=================================')
