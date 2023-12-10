weather_forecast = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "

import re
temperatures = re.findall("2.", weather_forecast)
print(temperatures)