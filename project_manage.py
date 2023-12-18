from database import DB, Table
from datetime import date
import csv
import random


# define a funcion called initializing

def initializing():
    global my_DB
    person = Table()
    persons = person.insert_by_csv('persons.csv', 'persons')
    login_t = Table()
    logins = login_t.insert_by_csv('login.csv', 'login')
    project = Table()
    projects = project.insert_by_csv('project.csv', 'project')
    advisor_pending = Table()
    advisor_pending_table = advisor_pending.insert_by_csv('advisor_pending_table.csv', 'advisor_pending_table')
    member_pending = Table()
    member_pending_request = member_pending.insert_by_csv('member_pending_request.csv', 'member_pending_request')
    my_DB = DB()
    my_DB.insert(persons)
    my_DB.insert(logins)
    my_DB.insert(projects)
    my_DB.insert(advisor_pending_table)
    my_DB.insert(member_pending_request)


# here are things to do in this function:

# create an object to read all csv files that will serve as a persistent state for this program

# create all the corresponding tables for those csv files

# see the guide how many tables are needed

# add all these tables to the database


# define a funcion called login

def login():
    # here are things to do in this function:
    # add code that performs a login task
    # ask a user for a username and password
    # returns [ID, role] if valid, otherwise returning None

    login_info = my_DB.search('login')
    username = input('username: ')
    password = input('password: ')
    for ele in login_info.table:
        if ele['username'] == username and ele['password'] == password:
            return [ele['ID'], ele['role']]
    return None


# define a function called exit
def exit():
    # here are things to do in this function:
    # write out all the tables that have been modified to the corresponding csv files
    # By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:

    # https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python

    person_f = open('persons.csv', 'w')
    login_f = open('login.csv', 'w')
    project_f = open('project.csv', 'w')
    ad_pending = open('advisor_pending_table.csv', 'w')
    mem_pend_re = open('member_pending_request.csv', 'w')

    writer_1 = csv.DictWriter(person_f, fieldnames=['ID', 'first', 'last', 'type'])
    writer_1.writeheader()
    writer_1.writerows(my_DB.search('persons').table)
    person_f.close()

    writer_2 = csv.DictWriter(login_f, fieldnames=['ID', 'username', 'password', 'role'])
    writer_2.writeheader()
    writer_2.writerows(my_DB.search('login').table)
    login_f.close()

    writer_3 = csv.DictWriter(project_f,
                              fieldnames=['projectID', 'title', 'lead', 'member1', 'member2', 'advisor', 'status'])
    writer_3.writeheader()
    writer_3.writerows(my_DB.search('project').table)
    project_f.close()

    writer_4 = csv.DictWriter(ad_pending, fieldnames=['projectID', 'to_be_advisor', 'response', 'response_date'])
    writer_4.writeheader()
    writer_4.writerows(my_DB.search('advisor_pending_table').table)
    ad_pending.close()

    writer_5 = csv.DictWriter(mem_pend_re, fieldnames=['projectID', 'to_be_member', 'response', 'response_date'])
    writer_5.writeheader()
    writer_5.writerows(my_DB.search('member_pending_request').table)
    mem_pend_re.close()

    quit()



# make calls to the initializing and login functions defined above

initializing()
val = login()
# print(my_DB.search('project'))

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

if val[1] == 'admin':
    print("Enter the number of a task you want to do.")
    print("1: update the tables")
    print("2: exit")
    choice = input("Which task would you choose?: ")
    while choice != '2':
        if choice == '1':
            name = input("Which table would you want to update?(name of that table): ")
            tb = my_DB.search(name)
            # keys = tb.key
            # print('key:', keys)
            # print('tb: ', tb.table)
            safe = input("Key: ")
            try:
                ind = tb.key[safe]
            except KeyError:
                print("Key is incorrect")
            for key, ele in tb.table[ind].items():
                new = input(f"Input new {key}: ")
                tb.table[ind][key] = new
        print("Updates an information successful")
        # print(tb.table)
        print("Enter the number of a task you want to do.")
        print("1: update the tables")
        print("2: exit")
        choice = input("Which task would you choose?: ")

    # see and do admin related activities
