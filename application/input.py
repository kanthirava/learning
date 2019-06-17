print("If u want to search student details enter 'search' (or) if u want to add enter 'add'")
a = input("Please enter: ")
if (a =="add"):
    add_branch = input('Enter branch: ')
    print(" please select the about")
    if(add_branch=="mec"):
        add_year = int(input("Enter year :"))
        if(add_year==1):
            add_id="12L31A03"
            x=input("enter id:")
            add_id = add_id + x
            print(add_id)
            add_name = input("Enter name : ")
        elif(add_year==2):
            add_id = input("Enter id : ")
            add_name = input("Enter name : ")
        elif(add_year==3):
            add_id = input("Enter id : ")
            add_name = input("Enter name : ")
        elif(add_year==4):
            add_id = input("Enter id : ")
            add_name = input("Enter name : ")
        else:
            print("please enter a valid year")
    elif(add_branch=="eee"):
        add_year = input("Enter year :")
        if(add_year==1):
            add_id = input("Enter id : ")
            add_name = input("Enter name : ")
        elif(add_year==2):
            add_id = input("Enter id : ")
            add_name = input("Enter name : ")
        elif(add_year==3):
            add_id = input("Enter id : ")
            add_name = input("Enter name : ")
        elif(add_year==4):
            add_id = input("Enter id : ")
            add_name = input("Enter name : ")
        else:
            print("please enter a valid year")
    elif(add_branch=="cse"):
        add_year = input("Enter year :")
        if(add_year==1):
            add_id = input("Enter id : ")
            add_name = input("Enter name : ")
        elif(add_year==2):
            add_id = input("Enter id : ")
            add_name = input("Enter name : ")
        elif(add_year==3):
            add_id = input("Enter id : ")
            add_name = input("Enter name : ")
        elif(add_year==4):
            add_id = input("Enter id : ")
            add_name = input("Enter name : ")
        else:
            print("please enter a valid year")
    elif(add_branch=="it"):
        add_year = input("Enter year :")
        if(add_year==1):
            add_id = input("Enter id : ")
            add_name = input("Enter name : ")
        elif(add_year==2):
            add_id = input("Enter id : ")
            add_name = input("Enter name : ")
        elif(add_year==3):
            add_id = input("Enter id : ")
            add_name = input("Enter name : ")
        elif(add_year==4):
            add_id = input("Enter id : ")
            add_name = input("Enter name : ")
        else:
            print("please enter a valid year")
    else:
        print("please enter a valid branch")
            
    #add_year = input("Enter year :")
    #add_id = input("Enter id : ")
    #add_name = input("Enter name : ")
    #sid.add(add_branch)
    #sinfo[add_branch] = {'year':add_year,'id':add_id,'name':add_name}
    #print(sinfo[add_branch])
elif(a == "search"):
    print("please search student deatils")
    search_id = input("Enter student ID: ")
else:
    print("please enter either search (or) add ")