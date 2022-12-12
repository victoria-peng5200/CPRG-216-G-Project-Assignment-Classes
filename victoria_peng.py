# # Name: VICTORIA PENG
#Student ID: 000677647
# Course: CPRG-216-G
# Date: Dec 11, 2022
# Assignment: Project Classes

#***********************************************************************************************************************
# Class #2 Facility
class Facility:
    def __init__(self):
        self.info=[]
        with open ("facilities.txt","r") as rf:
            lines=rf.readlines()
            for line in lines:
                self.info.append(line.split("\n")[0])
        pass

    def addFacility(self,name): #Adds and writes the facility name to the file
        self.info.append(name)
        pass

    def displayFacilities(self): #Displays the list of facilities
        for i in self.info:
            print(i+'\n')
        print('Back to the previous Menu')
        pass

    def writeListOffacilitiesToFile(self): #Writes the facilities list to facilities.txt
        with open("facilities.txt", "w") as file:
            for i in self.info:
                file.write(i+"\n")
        pass


# Class #2 Facility user input loop
def facilities():
    facility=Facility()
    while True:
        nav = input("Facilities Menu:\n1 - Display Facilities list\n2 - Add Facility\n3 - Back to the Main Menu\n"+'\n')
        if nav == "1":
            facility.displayFacilities()
        elif nav == "2":
            new_facility = input("Enter Facility name:\n"+'\n')
            facility.addFacility(new_facility)
            facility.writeListOffacilitiesToFile()
            print('\nBack to previous Menu')
        elif nav == "3":
            break
        else:
            print('\nYou input a wrong number. Please try it again.\n')
            print('\nBack to the previous Menu\n')
            break

#***********************************************************************************************************************
# Class #3: Laboratory
class Laboratory:
    def __init__(self):
        pass

    def addLabToFile(self,format_Laboratory): #Adds and writes the lab name to the file in the format of the data that is in the file
        with open('laboratories.txt','w') as wf:
            wf.write(format_Laboratory)
        pass

    def writeListOfLabsToFile(self,format_Laboratory): #Writes the list of labs into the file laboratories.txt
        with open('laboratories.txt','w') as wf:
            wf.write(format_Laboratory)
        pass

    def displayLabsList(self,Laboratories): #Displays the list of laboratories
        for Lab in Laboratories:
            print("{}{}{}".format(Lab[0], " " * 10, Lab[1])+'\n')
        print('Back to the previous Menu')
        pass

    def formatLabInfo(self,Laboratories): #Formats the Laboratory object similar to the laboratories.txt file
        format_Laboratory=''
        for Laboratory in Laboratories:
            Laboratory=Laboratory[0]+'_'+Laboratory[1]+'\n'
            format_Laboratory+=Laboratory
        return format_Laboratory

    def enterLaboratoryInfo(self,Laboratories): #Asks the user to enter lab name and cost and forms a Laboratory object
        self.name=input("Enter Laboratory facility:\n"+'\n')
        self.cost=input("Enter Laboratory cost:\n"+'\n')
        new_lab=[self.name,self.cost]
        Laboratories.append(new_lab)
        return Laboratories

    def readLaboratoriesFile(self):#Reads the laboratories.txt file and fills its contents in a list of Laboratory objects
        Laboratories=[]
        with open ('laboratories.txt','r') as rf:
            for row in rf:
                row = row.rstrip('\n')
                row=row.split('_')
                Laboratories.append(row)
        return Laboratories


# Class #3: Laboratory user input loop
def laboratories():
    lab=Laboratory()
    while True:
        nav = input("Laboratories Menu:\n1 - Display laboratories list\n2 - Add laboratory\n3 - Back to the Main Menu\n"+"\n")
        if nav == "1":
            Laboratories=lab.readLaboratoriesFile()
            lab.displayLabsList(Laboratories)
        elif nav == "2":
            Laboratories=lab.readLaboratoriesFile()
            Laboratories=lab.enterLaboratoryInfo(Laboratories)
            format_Laboratory=lab.formatLabInfo(Laboratories)
            lab.addLabToFile(format_Laboratory)
            print('\nBack to previous Menu')
        elif nav == "3":
            break
        else:
            print('\nYou input a wrong number. Please try it again.\n')
            print('\nBack to the previous Menu')
            break

#***********************************************************************************************************************
#Back to main option loop
while True:
    print('Welcome to Alberta Hospital (AH) Management system')
    b=input("Select from the following options, or select 0 to stop: \n1 - 	Doctors \n2 - 	Facilities \n3 - 	Laboratories \n4 - 	Patients\n"+'\n')
    if b=='2':
            facilities()
    elif b=='3':
            laboratories()
    elif b=='0':
        break