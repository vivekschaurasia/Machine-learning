population_growth = 1.00005
total_population = 50

day_count = 0 #Every 2 months the population is reported

while total_population < 1000000:
    day_count = day_count+1
    total_population = total_population*population_growth
    #Every 56th day, population is reported
    if day_count ==56:
        print(day_count)
        print(total_population)
        day_count = 0



        
import random
startingPopulation = 50
infantMortality = 25

agriculture = 5

disasterChance = 10

food = 0

fertilityx = 18
fertilityy = 35
peopleDictionary = []
class Person:
    def __init__(self, age):
        self.gender = random.randint(0,1)
        self.age = age

def harvest(food, agriculture):
    ablePeople = 0
    for person in peopleDictionary:
        if person.age > 8:
            ablePeople +=1
    food += ablePeople * agriculture
    if food < len(peopleDictionary):
        del peopleDictionary[0:int(len(peopleDictionary)-food)]
        food = 0
    else:
        food -= len(peopleDictionary)

def reproduce(fertilityx, fertilityy):
    for person in peopleDictionary:
        if person.gender == 1:
            if person.age > fertilityx:
                if person.age < fertilityy:
                    if random.randint(0,5)==1:
                        peopleDictionary.append(Person(0))
def beginSim():
    for x in range(startingPopulation):
        peopleDictionary.append(Person(random.randint(18,50)))
beginSim()

def runYear(food, agriculture, fertilityx, fertilityy):
    harvest(food, agriculture)
    reproduce(fertilityx, fertilityy)
    for person in peopleDictionary:
        if person.age > 80:
            peopleDictionary.remove(person)
        else:
            person.age +=1
    
    print(len(peopleDictionary))

while len(peopleDictionary)<100000 and len(peopleDictionary) > 1:
    runYear(food, agriculture, fertilityx, fertilityy)

if random.randint(0,5)==1:
     if random.randint(0,100)>infantMortality:
           peopleDictionary.append(Person(0))

