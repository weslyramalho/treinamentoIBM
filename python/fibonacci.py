n = int(input("Entre com o numero de valores : "))
first = 0
second= 1
sum=0
count=1
print("Sequencia de Fibonacci: ")
while(count<=n):
    print(sum)
    count+=1
    first=second
    second=sum
    sum=first+second