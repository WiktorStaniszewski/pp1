speed = int(input("Enter distance in km: "))
travel_hours = int(input("Enter the amount of hours you traveled: "))
travel_minutes = int(input("Enter the amount of minutes travelled: "))

def avg_speed(distance, hours, minutes):
    time = hours + minutes/60
    return round(distance/time, 1)

print(avg_speed(speed,travel_hours,travel_minutes))