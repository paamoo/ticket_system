
from read_ticket import *
from dokumentation import *


welcome = """
_______________________________________________________________________________________________________________________________
                  WE (Parsa - Rapahel) did what we could, hope u like it... 
_______________________________________________________________________________________________________________________________        
-------------------------------------------------------------------------------------------------------------------------------
                              .       .
                             / `.   .' " 
                     .---.  <    > <    >  .---.
                     |    \  \ - ~ ~ - /  /    |
         _____          ..-~             ~-..-~
        |     |   \~~~\.'                    `./~~~/
       ---------   \__/                        \__/  <---------------- SAE Project
      .'  O    \     /               /       \  " 
     (_____,    `._.'               |         }  \/~~~/
      `----.          /       }     |        /    \__/
            `-.      |       /      |       /      `. ,~~|
                ~-.__|      /_ - ~ ^|      /- _      `..-'   
                     |     /        |     /     ~-.     `-. _  _  _
 O   O                 |_____|        |_____|         ~ - . _ _ _ _ _>
/|\ /|\   <-- (Ich und Raphael)
/ \ / \

just for fun :O but for real :D
-------------------------------------------------------------------------------------------------------------------------------
"""

def main():
    global docu
    file_name = input("Write the name of your File: ")
    if file_name.endswith(".json"):
        print("File name is correct")
        while True:
            print(welcome)
            print("\n\t\tWelcome to the ticket system")
            print("1. View the Tickets")
            print("2. Create a ticket")
            print("3. Documentation")
            print("4. Exit")
            answer = input("What do you want to do? ")
            if answer == "1":
                text = jsonjson()
                list_x = text.read_ticket(file_name)
                for ticket_id, tickets in enumerate(list_x):
                        print(f"============= {ticket_id + 1} Ticket =============\n||")
                        for key, value in tickets.items():
                         print('||', '\t\t', key, ': ', value)
                         print('||')
            elif answer == "2":
                email = input("Write your Email please: ")
                if "@" not in email:
                    print("Please enter a valid Email \n\texample@gmail.com")
                    return main()
                name = input("Name: ")
                lastName = input("Lastname: ")
                description = input("Please descripe the Problem here: ")
                text = jsonjson()
                text.create_ticket(file_name, email, name, lastName, description)
                print("\n\tNew Ticket has been created :-) ")
                print("=====================================")
                another = input(print("Do you want to create another ticket? (y/n)"))
                if another.lower() == "y":
                    return main()
                elif another.lower() == "n":
                    print("Bye")
                    return main()
            elif answer == "3":
                docu()
            elif answer == "4":
                print("Bye")
                return main()
            else:
                print("Please enter a number between 1 and 4")
            return main()
    elif file_name.endswith(".csv"):
        while True:
            print(welcome)
            answer = input("Pleasae choose a Number:  ")
            if answer == "1":
                pass
            elif answer == "2":
                pass
            elif answer == "3":
                pass
            elif answer == "4":
                pass
            elif answer == "5":
                return main()
            else:
                print("Please enter a number between 1 and 5")
    else:
        print('Available Formats: CSV , json! ')
        return main()

if __name__ == "__main__": 
    main()