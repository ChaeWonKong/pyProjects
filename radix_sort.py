'''LSD Radix Sort

sort the given list of integers by sorting from least digit to most significant digit'''

def convert_str(values):
	'''Return list consist of strings from list consist of integers'''
	
	str_list = []
	for i in values:
		str_list.append(str(i))

	return str_list


def max_digit(values):
	'''Add '0' to elements to make them as same digit number'''

	intMax = max(values)
	digitMax = len(str(intMax))

	values = convert_str(values)

	result = [] #Contain converted outcomes

	for i in values:
		required = digitMax - len(i)
		result.append(required * '0' + i)

	return result




def sortLSD(values):
	'''Sort given list by using radix sort starting from least significant digit'''

	digitMax = len(values[0])
	temp = []
	result = []

	for units in range(1, digitMax +1):
		#Contain all the digits of same units into temp list
		for i in range(len(values)):
			if values[i][-units] not in temp:
				temp.append(values[i][-units])
			temp.sort()
		#print(temp)

		#Sort values list by comparing the units
		for k in temp:
			index = 0
			length = len(values)
			while index < length:
				#Contain value in result list as order
				if values[index][-units] == k:
					result.append(values.pop(index))
					length = len(values)
				else:
					index = index + 1
				
		# Reset all the lists for next sequence
		values = result
		temp = []
		result = []

	#Retern ordered values in integer form
	for i in values:
		result.append(int(i))

	return result

#List given
integers = [256, 56, 8, 2974, 13, 2972, 88] # List of integers given

print(sortLSD(max_digit(integers)))


