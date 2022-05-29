#Python 3.10.4
#import sys
#print(sys.version)

#Sudent Name: Sai Saing Khon Pha
#Studen ID: 10241985

def main():
    swimmer = [{"name": "Sai","gender":"male","age":"20",
                "event":(1500,"Freestyle"),"time":"06.30.00","meet":"SIM 2022","status":"active","post":"posted"},
               {"name":"Claire","gender":"female","age":"18",
                "event":(100,"Butterfly"),"time":"10.20.33","meet":"Olympic 2022","status":"active","post":"posted"}]
    unpostedlist = []
    displayScreen(swimmer)
    #looping menu
    quit = "no"
    while(quit == "no"):
        #Input from the user
        start = int(input("\nPress 1 to Register Swimmer\nPress 2 to Remove swimmer\nPress 3 to Record swimmers' timing\nPress 4 to Enquire swimmer's timing\nPress 5 to post active unposted-swimmers\nPress 6 to view the Table\nPress 7 to end the program\n"))

        #1 For Registration
        if(start == 1 ):
            again = "yes"
            while again == "yes":
                print("-"*8,"REGISTRATION","-"*8)
                name = input('Enter swimmer name ')
                gender = input('Enter Gender (male or female) ')
                dateofBirth = str(input('Enter Date of birth YYYY.MM.DD '))
                age = calculateAge(dateofBirth)
                new_data = {"name":name,"gender":gender,"age":age,"status":"active",
                            "event":(00,"unknown"),"time":"00.00.00","meet":"Unknown","status":"active","post":"posted"}
                swimmer.append(new_data)
                displayScreen(swimmer)
                again = input("\nRegister again?(yes/no) ")
        #2 For Removing swimmer
        if(start ==2):
            print("-"*8,"REMOVING SWEIMMER","-"*8)
            again = "yes"
            while again == "yes":
                name = input('Enter swimmer name (**User must be registered first**)\n ')
                if(checkName(name,swimmer)== True ):
                    for x in swimmer:
                        if x["name"] == name:
                            x["status"] = "inactive"
                            displayScreen(swimmer)
                            again = input("\nRemove swimmer again?(yes/no) ")
                else:
                    print("Swimmer not found")
                    again = input("\nRemove swimmer again?(yes/no) ")

    
        #3 For Recording swimmers'timing
        if(start == 3):
            recordagain=1
            while(recordagain==1):
                print("-"*8,"RECORDING TIMING","-"*8)
                name = input('Enter swimmer name (**Swimmer must be registered first**) \n')
                if(checkName(name,swimmer)== True ):
                    print("Swimmer found")
                    valid = (1,2,3,4,5)
                    event = int(input('Choose Event below\nPress 1 for Freesyle\nPress 2 for Backstroke\nPress 3 for Breakstroke\nPress 4 for Butterfly\nPress 5 for Individual Medley\n'))
                    while event not in valid:
                        print("Invalid selection") 
                        event=int(input("Choose Event below\nPress 1 for Freesyle\nPress 2 for Backstroke\nPress 3 for Breakstroke\nPress 4 for Butterfly\nPress 5 for Individual Medley\n"))
                    event = event_detail(event)
                    time = input('Submit Time in the format 00.00.00 ')
                    meet = input('Submit Meet ')
                    #inserting record in swimmer list
                    n=0
                    while(swimmer[n]["name"] != name):
                        n+=1
                    
                    new_data = swimmer[n].copy()
                    new_data.update({"event":event,"time":time,"meet":meet,"post":"unposted"})
                    swimmer.insert(n,new_data)
                    unpostedlist.append(new_data)
               
                    displayScreen(unpostedlist)
                    recordagain = int(input("\nPress 1 to continue record\nPress 2 to stop recording\n"))
                    
                    
                else:
                    print("Swimmer not found")
                    recordagain = int(input("Press 1 to continue record\nPress 2 to stop recording\n"))
            
        #4 For Enquiring swimmer's timing
        if(start == 4):
            again = "yes"
            while again == "yes":
                print("-"*8,"ENQUIRING TIMING","-"*8)
                option = int(input("Press 1 to enquire with name\nPress 2 to enquire with name and event\n"))
                while option != 1 and option !=2 :
                    option = int(input("Invalid\nPress 1 to enquire with name\nPress 2 to enquire with name and event\n"))
                if ( option == 1):
                    name = input('Enter Name to enquire swim timings\n')
                    exist = False
                    for x in swimmer:
                        if x["name"] == name:
                            exist = True
                    if(exist == True):
                        enquireTiming(name,swimmer)
                    else:
                        print("\nNo user found\n")
                    again = input("\nEnquire again? (yes or no) ")
                    
                else:
                    name = input('Enter Name to enquire swim timings\n')
                    exist = False
                    for x in swimmer:
                        if x["name"] == name:
                            exist = True
                    if(exist == True):
                        meter = validMeter()
                        style = input("Enter style for event details (Freesyle,Backstroke,Breakstroke,Butterfly,Individual Medley) \n")
                        event=(meter,style)
                        enquireTiming2(name,event,swimmer)                       
                    else:
                        print("\nNo user found\n")     
                    
                    again = input("\nEnquire again? (yes or no) ")
                
                
        #5 For posting active swimmers
        if(start == 5):
            print("-"*8,"POSTING STATUS","-"*8)
            displayScreen(unpostedlist)
            check = "yes"
            if(check == input("Do you wanna post the status?(yes/no)")):
                for x in swimmer:
                    x["post"] = "posted"
                unpostedlist.clear()
                displayScreen(swimmer)
            else:
                displayScreen(swimmer)
            
        #6 View table
        if(start == 6):
            displayScreen(swimmer)
        
        #7 End program
        if(start == 7):
            quit = "yes"
            
    #byebye
    print("-"*20,"Bye Bye ! Thanks for running the program （っ＾▿＾）❤","-"*20)
