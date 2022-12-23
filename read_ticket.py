from datetime import date
from random import randint as rd
today = date.today()

class jsonjson:

    # Das ist eine Methode, damit das Jsonfile in eine Liste konvertiert wird, um später diese Liste bearbeiten zu können
    def read_ticket(self, file_Name): # file_Name ist der Name der Jsonfile
        test = open(file_Name, 'r')
        text = test.readlines() 
        list_tx = []
        i = 2
        while i < len(text):
            list_tx.append(text[i:i + 6]) # i ist der Index und i+6 ist die Stelle auf der die Liste aufhört
            i += 8  
        list_x = []
        for i in list_tx:
            listname = {}
            for j, l in enumerate(i): # l ist der Wert und j ist der Index # i ist eine Liste #enumerate gibt die Index und den Wert zurück
                list = []
                txt = l.strip('\t\n," ')
                bakhsh = txt.split(':')
                for k, v in enumerate(bakhsh):   # v ist der Wert und k ist der Index # bakhsh ist eine Liste # txt ist ein String
                    txt = v.strip('" ')
                    list.append(txt)
                if j == 0:
                    listname["ID"] = v
                elif j == 1:
                    listname["Title"] = v
                elif j == 2:
                    listname["name"] = v
                elif j == 3:
                    listname["lastname"] = v
                elif j == 4:
                    listname["Problem"] = v
            list_x.append(listname)
        test.close()
        return list_x   # List_x ist eine Liste und in Liste liegt jede Ticket als Wörterbuch(dictionary)

    def create_ticket(self,file_Name, email, name, lastName, description):
        with open(file_Name, 'r') as read:
            liste = read.readlines()
            read.close()
            # Das ist eine Liste, die die neuen Werte enthält # die Werte werden in die Liste eingetragen # die Liste wird in die Jsonfile geschrieben
            nemidonam = ['\t{\n', '\t\t"ID": 'f'{rd(0, 100)},\n', '\t\t"Email": "'f'{email}",\n', '\t\t"Name": "'f'{name}",\n',
                      '\t\t"lastname": "'f'{lastName}",\n', '\t\t"Problem": "'f'{description}",\n', '\t\t"Date": "'f'{today.strftime("%d/%m/%Y")}"\n', '\t},\n']
            for i in nemidonam:
                liste.insert(len(liste)-1, i)
            with open(file_Name, 'w') as wr:
                for i in liste:
                    wr.writelines(i)
                wr.close()
    
    """ def import_ticket(self, liste, filename):
            with open(filename, 'r') as read:
                ticket_list = filename.readlines()
                filename.close()
                for i in liste:
                    ticket_list.insert(len(ticket_list)-1, i)
                with open(filename, 'w') as wr:
                    for i in ticket_list:
                        wr.writelines(i)
                    wr.close() """
