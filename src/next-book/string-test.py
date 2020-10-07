s1 = "His name is {0} !".format("Arthur")
print(s1)

name = "Alice"
age = 10
s2 = "I am {1} and I am {0} years old".format(age,name)
print(s2)

n1 = 4
n2 = 5
s3 ="2**10 = {0} and {1} * {2} = {3:f}".format(2**10,n1,n2, n1 * n2)
print(s3)

n1 = "Paris"
n2 = "Whitney"
n3 = "Hilton"

print("Pi to three decimal places is {0:.3f}".format(3.1415926))

print("||| {0:<15}|||| {1:^15}|||{2:>15}||| Born in {3}|||".format("Paris","Whitney","Hilton",1981))


print("i\ti**2\ti**3\ti**4\ti**5\ti**10\ti**20")
for i in range(1,11):
    print(i,"\t",i**2,"\t", i**3,"\t",i**4,"\t",i**5,"\t",i**10,)

