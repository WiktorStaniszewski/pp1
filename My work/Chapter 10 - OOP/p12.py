class TV:
    def __init__(self, channel_no):
        self.is_on = False
        self.channel = channel_no
        self.current_channel = 1
        
    def turn_on(self):
        self.is_on = True
        
    def turn_off(self):
        self.is_on = False 
    
    def set_channel(new_channel_no):
        print("dupa")    
        
    def show_status(self):
        if self.is_on:
            return f"TV is on\nChannel: {self.current_channel}"
        else:
            return "TV is off"

my_tv = TV(13)
print(my_tv.show_status())
my_tv.turn_on()
print()
print(my_tv.show_status())