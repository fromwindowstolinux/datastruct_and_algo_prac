# user input number
# user input target
# 'd' for done
# store number in list
# iterate the list
# if 'a' + 'b' = target, print found

empty_list = []

print("Enter 'd' when done\n")

print("Enter numbers:")

while True:
    numbers = input("")
    if numbers == "d":
        break
    empty_list.append(int(numbers))

target = input("\nEnter target:\n")

print("\nInput:")
print("nums =", empty_list)
print("target =", target)

print("\nOutput:")

for a in range(len(empty_list)):
    for b in range(len(empty_list)):
        calculate = empty_list[a] + empty_list[b]

        if  calculate == int(target):
            print(f"Pair found! {empty_list[a]} + {empty_list[b]} = {target}")
        else:
            print("Pair not found")