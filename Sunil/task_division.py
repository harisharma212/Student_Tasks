
values = '4,3,1'
big = max([int(i) for i in values.split(',')])
greatest = int('9'* big)
while greatest % big !=0:
	greatest -= 1
	print(greatest)

"""
class A :
	def __init__(self,a,b):
		self.a = a
		self.b = b
	def add (self):
		return self .a+self .b
	def mul (self):
		return self.a*self.b	

obj = A(20,30)
print(obj.mul())
"""