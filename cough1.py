def main ():
        cough(3)
        sneeze(10)
def cough (n):
    say("cough",n)

def sneeze (n):            
    say("achoo",n)

def say (s,n):
    for i in range(n):
        print(s)
if __name__=="__main__":
    main()