speed = int(input("Enter distance in km: "))
travel_hours = int(input("Enter the amount of hours you traveled: "))
travel_minutes = int(input("Enter the amount of minutes travelled: "))

avg_speed = lambda dist,hours,minutes: round(dist/(hours+minutes/60),1)
print(avg_speed(speed,travel_hours,travel_minutes))