elif val[1] == 'student':
    # see and do student related activities
    print("Enter the number of a task you want to do.")
    print("1: see pending requests")
    print("2: create a project")
    print("3: exit")
    choice = input("Which task would you choose?: ")
    while choice != '3':
        tb = my_DB.search('member_pending_request')
        project_tb = my_DB.search('project')
        lg = my_DB.search('login')
        pr = my_DB.search('persons')
        # print('project right now ', project_tb.table)
        if choice == '1':
            print("--Request--")
            for var in tb.table:
                if var['to_be_member'] == val[0] and var['response'] != 'no':
                    print('projectID: ', var['projectID'])
                    response = input("Your response(answer 'yes' or 'no'): ")
                    if response == 'yes':
                        for pj in project_tb.table:
                            if pj['projectID'] == var['projectID']:
                                if len(pj['member1']) == 0 and pj['lead'] != val[0]:
                                    pj['member1'] = val[0]
                                    var['response'] = response
                                    response_date = date.today()
                                    var['response_date'] = str(response_date)
                                    for log in lg.table:
                                        if log['ID'] == val[0]:
                                            log['role'] = 'member'
                                            print("Accept a member request successfully")
                                            break
                                    for p in pr.table:
                                        if p['ID'] == val[0]:
                                            p['type'] = 'member'
                                            break
                                elif len(pj['member2']) == 0 and pj['lead'] != val[0]:
                                    var['response'] = response
                                    response_date = date.today()
                                    var['response_date'] = str(response_date)
                                    pj['member2'] = val[0]
                                    pj['status'] = 'ready to solicit an advisor'
                                    for log in lg.table:
                                        if log['ID'] == val[0]:
                                            log['role'] = 'member'
                                            print("Accept a member request successfully")
                                            break
                                    for p in pr.table:
                                        if p['ID'] == val[0]:
                                            p['type'] = 'member'
                                            break
                                exit()
                    if response == 'no':
                        print("Deny a member request successfully")
                        print()
                        var['response'] = response
                        response_date = date.today()
                        var['response_date'] = str(response_date)
                        exit()
        if choice == '2':
            check = 1
            for att in project_tb.table:
                if att['member1'] == val[0] or att['member2'] == val[0]:
                    print("You can't create a project")
                    check = 0
                    break
            if check:
                print("Create a project")
                pr_id = str(random.randint(100000, 999999))
                title = input("Title: ")
                lead = val[0]
                mem1 = ''
                mem2 = ''
                ad = ''
                status = 'pending member'
                project_tb.table.append({'projectID': pr_id, 'title': title, 'lead': lead, 'member1': mem1, 'member2': mem2, 'advisor': ad, 'status': status})
                for log in lg.table:
                    if log['ID'] == val[0]:
                        log['role'] = 'lead'
                        break
                for p in pr.table:
                    if p['ID'] == val[0]:
                        p['type'] = 'lead'
                        break
                req_mem = input("Which student you want to invite?(answer their id) or 'exit': ")
                while req_mem != 'exit':
                    tb.table.append({'projectID': pr_id, 'to_be_member': req_mem, 'response': '', 'response_date': ''})
                    req_mem = input("Which student you want to invite?(answer their id or 'exit'): ")
                exit()
        print("Enter the number of a task you want to do.")
        print("1: see pending requests")
        print("2: create a project")
        print("3: exit")
        choice = input("Which task would you choose?: ")

elif val[1] == 'member':
    print("Enter the number of a task you want to do.")
    print("1: see or modify a project")
    print("2: exit")
    choice = input("Which task would you choose?: ")
    while choice != '2':
        print('--Project information--')
        project_tb = my_DB.search('project')
        for pj in project_tb.table:
            if pj['member1'] == val[0] or pj['member2'] == val[0]:
                print("ProjectID:", pj['projectID'])
                print("Title:", pj['title'])
                print("Lead:", pj['lead'])
                print("Member1:", pj['member1'])
                print("Member2:", pj['member2'])
                print("Advisor:", pj['advisor'])
                print("Status:", pj['status'])
                print()
                modify = input("Do you want to modify?(answer 'yes' or 'no'): ")
                if modify == 'yes':
                    print("--Modify--")
                    new_title = input("New Title: ")
                    pj['title'] = new_title
                break
        print("Enter the number of a task you want to do.")
        print("1: see or modify a project")
        print("2: exit")
        choice = input("Which task would you choose?: ")
    # see and do member related activities
elif val[1] == 'lead':
    print("Enter the number of a task you want to do.")
    print("1: see or modify a project")
    print("2: send out request to student")
    print("3: send out request to professor")
    print("4: exit")
    choice = input("Which task would you choose?: ")
    while choice != '4':
        if choice == '1':
            print('--Project information--')
            project_tb = my_DB.search('project')
            for pj in project_tb.table:
                if pj['lead'] == val[0]:
                    print("ProjectID:", pj['projectID'])
                    print("Title:", pj['title'])
                    print("Lead:", pj['lead'])
                    print("Member1:", pj['member1'])
                    print("Member2:", pj['member2'])
                    print("Advisor:", pj['advisor'])
                    print("Status:", pj['status'])
                    print()
                    modify = input("Do you want to modify?(answer 'yes' or 'no'): ")
                    if modify == 'yes':
                        print("--Modify--")
                        choose = input("What do you want to modify?: ")
                        if choose == 'title':
                            new_title = input("New Title: ")
                            pj['title'] = new_title
                        elif choose == 'submit' and len(pj['advisor']) != 0:
                            pj['status'] = 'submitted'
                        elif choose == 'submit' and len(pj['advisor']) == 0:
                            raise ValueError("You should have an advisor first")
                        else:
                            raise ValueError("You should select 'submit' or 'title'")
                    break
        if choice == '2':
            req_mem = input("Which student you want to invite?(answer their id) or 'exit': ")
            tb = my_DB.search('member_pending_request')
            project_tb = my_DB.search('project')
            for pj in project_tb.table:
                if pj['lead'] == val[0]:
                    pr_id = pj['projectID']
                    break
            while req_mem != 'exit':
                tb.table.append({'projectID': pr_id, 'to_be_member': req_mem, 'response': '', 'response_date': ''})
                req_mem = input("Which student you want to invite?(answer their id) or 'exit': ")
        if choice == '3':
            pr = my_DB.search('persons')
            ad = my_DB.search('advisor_pending_table')
            project_tb = my_DB.search('project')
            c = 1
            for pj in project_tb.table:
                if pj['lead'] == val[0] and (len(pj['member1']) == 0 or len(pj['member2']) ==0):
                    c = 0
                    print("You cannot have an advisor right now")
                    break
            if c:
                req_ad = input("Which professor you want to invite?(answer their id) or 'exit': ")
                for pj in project_tb.table:
                    if pj['lead'] == val[0]:
                        pr_id = pj['projectID']
                        break
                while req_ad != 'exit':
                    ad.table.append({'projectID': pr_id, 'to_be_advisor': req_ad, 'response': '', 'response_date': ''})
                    req_ad = input("Which professor you want to invite?(answer their id) or 'exit': ")
        print("Enter the number of a task you want to do.")
        print("1: see or modify a project")
        print("2: send out request to student")
        print("3: send out request to professor")
        print("4: exit")
        choice = input("Which task would you choose?: ")

