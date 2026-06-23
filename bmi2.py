w = float(input("Weight (kg): "))
h = float(input("Height (m): "))

b = w / (h ** 2)

print(f"BMI: {b:.2f}")

if b < 18.5:
    print("Underweight")
elif b < 25:
    print("Normal")
elif b < 30:
    print("Overweight")
else:
    print("Obese")