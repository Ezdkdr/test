# a function that takes a list of positive integers as argument. The elements represnt the lengths of the towers
# it returns the number of units of water trapped between the towers
def measureTrappedWater(lst):
	i = 0
	trappedWaterUnits = 0
	j = len(arr) - 1
	added = True
	while added:
		while i < j and arr[i] == 0:
			i += 1
		while i < j and arr[j] == 0:
			j -= 1
		waterUnits = j - i + 1
		for k in range(i, j + 1):
			if arr[k] > 0:
				waterUnits -= 1
				arr[k] -= 1
		if waterUnits <= 0 or i == j:
			added = False
		else:
			trappedWaterUnits += waterUnits
	return trappedWaterUnits

l = list(input("input the list of items (comma separated): ")) # example: 0,1,0,0,2,0,4,0,3,0,0,2,1,0,3,0
print "The quanity of trapped water units is :", measureTrappedWater(l)
