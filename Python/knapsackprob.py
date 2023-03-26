#Fractional Knapsack Problem
def knapsack(w,weights,values):
    ratios=[v/w for v,w in zip(values,weights)]
    n=len(weights)
    index=list(range(n))
    index.sort(key= lambda i: ratios[i] ,reverse=True)
    max_value =0
    fractions=[0]*n
    for  i in index:
        if weights[i]<=w:
            max_value+= values[i]
            w-=weights[i]
            fractions[i]=1
        else:
            fractions[i]=w/weights[i]
            max_value+=values[i] * fractions[i]
            break
    print(fractions)
    return max_value
    
            
weights=[10,20,30]
values=[60,100,120]
w=50  #maximum weight
#ratio values/weights
 #           6/kg    5/kg    4/kg

print(knapsack(w,weights,values))




'''
The code solves the Fractional Knapsack Problem which is a variant of the classic Knapsack Problem where items
can be divided into fractions. The objective is to maximize the total value of the selected items while keeping the total weight
below the maximum weight allowed. Here is a step-by-step explanation of the code:

Define the knapsack function with three parameters: w (maximum weight), weights (a list of item weights), and values (a list of item values).

Compute the ratio of value to weight for each item in the list using a list comprehension. This gives a list of ratios corresponding to the items.

Get the length of the weights list and create a list of indices for the items using the built-in function range().
Then, sort the list of indices based on the corresponding ratios in descending order using the sort() method and a lambda function.

Initialize the maximum value of the knapsack to zero and create a list of fractions corresponding to each item, initially set to zero.

Iterate through the sorted list of indices and for each item:
a. Check if the weight of the item is less than or equal to the remaining capacity of the knapsack.
    If it is, add the value of the item to the maximum value and subtract the weight of the item from the remaining capacity of the knapsack.
    Set the fraction of the item to 1 since the whole item is selected.
b. If the weight of the item is greater than the remaining capacity of the knapsack, calculate the fraction of the item
    that can be added to the knapsack by dividing the remaining capacity by the weight of the item.
    Add the fraction times the value of the item to the maximum value. Set the fraction of the item to the calculated value.
c. Break out of the loop since the remaining capacity of the knapsack is now zero.

Print the list of fractions and return the maximum value of the knapsack.

The function calculates the optimal combination of items to add to the knapsack to maximize the total value
while keeping the total weight below the maximum weight allowed. The solution includes the fraction of each item added to the knapsack.
'''
