#快速排序

def selectSort(tup):
	length = len(tup)
	temp = 0
	for i in range(length):
		min = i
		for j in range(length - 1,i,-1):
			if tup[j] < tup[min]:
				min = j

		tup[i], tup[min] = tup[min], tup[i] 

	return tup


tup = [5,2,45,6,8,2,1]

print(selectSort(tup))