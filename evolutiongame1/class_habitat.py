class Habitat:
    def __init__(self, temperature, humidity, elevation, terrestrial, aqeous):
        self.temperature = temperature
        self.humidity = humidity
        self.elevation = elevation
        self.terrestrial = terrestrial
        self.aqeous = aqeous
        
#humidity goes from 0/100 and elevation/temperature and terrestrial/aqeuos are 0/100 with respect to eachother are real numbers
Desert = Habitat(temperature = 40, humidity = 10, elevation = 20, terrestrial = 99, aqeous=1)
Ocean = Habitat(temperature = 10, humidity = 100, elevation = 0, terrestrial = 0, aqeous=100)
Forest = Habitat(temperature = 15, humidity = 40, elevation = 100, terrestrial = 75, aqeous=25)
Mountains = Habitat(temperature = -10, humidity = 60, elevation = 3000, terrestrial = 90, aqeous=10)
Lake = Habitat(temperature = 10, humidity = 100, elevation = 0, terrestrial = 0, aqeous=100)
Shore= Habitat(temperature = 15, humidity = 80, elevation = 0, terrestrial = 40, aqeous=60)