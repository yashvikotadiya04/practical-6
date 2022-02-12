#ID: 20CE045
#NAME: YASHVI KOTADIYA

from collections import Counter
t=int(input ())        #number of test cases
l=list()               #list for storing string
for _ in range (t):
    l.append(input())  #add a string to the existing list
x=Counter(l)           #counter() count the  items in an iterable list

print (len(x))         #length of counter function
print(*x.values())      #unpackaging the item using asterisk operator
