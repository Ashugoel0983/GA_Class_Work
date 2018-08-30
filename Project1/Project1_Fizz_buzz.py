'''

Assignment : Project 1
Name: Ashu Goel

batch : Data Science

'''

##BONUS Challenge: FizzBuzz

def fizzbuzz():
    for i in range(1,101):  ##Running a Lopp till 100
        if i%3 == 0 and i%5 == 0:  #Checking a Number is divide by 3 and 5
            print("The nubmer {} is FizzBuzz ".format(i))
        elif i%3==0 :   ### Checking Number is only divide by 3
            print("The number {} is Fizz".format(i))
        elif i%5==0: ##Checking Number is only divide by 5
            print("The number is {} is Buzz".format(i))


fizzbuzz()