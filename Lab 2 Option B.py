'''
10-million-combos
New Text Document.txt

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
   count = 0
   next = None

   def __init__(self, password, count, next):
       self.password = password
       self.count = count
       self.next = next

def main():
    with open("10-million-combos.txt") as file:
        head = Node('', 0, None)
        for line in file:
            split_line = line.split('\t')
            for word in split_line:
                if check_recurrence(head, word):
                    find_word(head, word)
                else:
                    tempNode = Node(word, 1, None)
                    tempNode.next = head
                    head = tempNode
    temp = head
    print('start bubble sort')
    bubblesort(temp)
    counter = 0
    while temp != None:
        print(temp.password)
        print(str(temp.count))
        temp = temp.next
        counter += 1
    with open("10-million-combos.txt") as file:
        sorted_dict = {}
        head = Node('', 0, None)
        for line in file:
            split_line = line.split('\t')
            for word in split_line:
                if word in sorted_dict:
                    sorted_dict[word] = sorted_dict[word] + 1
                else:
                    sorted_dict[word] = 1
                    tempNode = Node(word, 1, None)
                    tempNode.next = head
                    head = tempNode
    print(sorted_dict)
    temp = head
    print('start merge sort')
    mergesort(temp)
    
        
def find_word(head, password):
    temp = head
    while temp != None:
        if(temp.password == password):
            temp.count += 1
        temp = temp.next

def check_recurrence(head, password):
    temp = head
    while temp != None:
        if(temp.password == password):
            return True
        temp = temp.next
    return False
        
def bubblesort(head):
    first = head
    while first != None:
        second = first.next
        while second != None:
            if first.count < second.count:
                tempcount = first.count
                temppassword = first.password
                first.count = second.count
                first.password = second.password
                second.count = tempcount
                second.password = temppassword
            second = second.next
        first = first.next
    
main()