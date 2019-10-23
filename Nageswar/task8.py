"""
value = '4,3,1'

max_ele = max([int(i) for i in value.split(',')])

greatest = int('9' * max_ele)

while greatest % max_ele != 0:
	greatest -= 1

print(greatest)
"""

value = '2, 1, 16, 3, 4'

max_ele = max([int(i.strip()) for i in value.split(',')])

greatest = int('9' * max_ele)

while greatest % max_ele != 0:
	greatest -= 1

print(greatest)