##########################functions#############################

def calculateAge(date):
    space = date.index(".")
    age = 2022 - int(date[:space])
    return age 

#checking resgistered name or not
def checkName(name,swimmer):
    for x in swimmer:
        if(x["name"] == name):
            return True
    
    return False
#This function is asking about event details
def event_detail(event):
    if(event == 1):
        condition = 0
        while(condition == False):
            meter=int(input("Enter 50/100/200/400/800/1500 meters"))
            if (meter==50 or meter==100 or meter==200 or meter==400 or meter==800 or meter == 1500):
                condition = True
            else:
                condition = False
                print("Invaild meter")
        return(meter,"Freestyle")
    if(event == 2):
        condition = 0
        while(condition == False):
            meter=int(input("Enter meters(50m,100m,200m)"))
            if (meter==50 or meter==100 or meter==200 or meter==400 or meter==800 or meter == 1500):
                condition = True
            else:
                condition = False
                print("Invaild meter")
        return(meter,"Backstroke")
    if(event == 3):
        condition = 0
        while(condition == False):
            meter=int(input("Enter meters(50m,100m,200m)"))
            if (meter==50 or meter==100 or meter==200 or meter==400 or meter==800 or meter == 1500):
                condition = True
            else:
                condition = False
                print("Invaild meter")
        return(meter,"Breaststroke")
    if(event == 4):
        condition = 0
        while(condition == False):
            meter=int(input("Enter meters(50m,100m,200m)"))
            if (meter==50 or meter==100 or meter==200 or meter==400 or meter==800 or meter == 1500):
                condition = True
            else:
                condition = False
                print("Invaild meter")
        return(meter,"Butterfly")
    if(event == 5):
        condition = 0
        while(condition == False):
            meter=int(input("Enter meters(100m,200m,400m)"))
            if (meter==50 or meter==100 or meter==200 or meter==400 or meter==800 or meter == 1500):
                condition = True
            else:
                condition = False
                print("Invaild meter")
        return(meter,"Individual Medley")
    
#this function is enquire with name only
def enquireTiming(name,swimmer):
            print('\n',"_"*60,"SWIMMER TABLE LIST","_"*60,'\nName\t\t Gender\t\t Age\t Event\t\t\t Time\t\t Meet\t\t\t Status\t\t\tSubmission\n')
            for x in swimmer:
                if x["name"] == name :
                    print(x["name"],"\t\t ",x["gender"],"\t\t",x["age"],"\t",
                          x["event"],"\t",x["time"],"\t ",x["meet"],"\t\t",x["status"],"\t\t",x["post"])  
       
           
            
#this function is enquire with name and event
def enquireTiming2(name,event,swimmer):
            print('\n',"_"*60,"SWIMMER TABLE LIST","_"*60,'\nName\t\t Gender\t\t Age\t Event\t\t\t Time\t\t Meet\t\t\t Status\t\t\tSubmission\n')
            for x in swimmer:
                if name == x["name"] and event == x["event"]:
                    print(x["name"],"\t\t ",x["gender"],"\t",x["age"],"\t",
                          x["event"],"\t",x["time"],"\t ",x["meet"],"\t\t",x["status"],"\t\t",x["post"])
       
        
#validation meter
def validMeter():
    validmeter = (50,100,200,400,800,1500)
    meter = input("Enter valid meter ")
    while int(meter) not in validmeter:
        meter=input("You have entered invalid meters Please re-enter ")
    return int(meter)
          
            
def displayScreen(swimmer):
    print('\n',"_"*60,"SWIMMER TABLE LIST","_"*60,'\nName\t\t Gender\t\t Age\t Event\t\t\t Time\t\t Meet\t\t\t Status\t\t\tSubmission\n')
    for x in swimmer:
        if(x["gender"] == "male" ):
            print(x["name"],"\t\t ",x["gender"],"\t\t",x["age"],"\t",
                  x["event"],"\t",x["time"],"\t ",x["meet"],"\t\t",x["status"],"\t\t",x["post"])
        else:
            print(x["name"],"\t\t ",x["gender"],"\t",x["age"],"\t",
                  x["event"],"\t",x["time"],"\t ",x["meet"],"\t\t",x["status"],"\t\t",x["post"]) 
     
     
main()
    
    
    

    
    




