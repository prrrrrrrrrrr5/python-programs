from Sfera import *

r=float(input("Inserisci di seguito il raggio della sfera in cm \n --> "))
c=Sfera(r)
print("L'area della sfera di raggio" ,r, "è" ,c.volume(), "cm^3")
print("La superficie della sfera di raggio" ,r, "è" ,c.superficie(), "cm^2")
