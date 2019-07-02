##this is an example of data type conversion
i='5'
o='hello'
p=int(i)	#convert to int
print(str(p))
#p=Long(i)
p=float(i)	#convert to float
print(str(p))
p=complex(i)	#convert to complex
print(str(p))
p=str(i)	#convert to str
print(p)
p=repr(i)	#convert to an expression str
print(p)
p=eval(i)	#convert to an object
print(p)
p=tuple(i)	#convert to a tuple
print(p)
p=list(o)	#convert to a list
print(p)
p=set(o)	#convert to set
print(p)
p=dict(i=o)	#convert to a dictionary
print(p)
p=frozenset(o)	#convert to a frozen set
print(p)
p=chr(65)	#convert to a int to charecter
print(p)
#p=unichr(65)	#convert int to unicode character
p=hex(65)	#convert ont to hex str
print(p)
p=ord('A')	#convert charecter to its int value
print(str(p))
p=oct(65)	#convert int to oct str
print(p)

