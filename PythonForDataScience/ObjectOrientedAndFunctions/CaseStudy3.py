# Business challenge/requirement
# GoodsKart
#
# largest ecommerce company of Indonesia with revenue of $2B+ acquired another ecommerce company FairDeal.
# FairDeal has its own IT system to maintain records of customer, sales etc.
# For ease of maintenance and cost savings GoodsKart is integrating customer databases of both the organizations
# hence customer data of FairDeal has to be converted in GoodsKart
# Customer Format.
# Key issues
# GoodsKart customer data has more fields than in FairDeal customer data. Hence FairDeal data needs to be split and
# stored in GoodsKart Customer Object Oriented Data Structure
# Considerations
# System should convert the data at run time
# Data volume - NA
# Additional information - NA
# Business benefits
# GoodsKart can eventually sunset IT systems of FairDeal and reduce IT cost by 20 - 30%
# Approach to Solve
# You have to use fundamentals of Python taught in module 2
# 1. Read FairDealCustomerData.csv
# 2. Name field contains full name – use regular expression to separate title, first name, last name
# 3. Store the data in Customer Class
# 4. Create Custom Exception – CustomerNotAllowedException
# 5. Pass a customer to function "createOrder" and throw
# CustomerNotAllowedException in case of blacklisted value is 1
#
# Enhancements for code
# You can try these enhancements in code
# 1. Change function createOrder to take productname and product code as input
# 2. Create Class Order Return object of type Order in case customer is eligible
#

class CustomerNotAllowedException(Exception):
    def __init__(self, message):
        #Call the base class constructor with the parameters it needs
        # super(CustomerNotAllowedException, self).__init__(message)
        self.message=message

    def __str__(self):
        return str(self.message)

class Customer:
    def __init__(self,title,name,surname,blacklisted):
        self.title = title
        self.name = name
        self.surname = surname
        self.blacklisted = blacklisted

    def __str__(self):
        return "Customer: "+ self.title+" "+self.name+" "+self.surname+" blacklisted: "+self.blacklisted

class Order:
    def __init__(self,productname,productcode,customer):
        self.productname = productname
        self.productcode = productcode
        self.customer = customer

    def createOrder(self):
        try:
            if int(self.customer.blacklisted) == 1:
                # print("Exception raised")
                raise CustomerNotAllowedException("The customer is not allowed")
            else:
                print("Order created successfully")
        except CustomerNotAllowedException as e:
            # print("Exception Caught")
            print(e.__str__())


    def __str__(self):
        return "Customer: "+ self.productname+" "+self.productcode+" "+self.customer



f = open("dataset\FairDealCustomerData.csv","r")

lines = f.readlines()
customers = []

for line in lines:
    l = line.split(",")
    fullname = l[1].strip(" ")
    fullname = fullname.split(" ")

    title = fullname[0].strip(" ")
    name = fullname[1].strip(" ")

    if len(fullname) > 2:
        surname = fullname[2].strip(" ")
    else:
        surname = ""
    blacklisted = l[2].strip(" ")
    customers.append(Customer(title,name,surname,blacklisted))

# for customer in customers:
#     print(customer.__str__())

customer = customers[35]
print(customer)
order= Order("Iphone","Phone22",customer)

order.createOrder()