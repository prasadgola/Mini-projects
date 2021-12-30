class person:
	def __init__(self,name,age,address):
		self.name=name
		self.age = age
		self.address = address

	def __repr__(self):
		return "person({},{},{})".format(self.name,self.age,self.address)
	def __str__(self):
		return "{} is {} years old".format(self.name,self.age)

p1 = person('jerin',50,'delhi')
p2 = person('jn',0,'lhi')
print(p1)
print(p2)