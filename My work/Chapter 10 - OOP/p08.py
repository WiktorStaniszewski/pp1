class Telefon():
    def __init__(self, number, make, camera, battery):
        self.number = number
        self.make = make
        self.camera = camera
        self.is_on = False
        self.battery = battery
    def open(self):
        self.is_on = True
    def close(self):
        self.is_on = False
    def camera_switch(self):
        if self.camera != 108:
            self.camera = 108
        else: 
            self.camera = 48
    def charging(self):
        if self.battery!=100:
            self.battery = 100
        else:
            return "Battery is full"

My_Phone = Telefon("281903812", "Xiaomi", 48, 78)
My_Phone.open()
if My_Phone.open:
    print(f"My phone is {My_Phone.make}, it's got a great camera: {My_Phone.camera} but with a better option of it's got {My_Phone.battery}% of battery but once i charge it, it will have%")
else:
    print("Turn on the phone first")