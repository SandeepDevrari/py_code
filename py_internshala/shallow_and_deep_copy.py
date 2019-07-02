##this is an example of "SHALLOW AND DEEP COPY" in python3
##Objects in python are immutable and mutable
import copy
num=[2,3,4,5]
n_shallowcopy=None
n_shallowcopy=copy.copy(num)
print(id(num)==id(n_shallowcopy))
print(id(num[0])==id(n_shallowcopy[0]))
num.append(7)
n_shallowcopy.append(10)
print(num,n_shallowcopy)
#n_shallowcopy[0].append(0)
#print(num,n_shallowcopy)
n_deepcopy=None
n_deepcopy=copy.deepcopy(num)
print(id(num)==id(n_deepcopy))
print(id(num[0])==id(n_deepcopy[0]))
n_deepcopy.append(9)
print(num,n_deepcopy)
