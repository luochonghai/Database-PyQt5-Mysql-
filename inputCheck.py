def str_check(strings):
	str_len = len(strings)
	if str_len == 0:
		#-3 means empty string
		return -3
	char_set = set("0123456789.")
	#set the position of dot as len(strings) by default
	dot_pos = str_len
	#sign:0-no sign,positive/0;1-positive;2-negative.
	sign = 0
	if strings[0] == '+':
		sign = 1
	elif strings[0] == '-':
		sign = 2

	for i in range(1,str_len):
		#check whether other characters exist in the string
		if strings[i] not in char_set:
			#-1 means strange characters exist in the strings
			return -1
		if strings[i] == '.':
			dot_pos = i
	#decimal_len records the length of decimal(no more than 2)
	decimal_len = str_len-dot_pos
	if decimal_len > 2:
		#-2 means decimal length is larger than 2
		return -2
	return 0

