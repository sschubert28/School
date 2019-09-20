'''
CS 2302 Data Structures
Writen by Steven Schubert
Lab 1 - Option B (Password Cracking)
Insrcutor Diego Aguirre
T.A. Gerardo Barraza
Last modification 9/19/2019
The purpose of this code is to find
all the passwords from 100 users
using only recursion
'''

class Node(object):
   password = ""
   count = -1
   next = None

   def __init__(self, password, count, next):
       self.password = password
       self.count = count
       self.next = next

def main():
    with open("10-million-combos.txt") as file:
        counter = 0
        head = Node("", 1 , None)
        for line in file:
            split_line = line.split('\t')
            for word in split_line:
                if check_recurrence(head, word) == False:
                    tempNode = Node(word, 1, None)
                    tempNode.next = head
                    head = tempNode
                else:
                    counter = counter
                    #need to add one to the count of password also need
                    #to switch what happens when true and false
            counter += 1
    temp = head
    while temp.next != None:
        print(temp.password)
        temp = temp.next

def check_recurrence(head, password):
    temp = head
    while temp.next != None:
        if(temp.password == password):
            return True
    return False

def bubblesort(head):
    temp = head
    first = temp
    second = temp.next
    while temp.next != None:
        while temp.next != None:
            if first.count > second.count:
                temp = first
                first = second
                second = temp
    
    '''
    file1 = open("10-million-combos.txt","r+")
    line = file1.readline()
    head = Node(, None)
    file1.close()
    print(head)
    '''
    
main()