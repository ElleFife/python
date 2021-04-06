#lpfeifer_x233_assignment5.py
#LaurenPfeifer

#QUESTION 1
favorite_numbers = {'eric': [3,6,9,12,15],
                    'sarah': [5,10,15,20,25],
                    'lauren': [4,8,12,16,20],
                    'james': [2,4,6,8,10],
                    'wanda': [1,2,3,4,5],
                    }
for k,v in sorted(favorite_numbers.items()):
    print(k,v)

#QUESTION 2
#As an alternative to the range function, some programmers like to increment a counter inside a while loop and 
#stop the while loop when the counter is no longer less than the length of the array. 
#Rewrite the following code using a while loop instead of a for loop.
'''
a = [7,12,9,14,15,18,12] 
b = [9,14,8,3,15,17,15] 
big = [ ] 
for i in range(len(a)): 
    big.append(max(a[i],b[i]))'''

a = [7,12,9,14,15,18,12] 
b = [9,14,8,3,15,17,15] 
big = []

i=0
while i < len(a):
    big.append(max(a[i],b[i]))
    print("Loop will stop bc it's greater than length of array")
    print(i)
    i += 1
else:
    print("Stop")

#QUESTIONS 3 AND 4
#QUESTION 3: Write a loop that reads each line of a file. It should count the number of characters in each line and keep track of
#the total number of characters read. Once you have a total of 1,000 or more characters, break from the loop. 
#(You can use a break statement to do this.)__

#QUESTION 4: Modify the program written in question 3 so that it doesn't 
#count characters on any line that begins with a pound sign (#).

infile = open('loopfile','r')
char_count = 0
count = 0
for line in infile:
    char_count += len(line)
    print(line)
    if char_count >= 100: #1000 not 100
        break
    if line.startswith('#'):
        continue
print(char_count)
print("File has {1} characters".format (count, char_count))