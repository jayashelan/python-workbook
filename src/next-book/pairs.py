celebs = [("Brad Pitt",1963),("Jack Nicholson",1937),("Justin Bieber",1994)]

for (nm,year) in celebs:
    if year < 1980:
        print(nm)

students = [
    ("John",["CompSci","Physics"]),
    ("Vusi",["Maths","CompSci","Stats"]),
    ("Jess",["CompSci","Accounting","Economics","Management"]),
    ("Sarah",["InfSys","Accounting","Economics","CommLaw"]),
    ("Zuki",["Sociology","Economics","Law","Stats","Music"])
]


for (name,subjects) in students:
    print(name, "takes",len(subjects)," courses")

# Count
counter = 0
for (name,subjects) in students:
    for s in subjects:
        if s =="CompSci":
            counter += 1

print("The number of students takin CompSci is ",counter)
