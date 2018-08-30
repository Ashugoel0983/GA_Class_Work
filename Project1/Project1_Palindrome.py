
'''

Assignment : Project 1
Name: Ashu Goel

batch : Data Science

'''

## Challenge 1: Largest Palindrome
def palidrome():
	num_plaindrome = 0 ## It stored the Product of Number


	for i in range(999,99,-1):    ##Define outer Loop
		for j in range(i,99,-1):   ## Inner Loop
			plaindrome_string = str(i*j)  ## Converting into String 
			reverse_num=plaindrome_string[::-1] ## Reverse a String and storned into Number

			if(plaindrome_string==reverse_num and i*j > num_plaindrome):  ##Compare The Reverse String with actual string and compare the Product of two number with previous number
				num_plaindrome = i*j   ## updating the Palindrome number with
	return print("The Longest Palidrom Number is :", num_plaindrome)

palidrome()














