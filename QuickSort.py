#快速排序

def quickSort(tup,_left,_right):
	
	left = _left
	right = _right
	tem = 0
	if left <= right:
		tem = tup[left]

		while left != right:
			#从右向左找到比tem小的数
			while right > left and tup[right] >= tem:
				right -= 1
			#将此数赋值给left位置
			tup[left] = tup[right]
			
			#从左向右找到比tem大的数
			while right > left and tup[left] <= tem:
			  	left += 1
			#将此数赋值给right位置
			tup[right] = tup[left]
		#left和right位置重合
		tup[right] = tem
		#递归调用
		quickSort(tup, _left, left - 1)
		quickSort(tup, right + 1, _right)
	return tup

tup = [5,2,45,6,8,2,1]


print(quickSort(tup,0,len(tup)-1))