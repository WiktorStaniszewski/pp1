class TV:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        
    def turn_off(self):
        self.is_on = False
        
    def show_status(self):
        if self.is_on:
            return "TV is on"
        else:
            return "TV is off"

my_tv = TV()
print(my_tv.show_status())
my_tv.turn_on()
print(my_tv.show_status())