'''

Assignment : Project 1
Name: Ashu Goel

batch : Data Science

'''

###Challenge 4: String Compressor


def strCompressor(myList):
    strList=[] ## Empty List which will hold actuall Output of String
    count=1  ## it is Counter variable which count the number of Char Occurance
    for i in range(1,len(myList)):     ### For List and it will execute till the Length of List and it is starting from postion 1
        if myList[i] == myList[i-1]:  ### Compare the Char with Previous Char and if it is match then Increase the Count
            count=count+1
        else:
            strList.append(myList[i-1]) ### If the Char nt match then Stored the last Char into Main Strlist with Count
            strList.append(count)
            count=1 ## Rest thhe Counter
            if i == (len(myList)-1):
                strList.append(myList[i])
                strList.append(count)
    return print('The Compressed String is ',(''.join(str(a) for a in strList)))


strCompressor('AAABCAAACCD')