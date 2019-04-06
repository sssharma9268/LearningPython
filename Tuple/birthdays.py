import datetime
import calendar

def get_birthdays(current, year, month, day):
    #print("Before weekday index")
    weekday_index = calendar.weekday(current, month, day)
    #print("After weekday index: ",weekday_index)
    dayname = calendar.day_name[weekday_index]
    age = current-year
    return age, dayname

print("""
Enter Your Birthday
Usage: 09/23/1970
""")

birthday = input("Birthday: ")
month, day, year = tuple(birthday.split("/"))

month = int(month)
day = int(day)
year = int(year)

now = datetime.datetime.now()
print("Now: ",now)
current_year = now.year
#print("Current Year: ",current_year)

while (current_year-year) >= 0:
    age, dayname = get_birthdays(current_year, year, month, day)
    print("Age: {}  Day: {}".format(age, dayname))
    current_year -=1


