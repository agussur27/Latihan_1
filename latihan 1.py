print ("program mencari bilangan terbesar")
bil1=int(input("masukkan bilangan 1= "))
bil2=int(input("masukkan bilangan 2= "))
bil3=int(input("masukkan bilangan 3= "))

#Nilai terbesar

if (bil1>bil2) and (bil1>bil3):
    print("terbesarnya adalah= ",bil1)
elif (bil2>bil1) and (bil2>bil3):
    print("terbesarnya adalah= ",bil2)
else:
    print("terbesarnya adalah= ",bil3)