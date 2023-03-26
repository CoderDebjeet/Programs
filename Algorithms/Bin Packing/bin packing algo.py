weight=[]
weight1=[]
n=int(input("Enter the size of the weights: "))
for i in range(0,n):
    ele=int(input("Enter a number : "))
    weight.append(ele)
size=int(input("Enter the size : "))
for i in range(n):
    for  j in range(0,n-i-1):
        if (weight[j] < weight[j+1]):
            weight[j],weight[j+1]=weight[j+1],weight[j]
for i in range(len(weight)):
    weight1.append(weight[i])
print(weight1)
space=[]
c=0
for i in range(len(weight1)):
    k=size-(weight[i])
    if(k<=size/2):
        space.append(k)
print(space)
weight3=set(weight1).intersection(space)
w3=list(weight3)
print(w3)
s=0
for i in range(0,len(w3)):
    s=s+w3[i]
print(s)
for i in w3:
    c=c+1

'''if s==0:
        for i in range(len(weight1)):
            for j in range(len(space)):
                if weight1[i] == space[j]:
                    print("The elements in bag ",i+1,"are:",weight1[i], "+",space[j])
            print("The elements in bag ",i+1,"are:",weight1[i],"+ 0")
        print("No of bags is",i)
else:'''
for o in range(len(weight1)):
        for  r in range(len(w3)):
            if weight1[o] == w3[r]:
                print("The elements in bag ",o+1,"are:",weight1[o], "+",w3[r])
        print("The elements in bag ",o+1,"are:",weight1[o], "+ 0")
  
print("No of bags is",o+1)
'''lst=[]
lst1=[]
for i in weight1:
    if i in w3:
        print("The elements in bag ",o+1,"are:",weight1[i], "+",w3[i])
    else:
       print(weight1[i],"+ 0")'''


        


