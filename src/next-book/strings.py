greet = "Hello World"
xx = greet.swapcase()
print(greet)

fruit = "bannana"
m = fruit[1]
print(m)
print(list(enumerate(fruit)))

ix = 0
while ix < len(fruit):
    letter = fruit[ix]
    print(letter)
    ix += 1

prefixes = "JKLMN0PQ"
suffix ="ack"
for p in prefixes:
    print(p + suffix)


greeting = "Hello World!"
new_greeting = "J" + greeting[1:]
print(new_greeting)


