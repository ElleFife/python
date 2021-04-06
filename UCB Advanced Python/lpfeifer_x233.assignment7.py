#lpfeifer_x233.assignment7.py

#THIS LESSON STILL THREW ME FOR A LOOP. I"LL CONTINUE TO WORK THROUGH IT. 
#NOTE THAT THIS ASSIGNMENT HAS A TON OF ERRORS AND FAULTY CODE THAT I DIDN"T QUOITE GET TO WORK THROUGH JUST YET
#ALSO I KNOW OUR COURSE ENDS TOMORROW, SO I"M CRANKING THE ASSIGNMENTS OUT AND WILL CORRECT WITH A TUTOR IN THE NEXT FEW
#WEEKS SO THAT I PROPERLY UNDERSTAND THE CONCEPTS

'''QUESTION 1. Suppose you want to determine whether an arbitrary text string can be converted to a number. 
Write a function that uses a try/except clause to solve this problem. 
Can you think of another way to solve this problem?'''

string = "Convert me into a number!"

def convert(string):
    try:
        return int(string)
    except ValueError:
        if string == "":
            return 0
        else:
            return "Bummer - it's still a string"
convert(string)
        
''' Need to do the alternate option - not sure how!'''

'''QUESTION 2. The input function will read a single line of text from the terminal. 
If you wanted to read several lines of text, you could embed this function inside a while loop and terminate the 
loop when the user of the program presses the interrupt key (Ctrl-C under UNIX, Linux and Windows.) 
Write such a program, and note its behavior when it receives the interrupt signal. 
Use a try/except clause to make the program behave more gracefully.'''
#I referenced: https://www.pyimagesearch.com/2018/03/12/python-argparse-command-line-arguments/
#I created a doc called "read_lines.py" which houses the following function

#command line action would look something like this:
#python read_lines.py --input Bird

import sys
print(sys.argv)

def read_lines(): #what do we put in the #() I know I need a function that reads lineS from terminal - use sys?
    text = input("Please enter something: ")
    print("You entered: " + text) 
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)
    