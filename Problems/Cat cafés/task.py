cafes = []
cafe_cat_quantities = []
max_cafe = ""

while True:
    user_input = input()
    if user_input == "MEOW":
        break

    user_input_split = user_input.split()
    pop1 = user_input_split[0]
    cafes.append(pop1)
    pop2 = int(user_input_split[1])
    cafe_cat_quantities.append(pop2)

point = cafe_cat_quantities.index(max(cafe_cat_quantities))
max_cafe = cafes[point]
print(max_cafe)