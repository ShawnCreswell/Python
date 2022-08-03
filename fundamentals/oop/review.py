class Bird:

    def __init__(self, color, wingspan, noise, has_fight = True):
        self.color = color
        self.wingspan = wingspan
        self.has_flight = has_fight
        self.noise = noise

    def make_noise(self):
        print(self.noise)
    
tweetie = Bird('yellow', 'small', 'tweet')