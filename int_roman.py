"""Write a Python class to convert an integer to a roman numeral.

a = Roman(10)
a.value = 'X'

b = Roman(8)
a.value = 'VIII'

"""

"""

pair = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

#1-9
ones = ['','I','II','III','IV','V','VI','VII','VIII','IX']
#10-90
tens = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
#100-900
hundreds = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
#1000-3000
thousands = ['','M','MM','MMM']
result = thousands[A//1000]+hundreds[(A%1000)//100]+tens[(A%100)//10]+ones[(A%10)]
return (result)



        """
class Roman(object):
	def __init__(self,number):
		self.number = number
		self.value = self.convert()

	def convert(self):
		pair = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

		#1-9
		ones = ['','I','II','III','IV','V','VI','VII','VIII','IX']
		#10-90
		tens = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
		#100-900
		hundreds = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
		#1000-3000
		thousands = ['','M','MM','MMM']
		result = thousands[self.number//1000]+hundreds[(self.number%1000)//100]+tens[(self.number%100)//10]+ones[(self.number%10)]
		return (result)

	def __repr__(self):
		return self.value


a = Roman(11)

