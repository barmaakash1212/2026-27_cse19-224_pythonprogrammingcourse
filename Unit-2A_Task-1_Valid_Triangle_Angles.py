angle1_in_degree = float(input("Enter first angle in degree: ")) 
angle2_in_degree = float(input("Enter second angle in degree: ")) 
angle3_in_degree = float(input("Enter third angle in degree: ")) 
if angle1_in_degree + angle2_in_degree + angle3_in_degree == 180 and angle1_in_degree > 0 and angle2_in_degree > 0 and angle3_in_degree > 0: 
    print(f"The triangle with angles {angle1_in_degree}, {angle2_in_degree}, and {angle3_in_degree} is valid")
else: 
    print(f"The triangle with angles {angle1_in_degree}, {angle2_in_degree}, and {angle3_in_degree} is not valid")