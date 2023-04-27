"""                  

                        # 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610

                #      fibanocci number upto given index.

def fibonacii(n):
    if n<=0:
        return -1
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        return (fibonacii(n-1) + fibonacii(n-2))

n=int(input(" Enter the number:"))
print(fibonacii(n))

"""



"""
                #     fibanocci series sum upto given index.

def fib(n):
    if n<=0:
        return -1
    if n==1:
        return 0
    if n==2:
        return 1
    return fib(n-1)+fib(n-2)+1
n=int(input("Enter the number: "))
print(fib(n))

"""















"""
                       
                       #     Map, Dictionaries, set

"""




#             Set doesn't allow duplicate values
#             Set is unordered,unindexed and unchangeable data structure.

"""
a=[1,2,3,4,4,2,3,1,5]
print(a)

set_a=set(a)
print(set_a)

"""

#                   Dictionary

#            Dictionary is unordered,changeable and indexed data structure.
#            Dictionary is written in curly brackets.
#            Dictionary is a collection of key value pairs.
#            No duplicate keys are allowed.


"""

a={1:"one",2:"two",3:"three",4:"four",5:"five"}
print(type(a))
a["name"]="Bheema linga sai"
print(a["name"])

"""





#                               OOPS

#            Object oriented programming language sample walk through.

class Car:
    engineType = "strongest Engine"
    numberOfTyers = 4
    numberOfWindow = 6
    isFridgeAValble = True


    def getNumberOfWindows(self):
        return self.numberOfWindow

    def getNumberOfTyres(self):
        return self.numberOfTyers

car1 = Car()
print(car1.getNumberOfWindows())
print(car1.getNumberOfTyres())




