class TV:
    def __init__(self, channel_no):
        self.is_on = False
        self.channel = channel_no
        
    def turn_on(self):
        self.is_on = True
        
    def turn_off(self):
        self.is_on = False 
    
    def set_channel(self,new_channel_no):
        self.channel = new_channel_no
                
    def show_status(self):
        if self.is_on:
            return f"TV is on\nChannel: {self.channel}"
        else:
            return "TV is off"
print(">")
tv = TV(1)
print(tv.show_status())
tv.turn_on()
print(">")
print(tv.show_status())
print(">")
tv.set_channel(5)
print(tv.show_status())
tv.turn_off()
print(">")
print(tv.show_status())