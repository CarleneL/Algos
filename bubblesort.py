
#write the bubble sort algorithm
#need a flag to track whether or not I sorted something 
#then in a for a loop of len of the data start iterating 
#if the item at the index is smaller then the next item I will swap them and set my flag to true. 
#If no swapping was done then I can set my flag to false

def bubble_sort(data):
    swapped = True
    while swapped:
    	for index in range(0, len(data)):
    		for next_item in range(index+1, len(data)):
    			if data[index] > data[next_item]:
    				data[index], data[next_item] = data[next_item], data[index]
    				swapped = True
    			else:
    				continue
    	swapped = False
    return data



assert bubble_sort([6,4,7,8]) == [4,6,7,8]

