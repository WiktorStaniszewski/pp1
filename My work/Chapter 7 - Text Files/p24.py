'''
with open("studentslist.txt",'w') as kfc:
    kfc.write("first_name,last_name,age,gender,email\nDecca,Blackstone,52,Male,dblackstone0@time.com\nElena,Rechert,27,Female,erechert1@ucoz.com\nBibbye,Norree,26,Female,bnorree2@reddit.com\nAlasdair,McCoole,53,Male,amccoole3@foxnews.com\nHogan,Hatrey,26,Male,hhatrey4@zimbio.com")
'''
'''
import csv
with open("studentslist.txt",'r') as kfc:
'''

import csv

def display_students_under_30(file_path):
    with open(file_path,'r') as file:
        reader = csv.DictReader(file)
        
        print("{:<10} {:<10} {:<10}".format("First Name", "Last Name", "Email"))
        print("="*40)
        
        for row in reader:
            if int(row['age']) < 30:
                print("{:<10} {:<10} {:<20}".format(row['first_name'], row['last_name'], row['email']))

file_path1 = "studentslist.txt"
display_students_under_30(file_path1)