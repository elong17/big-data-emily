# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def bookTitle (Title: str, N: int='N'):
    Title = str(input("Enter a booktitle:\n"))
    N = int(input("Enter a number:\n"))
    
    return 'The number ' + str(N)+ ' bestseller today is: ' + str(Title.title())
    
bookTitle()


def nReq():
    Title = (input("Enter a booktitle:"))    
    
    while True:
        try:
            N = int(input("Enter a number:"))
        except ValueError:
            print("You must enter a number.")
            continue
        else:
            break

    print ('The number ' + str(N)+ ' bestseller today is: ' + str(Title.title()))
    
def titleReq():
    while True:
        Title = str(input("Enter a title:"))
        if Title == '':
            print("You must enter a title.")
            continue
        else:
            break
    
    N = (input("Enter a number:"))
    
    print ('The number ' + str(N)+ ' bestseller today is: ' + str(Title.title()))

def allOpt():
    Title = (input("Enter a booktitle:"))  
    N = (input("Enter a number:"))
    print ('The number ' + str(N)+ ' bestseller today is: ' + str(Title.title()))

def testfxn (name, age="39"):
    
    print("your name is", name, "and your age is", age)

def inputPW():
    '''
    Asks for user input. 
    Returns user submitted password
    '''
    print ("Enter a new password.\n Your password must meet the following criteria:.\n Contain at least 2 numbers.\n Contain at least 1 uppercase letter.\n Contain at least 1 special character from the following: !@#$%^&*()-_+= \n") #prompt for input
    yourPW = str(input()) #asks for password, stores as string
    return yourPW #returns submitted password

def verifyPW(x):
    '''
    checks pw against criteria.
    Returns True if meets all criteria.
    False otherwise.
    '''
    digit = 0  #initiate counter for numbers
    upper = 0   #initiate counter for uppercase letters
    char = "!@#$%^&*()-_+=" #charset in criteria
    charN = 0   #initiate counter for special characters
    if len(x) >= 8 and len(x) <= 14: #if the password is the correct length,
        for i in x: #for ea. character in the password
            if i.isnumeric(): #if it is a number,
                digit+=1 #add to number counter
            if i in char: # if it is a special character
                charN +=1 #add to special character counter
            if i.isupper(): #if it is a uppercase letter
                upper+=1 #add to uppercase counter
        if digit >= 2 and charN >=1 and upper >=1: #if all criteria are met
            return True #return True
        else:
            return False #otherwise return False
            
def newPW(attempts=3):
    '''
    Gives feedback as to whether user enters valid pw. 
    Takes one argument, attempts, the # of attempts a 
    user is given to submit a valid password.  
    '''
    while attempts > 0: #if user has attempts remaining,
        PW = inputPW()  #prompts user to enter new password
        if verifyPW(PW):  #if PW meets criteria,
            print ("**SUCCESS** Your new password has been saved.") #print success msg
            break #break out of loop
        else:
            attempts -=1 #otherwise, deduct an attempt
            print ("**ERROR** Please make sure your password meets the criteria.") #print error message
            print ("You have", attempts, "attempts remaining.") #let user know # of tries remaining
            continue #continue with loop
    else: #if out of attempts,
        print ("Sorry. You have run out of attempts") #let user know, they have run out of attempts

def exp(x, y):
    '''
    Function that calculates the exponent. 
    x is the base, y is the exponent. 
    Returns the result of the exponentiation.
    '''
    total = 1 #initiate variable, total
    for i in range(y): # loop through y times
        total*=x # multiply x by itself, 
    return total #returns the product
    
print(exp(2, 3))
print(exp(5, 4))


def mymin(L):
    '''
    Takes one argument: L, list of numbers, and
    returns the lowest number in the list.
    '''
    temp = 0     #to store lowest element found
    for i in range(len(L)-1): #check every element
        if L[i]<L[i+1]: #if an element is smaller than the next element,
            temp = L[i] #store it as the lowest
        else: 
            temp = L[i+1] #otherwise store the next element
    return temp 
    
def mymax(L):
    '''
    Takes one argument: L, list of numbers, and
    returns the highest number in the list.
    '''
    temp = 0    #temp to store highest element found
    for i in range(len(L)-1): #check every element
        if L[i]>L[i+1]: #if an element is larger than the next element,
            temp = L[i] #store it as the highest
        else:
            temp = L[i+1] #otherwise store the next element
    return temp

M = [0.1, 9.0, -89]
N = [10000000, 9.099, 9.199, -89000000]

print ("min of M:", mymin(M),".", "max of M:", mymax(M))
print ("min of N:", mymin(N),".", "max of N:", mymax(N))