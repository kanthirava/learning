# declaring student data
student_ids = {'A101','A102','A103'}
student_ids.add('A104')
games = ('cricket','football','basketball','volleyball','chess')

student_info = {
    'A101':{'name':'Teja','branch':'CSE','year':4},
    'A102':{'name':'Vinay','branch':'Mech','year':4},
    'A103':{'name':'Kanthi','branch':'Civil','year':4},
    'A104':{'name':'Nandan','branch':'BSC','year':3}
    }
student_info['A105'] = {'name':'Chaitanya','branch':'BSC','year':3}

sports_subscribed = {
'cricket':{'A101','A102','A103'},
'basketball':{'A101','A102'},
'volleyball':{'A103'}
}

while True:
    get_user_option = input("What do you want to do? ")
    if get_user_option=="p":
        print(student_ids)
        print(student_info)
        # for k,v in student_info.items():
        #     print(v['name'])
    elif get_user_option=="i":    
        get_id = input('Enter student Id: ')
        get_name = input("Enter student Name :")
        get_branch = input("Enter branch : ")
        get_year = input("Enter year : ")
        get_sport = input("Enter sport: ")
        student_ids.add(get_id)
        student_info[get_id] = {'name':get_name,'branch':get_branch,'year':get_year, 'sport': get_sport}
        print(student_info[get_id])
    else:
        break

