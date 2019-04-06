from datetime import datetime
from datetime import date
from datetime import time


class Database:
    entries = []

    def add(self,todo):
        self.entries.append(todo)

    def remove(self,todo):
        pass

    def update(self,oldtodo,newoldtodo):
        index = self.entries.index(oldtodo)
        self.entries[index] = newoldtodo

    def remove(self,todo):
        self.entries.remove(todo)

    def getAll(self):
        return self.entries

class Todo:
    def __init__(self,text):
        self.text = text
        self.date = datetime.now

    def __str__(self):
        return "Date: "+ str(self.date)+"\nTo do: "+self.text

class Manager:
    def __init__(self,database):
        self.database = database

    def add(self,todo):
        self.database.add(todo)

    def update(self,oldtodo,newtodo):
        self.database.update(oldtodo,newtodo)

    def __delete__(self, todo):
        self.database.remove(todo)

    def showAll(self):
        entries = self.database.getAll()
        for item in entries:
            print("-"*24+str(entries.index(item)+1)+"-"*24)
            print(item)
            print("-"*50)

    def getAll(self):
        return self.database.getAll()


def menu():
    choice = None
    database = Database()
    manager = Manager(database)
    while choice!='q':
        print("To Do list Menu")
        print("a) Add")
        print("b) Edit")
        print("c) Delete")
        print("d) Show All")
        print("q) Quit")
        choice = input("Action: ")

        if choice == 'a':
            text = input("To do: ")
            todo = Todo(text)
            manager.add(todo)

        elif choice == 'b':
            manager.showAll()
            try:
                entries =  manager.getAll()
                if len(entries) > 0:
                    index = int(input("Enter the index number for edit: "))
                    oldtodo = entries[index-1]
                    text = input("To do: ")
                    newtodo = Todo(text)
                    manager.update(oldtodo,newtodo)
            except:
                print("Invalid Input")
        elif choice == 'c':
            manager.showAll()
            try:
                entries = manager.getAll()
                if len(entries) > 0:
                    index = int(input("Enter the index number for delete: "))
                    todo = entries[index-1]
                    manager.delete(todo)
            except:
                print("Invalid Input")
        elif choice == 'd':
            manager.showAll()


        else:
            pass

menu()