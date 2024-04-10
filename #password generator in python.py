#password generator in python
from itertools import product
import string 
characters=string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
print(characters)
min_length=1
max_length=2
myfile=open("password.txt","w")#w mode having capability to delete the old data of the file
counter=0#to know the counnt of generated passsword
for i in range(min_length,max_length+1):
  for j in product(characters,repeat=i):
    word="".join(j)
    myfile.write(word+"\n")
    counter+=1
print(counter)
print(j)