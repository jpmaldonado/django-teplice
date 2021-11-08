names = ["Pablo", "Marek", "Petra", "Jana"]

# First form ("classical")
i=0
while i < len(names):
    print(names[i])
    i += 1

# Second form: using range()
print('*'*50)
for i in range(len(names)):
    print(names[i])

# Third form: "Pythonic" way
print('*'*50)
for name in names:
    print(name)    

# Keep index + value without having a counter
print('*'*50)
for i, name in enumerate(names):
    #print(f'The {i+1}-th element is {name}')
    print('The {0}-th element is {1}'.format(i+1,name))

print('*'*50)
ages = {"Pablo":25, "Olga":30}
for name, age in ages.items():
    print(f"The age of {name} is {age}")

print('*'*50)
for it in ages:
    print(it)
