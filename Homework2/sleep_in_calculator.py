Day = 'Sun'
weekdays=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Mon", "Tue", "Wed", "Thu", "Fri"]
weekend=["Saturday","Sunday", "Sat", "Sun"]

if Day in weekdays:
    print('You can not sleep in baby. you better go to work')
elif Day in weekend:
    print('You are lucky. It is weekend. You can sleep in.')
