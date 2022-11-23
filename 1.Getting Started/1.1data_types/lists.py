
#list are the most flexible data type
#items in a list can be changed later in the program i.e they are flexible
#items in a list need not be of the same data type and are comma-separated
#example of a list in python
list = ['a','b','c','d']
print(list[2])
print("The number of items in this list = " + str(len(list)))#counting the number  of items in list

print(list *2)#repeating the items in a list and printing them out
# adding items in a list
list_1 =[1,2,3]
list_2 =[4,5,6]
print(list_1 + list_2) 
# membership in a list
print(6 in list_1)
# iteration in lists
for y in list_1:
    print(y)
 
 #comparing lists
# cmp(list_1,list_2)  
# 
# #returning maximum item in a list
print('###### returning maximum value in a list #####')
print(max(list_1))

##Returning a minimum value in a list###3
print('#### minimum value in list_1 ####')
print(min(list_1))

### Appending an object to list ###
list_2.append(7)
print(list_2) ## check if the oblect was really appended

#### counting the number of times an object occur ###
print('The object occur '+ str(list_2.count(5)) + ' times')


