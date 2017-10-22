f = open("out.txt", "w")
f.write("test")
f.close()

f = open("out.txt")
print(f.read())


def CelsiusToFahrenheit(Temperature):
   assert (Temperature > -273),"Colder than absolute zero!"
   return (Temperature * 9 / 5) + 32

def FahrenheitToCelsius(Temperature):
   return ((Temperature - 32) * 5 / 9)

def KelvinToCelsius(K):
    return K + 273

def CelsiusToKelvin(C):
    return C - 273

def KelvinToFahrenheit(K):
    return (CelsiusToFahrenheit(KelvinToCelsius(K)))

import math

print (KelvinToFahrenheit(32))
print (math.floor(KelvinToFahrenheit(505.78)))
#print (KelvinToFahrenheit(-5))

print (FahrenheitToCelsius(9/5))
print (FahrenheitToCelsius(32))
print (FahrenheitToCelsius(212))
print (FahrenheitToCelsius(42))


