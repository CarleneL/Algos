'''
Recursive Quick sort

'''
def qsort1(unsorted_list):
	if len(unsorted_list)==0:
		return unsorted_list
	else:
		pivot = unsorted_list[0]
		smaller_array = qsort1([x for x in unsorted_list if x < pivot])
		larger_array = qsort1([y for y in unsorted_list if y > pivot])
		return smaller_array + [pivot] + larger_array


print qsort1([1,2,3,4,5,6,2,3,4,1,2,3,4,11,23,33441,23])