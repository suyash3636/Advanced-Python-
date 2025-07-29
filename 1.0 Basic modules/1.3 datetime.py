from datetime import datetime

now = datetime.now()

# print(now)

# print(now.year)     
# print(now.month)     
# print(now.day)      
# print(now.hour)      
# print(now.minute)    
# print(now.second)    

formatted = now.strftime("%Y-%m-%d %H:%M:%S")
# print(formatted)
# formatted = now.strftime("Year :%Y ")
# print(formatted)


from datetime import timedelta

future = now + timedelta(days=7)
# print(future)
delta = timedelta(days=10,hours=7)
# print(delta)

# print(now.date())  
# print(now.time())   
