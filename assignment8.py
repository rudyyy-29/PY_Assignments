File1 = open("example.txt", "r")
ctr = 0
for i in File1:
        words = i.split() 
        ctr += len(words)
print ("Total number of words in file example.txt is: ", ctr)
File1.close()

#======================================================

File1 = open("example.txt", "r")
lines = File1.readlines()
print ("Total number of lines in file example.txt is: ", len(lines))

first_2_lines = lines[:2]
print ("\nFirst 2 lines of file example.txt are: ")
for i in first_2_lines:               #removes list format and print
    print(i)
File1.close()

#======================================================

File2 = open("example2.txt","w")
File2.writelines(first_2_lines)
File2.close()
print("\nFirst 2 lines of file example.txt are written in file example2.txt\n")