# Concatenate Lists: Given two lists, create a new list that combines both lists.

a = ['superr', 'banana', 'superr', 'banana']
meva = ['apple', 'banana', 'superr', 'apple', 'banana', 'banana', 'apple', 'banana']

meva.extend( ['superr', 'banana', 'superr', 'banana'])
print(meva)  

# Result
# ['apple', 'banana', 'superr', 'apple', 'banana', 'banana', 'apple', 'banana', 'superr', 'banana', 'superr', 'banana']