class op:
	a=list()
	def __init__(self):
		self.a=[]
	def get(self):
		size=int(input("Enter size"))
		for i in range(0,size):
			ele=int(input("Enter element"))
			self.a.append(ele)
		return self.a
	def __add__(self,other):
		b=[]
		for i in range(0,len(self.a)):
			b.append(self.a[i]+other.a[i])
		print(b)
	def __sub__(self,other):
		b=[]  
		for i in range(0,len(self.a)): 
			b.append(self.a[i]-other.a[i]) 
		print(b) 
	def __mul__(self,other):
		b=[]  
		for i in range(0,len(self.a)): 
			b.append(self.a[i]*other.a[i]) 
		print(b) 
	def __floordiv__(self,other):
		b=[]  
		for i in range(0,len(self.a)): 
			b.append(self.a[i]//other.a[i]) 
		print(b) 

 
