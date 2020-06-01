CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_number = 0

    def first_channel(self):
        print('FIRST channel')
        self.current_number = 0
        return self.channels[self.current_number]

    def last_channel(self):
        self.current_number = -1
        return self.channels[self.current_number]

    def turn_channel(self, N):
        if 1 <= N <= len(self.channels):
            self.current_number = N - 1
            return self.channels[N - 1]

    def next_channel(self):     
        self.current_number = (self.current_number + 1) % len(self.channels)
        return self.channels[self.current_number]

    def previous_channel(self):
        self.current_number = (self.current_number - 1) % len(self.channels)
        return self.channels[self.current_number]

    def current_channel(self):
        return self.channels[self.current_number]

    def is_exist(self, channel_arg):

        if type(channel_arg) == int:
            if 1 <= channel_arg <= len(self.channels):
                return "Yes"
            
        if type(channel_arg) == str:
            if channel_arg in self.channels:
                return "Yes"
            
        return "No"            

controller = TVController(CHANNELS)

