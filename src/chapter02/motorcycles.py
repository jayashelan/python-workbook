motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

motorcycles.insert(5,'jay')
print(motorcycles)

del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

poppped_motorcycles = motorcycles.pop()
print(motorcycles)
print(poppped_motorcycles)

motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop();
print(f"The last motorcycles I owned is {last_owned.title()}")
first_owned = motorcycles.pop(0)
print(first_owned)

motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me")

print(motorcycles[-1])
motorcycles =[]
print(motorcycles[-1])



