from math import *
G = 6.67430 * (10**-11)  #newton's universal constant of gravity # N*m^2/Km^2
R = {"Earth": 6371, "Mars": 3389.5, "Jupiter": 69911, "Saturn": 58232, "Uranus": 25362, "Venus": 6051.8, "Neptune": 24622, "Mercury": 2439.7 } #Radius of the planet #km
M = {"Earth": 5.972*(10**24), "Mars": 6.4185*(10**23), "Jupiter": 1.8986*(10**27), "Saturn": 5.6846*(10**26), "Uranus": 8.6810*(10**25), "Venus": 4.8685*(10**24), "Neptune": 10.243*(10**25), "Mercury": 3.3022*(10**23)}  #Mass of the planet #kg

a = str(input("Choose the planet: "))
r = 0
m = 0
ve = 0
for name,value in M.items():
    if name == a:
        m = value
        r = R[name]


ve = sqrt((2*G*m)/r) #Escape velocity # m/s
print("Escape velocity of " + a + " is : "+ str(ve) + " m/s")