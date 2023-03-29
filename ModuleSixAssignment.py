my_dict = {} #stores data
sorted_dict = {} #sorts the dictionary from my_dict
sorted_list = [] #makes the dictionary into a list
file1 = open(input(), 'r') #opens the first file in read only mode
contents = file1.readlines() #makes a list of the first element in the first like of the input
file1.close #closes the file when it is done as it is no longer needed
for i in range(0, len(contents), 2): #this keeps me from having an out of range error as EOF
    k = int(contents[i])
    v = contents[i+1].strip() #grabs the next like in the loop then removes the new line
    sorted_list.append(v) #turns the sorted list into a value so at the end of the loop it gets sorted by the function
    if k in my_dict: #this activates when a key is reached in the document and assigns it to the show
        my_dict[k] = my_dict[k] + '; ' + v
    else:
        my_dict[k] = v  #if one does not exist then this sets the value
for sk in sorted(my_dict):
    sorted_dict[str(sk)] = my_dict[sk] #prepares the key to be written
sorted_list.sort() #sorts my list after the loop ends
file2 = open("output_keys.txt", 'w') #opens the next file in write only
for k, v in sorted_dict.items():
    file2.write(k + ": " + v + '\n') #didn't need to convert to strings on this one but did have to write new lines
file2.close() #closes the document when it isnt needed
file3 = open("output_titles.txt", 'w') #opens the last one in write only
for v in sorted_list: #goes through all the values in the list
    file3.write(v + '\n')
file3.close() #closes the last file when it is no longer needed