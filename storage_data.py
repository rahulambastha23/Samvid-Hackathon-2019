#CLASS A
timeTable_4A = [
    ['Day', 'Lecture 1', 'Lecture 2', 'Lecture 3', 'Lecture 4', '', 'Lecture 5', 'Lecture 6', 'Lecture 7'],
    ['MON', 'DS', 'DS', 'CSA', 'OOPS', 'B', 'OS', 'CM', 'DMS'],
    ['TUE', 'CSA', 'OOPS', 'H/W LAB', 'H/W LAB', 'R', 'OS', 'DMS', 'CM'],
    ['WED', 'OOPS', 'OS', 'OOPS LAB', 'OOPS LAB', 'E', 'DS', 'DMS', 'CSA'],
    ['THU', 'OS', 'OOPS', 'DMS', 'DS', 'A', 'CM', 'DS LAB', 'DS LAB'],
    ['FRI', 'DMS', 'CSA', 'CM', 'DS', 'K', 'OOPS', 'GUI LAB', 'GUI LAB'],
]
subjectwise_faculty_4A = {"CSA":"Aakanksha Choubey","DS":"Samta Gajbhiye","DMS":"Manjula Swarnakar","OS":"Megha Mishra","CM":"K.K. Pandey","OOPS":"Rajesh Tiwari", "H/W LAB":"Aakanksha Choubey", "GUI LAB":"Vishnu Mishra", "OOPS LAB":"Rajesh Tiwari"}

#CLASS B
timeTable_4B = [
    ['Day', 'Lecture 1', 'Lecture 2', 'Lecture 3', 'Lecture 4', '', 'Lecture 5', 'Lecture 6', 'Lecture 7'],
    ['MON', 'DM', 'OS', 'OOPS LAB', 'OOPS LAB', 'B', 'CM', 'OOPS', 'CSA'],
    ['TUE', 'OS', 'DM', 'DS', 'CSA', 'R', 'OOPS', 'GUI LAB', 'GUI LAB'],
    ['WED', 'OOPS', 'CM', 'OS', 'DM', 'E', 'DS', 'DS LAB', 'DS LAB'],
    ['THU', 'DS', 'CSA', 'H/W LAB', 'H/W LAB', 'A', 'OS', 'CM', 'OOPS'],
    ['FRI', 'CM', 'OS', 'OOPS', 'CSA', 'K', 'DM', 'DS', 'DS'],
]

subjectwise_faculty_4B = {"OOPS":"Abhishek Dewangan","OS":"Megha Mishra", "CM":"K.K. Pandey", "DMS":"Yogesh Sahu", "DS":"Yamini Chouchan", "CSA":"Kamal Mehta", "H/W LAB":"Kamal Mehta", "GUI LAB":"Vishnu Mishra", "OOPS LAB":"Abhishek Dewangan"}

#CLASS C
timeTable_4C = [
    ['Day', 'Lecture 1', 'Lecture 2', 'Lecture 3', 'Lecture 4', '', 'Lecture 5', 'Lecture 6', 'Lecture 7'],
    ['MON', 'DS', 'DS', 'DMS', 'CMS', 'B', 'OOPS', 'H/W LAB', 'H/W LAB'],
    ['TUE', 'CM', 'CSA', 'DS LAB', 'DS LAB', 'R', 'DM', 'OOPS', 'OS'],
    ['WED', 'CSA', 'OOPS', 'DS', 'DS', 'E', 'OS', 'DM', 'CM'],
    ['THU', 'OOPS', 'CSA', 'DM', 'CM', 'A', 'OS', 'DS', 'DS'],
    ['FRI', 'OS', 'OOPS', 'OOPS LAB', 'OOPS LAB', 'K', 'CSA', 'CM', 'DM'],
]

#2nd page
def display(tt):
    for i in range(0, 6):
        for j in range(0, 9):
            print('{:^18}'.format(tt[i][j]), end = "")
        print("\n")
    print("\n\n\n")

def secondpage():

    section=input()
    if section=='A':
        display(timeTable_4A)
    elif(section=='B'):
        display(timeTable_4B)
    else:
        display(timeTable_4C)

def access(tt,day):
    for i in  tt:
        if tt[i][0]==day:
            temp=tt[i][0:]         #that particular days tt
            print (temp)
            break
     for j in temp:
         if j==

secondpage()