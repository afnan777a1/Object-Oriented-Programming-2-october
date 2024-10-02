class Vehicle:

    wheels = 4

    def __init__(self , maxSpeed, mileage):
        self.maxSpeed = maxSpeed
        self.mileage = mileage


nano = Vehicle(120, 30)
lambo = Vehicle(350, 3)

print(f"Nano Max Speed : {nano.maxSpeed}")
print(f"Nano Mileage : {nano.mileage}")

print(f"Lambo Max Speed : {lambo.maxSpeed}")
print(f"NLambo Mileage : {nano.mileage}")

print(f"Nano Wheels : {nano.wheels}")
print(f"Lambo Wheels : {lambo.wheels}")