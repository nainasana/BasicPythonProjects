#Temperature converter
#1 degree celsius = 33.8 degree farenhiet

#convert celsius into farenhiet using python
celsius = int(input("Enter the temperature: "))
farenhiet = (celsius * 1.8)+32
print(celsius, "degree celsius is equal to", farenhiet, "degree farenhiet")

#convert farenhiet intocelsius using python
farenhiet = int(input("Enter the temperature: "))
celsius = (farenhiet - 32)/1.8
print(farenhiet, "degree celsius is equal to", celsius, "degree farenhiet")
