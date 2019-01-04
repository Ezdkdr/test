def measureTrappedWater(arr):
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

l = list(input("input the list of items (comma separated): "))
print "The quanity of trapped water units is :", measureTrappedWater(l)
