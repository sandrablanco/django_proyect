#from module import suml, prodl
#zeroes = [ 0 for i in range(5)]
#ones = [ 1 for i in range(5)]
#print(suml(zeroes) == 0)
#print(prodl(zeroes) == 0)
#print(prodl(ones))
 #print(module.counter)

from sys import path 
path.append('..\\modules')
import module
zeroes = [ 0 for i in range(5)]
ones = [ 1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))