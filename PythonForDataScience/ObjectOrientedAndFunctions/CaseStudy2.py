# Business challenge/requirementBank of Portugal runs marketing campaign to offer loans to clients.
# Loan is offered to only clients with particular professions.
# List of successful campaigns(with client data) is given in attached dataset.
# You have to come up with program which reads the file and builds a set of unique profession list and
# given input profession of client –system tells whether client is eligible to be approached for marketing campaign.
#
# Key issues:
# Tele Caller can only make x number of cold calls in a day.
# Hence to increase her effectiveness only eligible customers should be called
# ConsiderationsCurrent: system does not differentiate clients based on age and profession Data
# volume:447 records in bank-data.csvAdditional
# information-NABusiness
# benefitsCompany can achieve between 15% to 20% higher conversion by targeting right clients
#
# Approach to SolveYou have to use fundamentals of Python taught in module2
# 1.Read file bank-data.csv
# 2.Build a set of unique jobs
# 3.Read the input from command line – profession
# 4.Check if profession is in list
# 5.Print whether client is eligible
#
# Enhancements for codeYou can try these enhancements in code
# 1.Compute max and min age for loan eligibility based on data in csv file
# 2.Store max and min age in dictionary
# 3.Make the profession check case insensitive
# 4.Currently program ends after the check.
# Take the input in whileloop and end only if user types "END" for profession
from functools import reduce

f =open("dataset\\bank-data.csv")

dict = {'age':[],'job':[],'marital':[],'y':[]}
lines = f.readlines()

for i in range(1,len(lines)):

    dict.get('age').append(lines[i].split(",")[0].strip())
    dict.get('job').append(lines[i].split(",")[1].strip("."))
    dict.get('marital').append(lines[i].split(",")[2].strip())
    dict.get('y').append(lines[i].split(",")[3].strip())

UniquesJobs = set(dict.get('job'))
print(UniquesJobs)

mystr = input("Enter the profession to check: ")
while mystr != "END":
    if mystr.lower() in UniquesJobs:
        print("The client is eligible")
    else:
        print(" The client is not eligible")
    mystr = input("Enter the profession again to check, Enter END to finish: ")

min_max_age={'min_age':reduce(lambda a,b : a if a < b else b, dict.get('age')),
             'max_age':reduce(lambda a,b : a if a > b else b, dict.get('age'))}

print(min_max_age)
