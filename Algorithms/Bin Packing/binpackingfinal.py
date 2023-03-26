def find_min_bags(weights, limit):
    weights.sort(reverse=True)
    bags = []
    for w in weights:
        added = False
        for bag in bags:
            if sum(bag) + w <= limit: #If the sum of the weights in the current bag plus the weight w is less than or equal to the limit, 
                bag.append(w) #the weight w is added to the current bag,
                added = True #and the added variable is set to True.
                break
        if not added:
            bags.append([w])
    return bags

weights = []
size = int(input("Enter the size of the weights: "))
for i in range(size):
    weight = int(input("Enter a number : "))
    weights.append(weight)

limit = int(input("Enter the size : "))
bags = find_min_bags(weights, limit)

print(weights)
for i in range(len(bags)):
    print(bags[i])

total_weight = 0
for bag in bags:
    total_weight += sum(bag)

print(total_weight)

for i in range(len(bags)):
    print("The elements in bag ", i+1, " are:", end=" ")
    for j in range(len(bags[i])):
        print(str(bags[i][j]) + " + ", end=" ")
    print()

print("No of bags is", len(bags))



'''Initialize an empty list called bags to hold the bags of weights.
Iterate through the weights in the input list weights.
For each weight w, initialize a boolean variable added to False.
For each bag in the list bags, check if the sum of the weights in the bag plus the current weight
w is less than or equal to the weight limit limit. If it is, add the weight w to the bag and set the added variable to True.
Then break out of the loop.
If the added variable is still False after iterating through all the bags,
that means there is no bag that can accommodate the weight w.
In this case, create a new bag with the weight w and add it to the list of bags bags.
After iterating through all the weights, return the list of bags.
This algorithm works by always adding the next weight to the first bag that can accommodate it.
If no bag can accommodate the weight, it creates a new bag.
This way, the algorithm always creates the minimum number of bags needed to hold all the weights.'''


'''
1.The 'find_min_bags' function takes in two parameters: weights and limit. weights is a list of integers representing the weights of items to be placed in bags, and limit is the maximum weight limit for each bag.

2.The weights list is sorted in descending order using the sort() method.

An empty list called bags is created to hold the bags.

A loop is started over each weight w in weights.

A boolean variable called added is initialized as False.

Another loop is started over each bag in bags.

If the sum of the weights in the current bag plus the weight w is less than or equal to the limit, the weight w is added to the current bag, and the added variable is set to True.

If the weight w cannot be added to any of the existing bags, a new bag is created with w as the only weight in it, and it is added to the bags list.

The function returns the list of bags.

The user is prompted to enter the size of the weights list, and each weight is entered through user input and appended to the weights list.

The user is prompted to enter the limit for the bags.

The find_min_bags function is called with weights and limit as arguments, and the result is assigned to the bags variable.

The weights list and each bag in the bags list are printed to the console.

The total weight of all the bags is calculated by summing up the weights in each bag.

The elements in each bag are printed to the console, along with the bag number.

The number of bags is printed to the console.

Overall, this code is implementing a solution to the bin packing problem, where the goal is to pack a set of items of different weights into the minimum number of bags possible, with each bag having a weight limit. 
The find_min_bags function uses a greedy algorithm to pack the items into bags in a way that minimizes the number of bags used.'''