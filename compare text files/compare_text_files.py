from tabulate import tabulate

f1 = open("C:/Users/avina/OneDrive/Desktop/Training/28_Apr_22/compare text files/file1.txt", "r")  
f2 = open("C:/Users/avina/OneDrive/Desktop/Training/28_Apr_22/compare text files/file2.txt", "r")  
f = open("C:/Users/avina/OneDrive/Desktop/Training/28_Apr_22/compare text files/file3.txt", "w+")

i = 0
list1 = []

for line1 in f1:
    i += 1
      
    for line2 in f2:
          
        # matching line1 from both files
        if line1 == line2:
            #print IDENTICAL if similar
            print("Line ", i, ": IDENTICAL") 
        else:
            line1=line1.split()
            line2=line2.split()
            print("Line :" + str(i))
            for j in range(len(line1)):
                if line1[j] != line2[j]:
                    print((line1[j],line2[j]))
                    output = str(i) + " " + line1[j] + " " + line2[j]
                    #output1 = output.items()
                    #f.write(tabulate(output1))
                    #f.write('\n')
                    list1.append([i, line1[j], line2[j]])

                    
                    

        break
f.write(tabulate(list1, headers=["line", "F1", "F2"],  tablefmt='grid'))
  
#closing files
f.close()
f1.close()                                       
f2.close()

