import datetime

current_time=datetime.datetime.now()
print(current_time)

# Printing attributes of now().
print("The attributes of now() are :")
print("Year :", current_time.year)
print("Month : ", current_time.month)
print("Day : ", current_time.day)
print("Hour : ", current_time.hour)
print("Minute : ", current_time.minute)
print("Second :", current_time.second)
print("Microsecond :", current_time.microsecond)