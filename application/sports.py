#list of sports and sports scubscribed
def sportsdata(s=0):
    print("Sports available are Cricket,Volley ball, Basket ball, Badminton and Football")
    print("If u want to add then enter 'add' (or) If u want to Search student sports details then enter 'search' ")
    enter= input('Please enter: ')
    if(enter== "add"):
        student_sports_id= input('Enter Student ID: ')
        subscribe_to_sport= input('Enter Sports name: ')
    elif (enter=="search"):
        student_id=('Enter Student ID: ')
sportsdata(s=9)