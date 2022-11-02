# user input number
# user input target
# 'd' for done
# store number in list
# iterate the list
# if 'a' + 'b' = target, print found

def findPair(nums, target):

    for a in range(len(nums) - 1):
        for b in range(a + 1, len(nums)):
            calculate = nums[a] + nums[b]

            if  calculate == int(target):
                print(f"Pair found! {nums[a]} + {nums[b]} = {target}")
            
    print("Pair not found")


if __name__ == "__main__":

    print("Enter 'd' when done\n")

    nums = []

    print("Enter numbers:")
    while True:
        numbers = input("")
        if numbers == "d":
            break
        nums.append(int(numbers))

    target = input("\nEnter target:\n")

    print("\nInput:")
    print("nums =", nums)
    print("target =", target)
    
    print("\nOutput:")
    findPair(nums, target)