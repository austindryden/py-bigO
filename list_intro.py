grocery_list = ["eggs", "milk", "bread"]

# how do I add stuff to a list
grocery_list.append("beer")
grocery_list.append("cat food")

# how do I access items from the end back?
grocery_list[-1]

#how do I acccess multiple items in a list?
grocery_list[0:3] #start at 0, end at 3(exclusive) (returns as a new list)

# what is "iteration" and how do  that with a list?
for item in grocery_list:
    print(f"you need to buy {item}")

# replace multiple items in a list
for i in range(len(grocery_list)):
    grocery_list[i] = "awesome " + grocery_list[1]

#how do I remove stuff from a list?
# POP POP!!
grocery_list.pop()

#how do I combine 2 lists?
# iterate and append
#extend
#concatenate
