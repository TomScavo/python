
# prompt user int x

x=int(input("please enter int x: "))

# prompt user int y

y=int(input("please enter int y: "))

# a list of calculations

print("{} plus {} is {} ".format(x,y,x+y))
print("{} minus {} is {} ".format(x,y,x-y))
print("{} times {} is {} ".format(x,y,x*y))
print("{} divided by {} is {:.55f} ".format(x,y,x/y))
print("{} divided by{}(floor) is {} ".format(x,y,x//y))
print("remainder of{} divided by {} is {} ".format(x,y,x%y))
