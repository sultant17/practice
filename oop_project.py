class School:

  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def __repr__(self):
    return "A {level} school named {name} with {numberOfStudents} students. ".format(level= self.level, name = self.name, numberOfStudents=self.numberOfStudents)
  
  def getName(self):
    return self.name
  
  def getLevel(self):
    return self.level
  
  def getNumberOfStudents(self):
    return self.numberOfStudents
  
  def setNumberOfStudents(self, new_number):
    self.numberOfStudents = new_number


a = School("Codecademy", "high", 100)
print(a)
print(a.name)
print(a.level)
a.setNumberOfStudents(200)
print(a.numberOfStudents)

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, "Primary", numberOfStudents)   
    self.pickupPolicy = pickupPolicy

  def __repr__(self):
    return super().__repr__() + "The pickup policy is {pickupPolicy}".format(pickupPolicy = self.pickupPolicy)

  def getPickupPolicy(self):
    return self.pickupPolicy

b = PrimarySchool("Codecademy", 300, "Pickup Allowed")
print(b.pickupPolicy)
print(b)

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportTeams=[]):
    super().__init__(name, "High", numberOfStudents)
    self.sportTeams = sportTeams
  
  def __repr__(self):
    return super().__repr__() + "The team sports are {sportTeams}".format(sportTeams = self.sportTeams)
  
  def getSportTeams(self):
    return self.sportTeams

c = HighSchool("Codecademy High", 500, ["Tennis", "Basketball"])
print(c.sportTeams)
print(c)


   

   

  
    



