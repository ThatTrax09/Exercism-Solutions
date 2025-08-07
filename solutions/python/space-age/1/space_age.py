class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.orbital_periods = {
            'Mercury' : 0.2408467,
            'Venus' : 0.61519726,
            'Earth'	: 1.0,
            'Mars' : 1.8808158,
            'Jupiter' : 11.862615,
            'Saturn' : 29.447498,
            'Uranus' : 84.016846,
            'Neptune' : 164.79132
        }
    def to_years(self, orbital_period):
        return self.seconds/60/60/24/(365.25 * orbital_period)
    def on_mercury(self):
        return round(self.to_years(self.orbital_periods['Mercury']),2)
    def on_venus(self):
        return round(self.to_years(self.orbital_periods['Venus']),2)
    def on_earth(self):
        return round(self.to_years(self.orbital_periods['Earth']),2)
    def on_mars(self):
        return round(self.to_years(self.orbital_periods['Mars']),2)
    def on_jupiter(self):
        return round(self.to_years(self.orbital_periods['Jupiter']),2)
    def on_saturn(self):
        return round(self.to_years(self.orbital_periods['Saturn']),2)
    def on_uranus(self):
        return round(self.to_years(self.orbital_periods['Uranus']),2)
    def on_neptune(self):
        return round(self.to_years(self.orbital_periods['Neptune']),2)
        
