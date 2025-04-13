#Error Correction Exercise----------------
#print("HELLO WORDDD') #Error
#data = [1, 2, 3, 4) #Error
#print(data)

#Shape Correct-----------------------------
print("HELLO WORDDD")
data = [1, 2, 3, 4]
print(data)
print()

#Method Error------------------------------
#nr = (input('Enter one number: '))
#s = nr * 3
#print(s)

#Shape Correct------------------------------
nr = int(input('Enter one number: ')) #Error
s = nr * 3
print(s)
print()

#Other Alternative--------------------------
nr = eval(input('Enter one number: '))
s = nr * 3
print(s)
q = 12 / s
print(q)
print()

#Error Division-------------------------------
#result = 10 / 0
#print(result)

#Method Correct--------------------------------
denominator = 0

if denominator != 0:
    result = 10 / denominator
    print(result)
else:
    print("Error: Division by zero not allowed!")
print()

#Error Two--------------------------------------
#for i in range(5)
#    print(i)

#Correction Two---------------------------------
for i in range(5):
    print(i)
print()

#Indentation error------------------------------
#def sum(a, b):
#return a + b

#Correction-------------------------------------
def sum(a, b):
    return a + b
r = sum(2 , 4)
print(r)


