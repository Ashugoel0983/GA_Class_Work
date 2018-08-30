'''

Assignment : Project 1
Name: Ashu Goel

batch : Data Science

'''

###Challenge 3: Multiples of 3 and 5

def multiple():
    num_sum = 0 ## Assing na Sum with 0 
    for i in range(1,1000): #For loop Till 1000 by using range function
        if(i%3==0 or i%5==0): ##checking Multiple of 3 and 5 
            num_sum=num_sum + i ## Adding Sum variable with current number
    
    return print("The Sum of Mulitple of 3 and 5 till 1000 is :",num_sum)

multiple()