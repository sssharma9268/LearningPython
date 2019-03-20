name = input("Name: ")
lastname = input("lastname: ")
company = input("Company: ")

name = ".".join(name.split())
lastname = ".".join(lastname.split())

email = name.lower()+"."+lastname.lower()+"@"+company.lower()+".com"
email = email.replace(' ','')
print("Email: ",email)