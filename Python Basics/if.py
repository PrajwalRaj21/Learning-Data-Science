##learning if statements

temperature = float(input("Enter the temperature: "))  #necessary to conver the string into float as default input() returns string
print (int(temperature))

if temperature > 30:
    print("It's hot")
elif temperature > 20:  #(20<x<30)
    print("Its a nice day")
elif temperature < 20:
    print("Its a bit cold")
else:
    print("Very Cold.")

print("Complete!")


