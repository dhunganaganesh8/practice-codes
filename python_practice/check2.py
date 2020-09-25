class Roommates():
    def __init__(self, name, roll, contact):
        self.name = name
        self.roll = roll
        self.contact = contact
    def display(self):
        print(self.name,'\t',self.roll,'\t',self.contact)
    
first = []
#for i in range(1,3):
 #   first.append(Roommates(input('Enter name'+str(i)), input('Enter roll for' + str(i)), input('Enter contact')))
#print('Name\t\tRoll\t\tContact')
#for j in range(0,2):
 #   first[j].display()
#print(len(first))
class Old():
    def mate(self, Name, Roll, Contact):
        self.name = Name
        self.roll = Roll
        self.contact = Contact
    def display(self):
        print(self.name, self.roll, self.contact)
class New(Roommates, Old):
    pass

person1 = New.mate('Ganesh', '075aer014', 9860919991)
New.mate()