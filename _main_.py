class EnergySource:

  def __init__(self, name, capacity, emissions_factor, cost):
    self.name = name
    self.capacity = capacity
    self.emissions_factor = emissions_factor
    self.cost = cost

  def get_emissions(self, energy_used):
    return energy_used * self.emissions_factor

class Building:

  def __init__(self, name, energy_need):
    self.name = name
    self.energy_need = energy_need
    self.powered = True

  def receive_power(self, energy_supplied):
    if energy_supplied < self.energy_need:
      self.powered = False
      print(f"{self.name} has lost power!")  

  def calculate_emissions(self, source, energy_used, time):
    return source.get_emissions(energy_used)*time

time_of_day = input('please input time of day for game (day/night) ')

oil_gas = EnergySource("Oil/Gas", 500, 0.005, 1)
solar = EnergySource("Solar", 200, 0, 0.6)
nuclear = EnergySource("Nuclear", 300, 0, 3)

sources = [oil_gas, solar, nuclear]
buildings = []

house_count = int(input("How many houses? "))
for i in range(house_count):
  buildings.append(Building("House", 5))

apartment_count = int(input("How many apartments? "))
for i in range(apartment_count):
  buildings.append(Building("Apartment", 10))

hospital_count = int(input("How many hospitals? "))
for i in range(hospital_count):
  buildings.append(Building("hospital", 10))

malls_count = int(input("How many malls? "))
for i in range(hospital_count):
  buildings.append(Building("mall", 10))
# Add other building types...

if time_of_day == 'day':
  energy_capacity = sum(s.capacity for s in sources)

else:
  energy_capacity = 0
  for s in sources:
    if s.name != 'solar':
      energy_capacity += s.capacity

emissions_total = 0
cost_total = sum(s.cost for s in sources)
energy_consumption = sum(s.energy_need for s in buildings)

def time_elapsed(energy_consumption, energy_capacity):
    hours = 0
    while energy_capacity > 0:
        energy_capacity -= energy_consumption
        hours += 1
    return hours


hours = time_elapsed(energy_consumption, energy_capacity)
emissions = oil_gas.capacity * oil_gas.emissions_factor * hours
score = hours*len(buildings) - emissions - cost_total

print("score:", score)
print("hours:", hours)
print("emissions:", emissions)