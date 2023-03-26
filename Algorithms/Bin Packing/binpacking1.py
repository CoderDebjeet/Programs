weight = []
n = int(input("Enter the number of items: "))
for i in range(n):
    ele = int(input("Enter the weight of item " + str(i+1) + ": "))
    weight.append(ele)

size = int(input("Enter the bin capacity: "))
weight.sort(reverse=True)

bins = [[]]
for w in weight:
    # Find the bin with the smallest available space that can accommodate the item
    found = False
    for b in bins:
        if sum(b) + w <= size:
            b.append(w)
            found = True
            break
    if not found:
        # Create a new bin if no existing bin can accommodate the item
        bins.append([w])

# Print the items in each bin
for i, b in enumerate(bins):
    print("Bin", i+1, "contains items:", b)

# Print the minimum number of bins required
print("Minimum number of bins required:", len(bins))
