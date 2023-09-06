tup1= ("apple", "banana", "cherry")
tuple2 = (1, 2, 3)


print(tup1[:1])

#Travessar uma tupla
for x in tup1:
    print(x)

#verificar se exixte item
if "banana" in tup1:
    print("Yes, 'banana' is present.")

#Comprimento da tupla
print(len(tup1))

#Junte dois tuplas
tup3= tup1 + tuple2
print(tup3)
