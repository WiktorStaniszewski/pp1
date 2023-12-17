class TV:
    def __init__(self):
        self.is_on = False
        self.channel = 'Not set yet'
        self.channel_list = []
        self.current_channel = 'Not set yet'
        
    def turn_on(self):
        self.is_on = True
        
    def turn_off(self):
        if self.is_on:
            self.is_on = False
        else:
            return "TV is already off" 
        
    def set_all_channels(self, channel_list):
        if self.is_on:
            import re
            pattern = rf"\w+"
            channel_list = re.findall(pattern, channel_list)
            self.channel_list = channel_list
            
    def show_channel(self, name):
        if self.is_on:
            channels = ""
            if name == 0:
                for i in self.channel_list:
                    channels+=f"{i} "
                return f"All channels: {channels}"
            else:
                self.channel = self.channel_list.index(name)+1
                for i in self.channel_list:
                    if i == name:
                        self.current_channel = i
                        return f"Current channel: {i}"
        
    def names(self, channel_list):
        self.channel_list = 0
        
    def show_status(self):
        if self.is_on:
            return f"TV is on\nChannel: {self.channel}\nChannel name: {self.current_channel}"
        else:
            return "TV is off"
if __name__ == "__main__":    
    print(">")
    tv = TV()
    print(tv.show_status())
    tv.turn_on()
    print(">")
    print(tv.show_status())
    print(">")
    print(tv.show_status())
    print(">")
    tv.set_all_channels("TVP1 TVP2 Polsat TVN Filmbox Discovery")
    print(tv.show_channel(0))
    print(tv.show_channel("Polsat"))
    print(">")
    tv.show_channel("Discovery")
    print(tv.show_status())
    tv.turn_off()
    print(">")
    print(tv.show_status())
