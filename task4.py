list1=[-1,-6,-6,6,3,4,6,7,8,9,10]
t=max(list1)
list2=set(list(range(min(list1),max(list1)+1)))
set(list1)
list2.discard(0)
list2.difference_update(list1)
try:
	if min(list2)<0:
		print(1)
	else:
		print(min(list2))
except:
	print(t+1)