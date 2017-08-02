def main():
    i=get_positive_int()
    print("{} is apositive integer".format(i))
  
def get_positive_int():
    while True:
        print("positive please: ",end="")
        i=int(input())
        if i>0:
            break
    return i
if __name__=="__main__":
    main()
 
    