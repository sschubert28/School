'''
CS 2302 Data Structures
Writen by Steven Schubert
Lab 1 - Option B (Password Cracking)
Insrcutor Diego Aguirre
T.A. Gerardo Barraza
Last modification 9/9/2019
The purpose of this code is to find
all the passwords from 100 users
using only recursion
'''


import hashlib
#import sys #Added this so the code could work

#sys.setrecursionlimit(4000) # Increases the recursion depth limit to 4000
#print(sys.getrecursionlimit()) #Prints the recursion depth limit

def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig

'''
The main method calls every method to read the file and look
for the password. No parameters. No return
'''
def main():
    hex_dig = hash_with_sha256('This is how you hash a string with sha256')
    print(hex_dig)
    text = read_file()
    counter = 0
    password = ' '
    while counter < 100:
        all_split = text[counter].split(',') #Splitting the lines in the file  by the coma
        for size in range(3, 8):
            password = create_password('', size, all_split[1], all_split[2])
        print("The password for User" + str(counter) + " is: " + password)
        counter += 1
     
'''
The read_file() method opens the file and then reads the whole
file line by line stroring in a list after the EOF the file is
closed and returns the list. No parameters. Return the text file
as a list
'''
def read_file():
    file1 = open("password_file.txt","r+")  
    text = file1.readlines()
    file1.close()
    return text
'''
The create_password() method is a recursive method that creates
password of the given size and checks if the password mathes with
the hash from the user. 4 paramters password, size, salt, 
user_hash_code; password is the string created; size is the length
of the password; salt is the unique string added to the password;
user_hash_code is the hash code of the user. Returns the 
correct password
'''  
def create_password(password, size, salt, user_hash_code):
    if len(password) == size:
        if hash_with_sha256(password + salt) == user_hash_code:
            return password
    for i in range(10):
        create_password(password + str(i), size, salt, user_hash_code)

'''
The check_password() method checks if the hash code is the same
as the one from the user. 2 parameters password, hash_code;
password is the password being check with the salt added;
hash_code is the users hash code; return true if correct and false
if wrong
''' 
def check_password(password, hash_code):
    print(password)
    new_hash = hash_with_sha256(password)
    if new_hash == hash_code:
        return True
    return False

main()