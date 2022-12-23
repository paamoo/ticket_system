import main
doku = """
______      _                               _        _   _             
|  _  \    | |                             | |      | | (_)            
| | | |___ | | ___   _ _ __ ___   ___ _ __ | |_ __ _| |_ _  ___  _ __  
| | | / _ \| |/ / | | | '_ ` _ \ / _ \ '_ \| __/ _` | __| |/ _ \| '_ \ 
| |/ / (_) |   <| |_| | | | | | |  __/ | | | || (_| | |_| | (_) | | | |
|___/ \___/|_|\_\\__,_|_| |_| |_|\___|_| |_|\__\__,_|\__|_|\___/|_| |_|
                                                                       
"""

def docu():
    global doku
    print(doku)
    doku_welcome = input("Welcome to the Documentation of the Ticket System\n\n[Enter]  For reading the Documentation please Enter\n\n[Q]  For Quitting the Documentation please Enter 'q'\n:")
    while True:
        if doku_welcome.lower() == "q" or "Q":
           return main.main()   
        elif doku_welcome == "":
            print("You pressed Enter")
        else:
            print("Please enter a valid doc")
            return docu()
    