# see and do lead related activities
elif val[1] == 'faculty':
    print("Enter the number of a task you want to do.")
    print("1: see all project")
    print("2: response to the pending requests")
    print("3: evaluate the project")
    print("4: exit")
    choice = input("Which task would you choose?: ")
    while choice != '4':
        project_tb = my_DB.search('project')
        advisor_tb = my_DB.search('advisor_pending_table')
        lg = my_DB.search('login')
        pr = my_DB.search('persons')
        if choice == '1':
            for pj in project_tb.table:
                print("ProjectID:", pj['projectID'])
                print("Title:", pj['title'])
                print("Lead:", pj['lead'])
                print("Member1:", pj['member1'])
                print("Member2:", pj['member2'])
                print("Advisor:", pj['advisor'])
                print("Status:", pj['status'])
                print()
        if choice == '2':
            print("--Request--")
            for var in advisor_tb.table:
                if var['to_be_advisor'] == val[0] and var['response'] != 'no':
                    print('projectID: ', var['projectID'])
                    response = input("Your response(answer 'yes' or 'no'): ")
                    if response == 'yes':
                        for pj in project_tb.table:
                            if pj['projectID'] == var['projectID']:
                                if len(pj['advisor']) == 0:
                                    pj['advisor'] = val[0]
                                    pj['status'] = 'can submit'
                                    var['response'] = response
                                    response_date = date.today()
                                    var['response_date'] = str(response_date)
                                    for log in lg.table:
                                        if log['ID'] == val[0]:
                                            log['role'] = 'advisor'
                                            print("Accept an advisor request successfully")
                                            break
                                    for p in pr.table:
                                        if p['ID'] == val[0]:
                                            p['type'] = 'advisor'
                                            break
                                    exit()
                                else:
                                    print("This project already have an advisor")
                                break
                    if response == 'no':
                        var['response'] = response
                        response_date = date.today()
                        var['response_date'] = str(response_date)
                        print("Deny an advisor request successfully")
                        print()
                        exit()
                break
        if choice == '3':
            project_tb = my_DB.search('project')
            for pj in project_tb.table:
                if pj['status'] == 'approved':
                    correct = input("Evaluate the project?(answer 'yes' or 'no'): ")
                    if correct == 'yes':
                        pj['status'] = ' faculty evaluated'
                    elif correct == 'no':
                        comment = input("Comment: ")
                        pj['status'] = 'comment: ' + comment
        print("Enter the number of a task you want to do.")
        print("1: see all project")
        print("2: response to the pending requests")
        print("3: evaluate the project")
        print("4: exit")
        choice = input("Which task would you choose?: ")



# see and do faculty related activities
elif val[1] == 'advisor':
    print("Enter the number of a task you want to do.")
    print("1: evaluate the project")
    print("2: approve the project")
    print("3: exit")
    choice = input("Which task would you choose?: ")
    while choice != '3':
        project_tb = my_DB.search('project')
        if choice == '1':
            for pj in project_tb.table:
                if pj['status'] == 'submitted' and pj['advisor'] == val[0]:
                    correct = input("Is the project ready to be sent to faculty?(answer 'yes' or 'no'): ")
                    if correct == 'yes':
                        pj['status'] = 'evaluated'
                    elif correct == 'no':
                        comment = input("Comment: ")
                        pj['status'] = 'comment: ' + comment
        if choice == '2':
            for pj in project_tb.table:
                if pj['status'] == 'evaluated':
                    prove = input("Do you want to approve?(answer 'yes' or 'no'): ")
                    if prove == 'yes':
                        pj['status'] = 'approved'
                    elif prove == 'no':
                        pj['status'] = 'disapproved'
        print("Enter the number of a task you want to do.")
        print("1: see all project")
        print("2: response to the pending requests")
        print("3: exit")
        choice = input("Which task would you choose?: ")

# see and do advisor related activities

# once everything is done, make a call to the exit function
exit()
