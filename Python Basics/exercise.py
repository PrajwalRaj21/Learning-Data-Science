weight = int(input("Enter your Weight: "))
weight_type = input("(K)g or (L)bs" )
weight_type.upper()

if weight_type == "K":
    converted = weight/ 0.45
    print("weight in lbs is " +str(converted))
else:
    converted = weight * 0.45
    print("Weight in kgs is " +str(converted))


