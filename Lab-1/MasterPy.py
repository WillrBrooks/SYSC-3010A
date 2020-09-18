def int2roman(num):

	strOut = ""
	
	if (num >= 5000) | (num <= 0):
		raise ValueError

	while num > 0:
		if num >= 1000:
			strOut = strOut + "M"
			num = num - 1000
			continue
		if num >= 900:
			strOut = strOut + "CM"
			num = num - 900
			continue
		if num >= 500:
			strOut = strOut + "D"
			num = num - 500
			continue
		if num >= 400:
			strOut = strOut + "CD"
			num = num - 400
			continue
		if num >= 100:
			strOut = strOut + "C"
			num = num - 100
			continue
		if num >= 90:
			strOut = strOut + "XC"
			num = num - 90
			continue
		if num >= 50:
			strOut = strOut + "L"
			num = num - 50
			continue
		if num >= 40:
			strOut = strOut + "XL"
			num = num - 40
			continue
		if num >= 10:
			strOut = strOut + "X"
			num = num - 10
			continue
		if num >= 9:
			strOut = strOut + "IX"
			num = num - 9
			continue
		if num >= 5:
			strOut = strOut + "V"
			num = num - 5
			continue
		if num >= 4:
			strOut = strOut + "IV"
			num = num - 4
			continue
		if num >= 1:
			strOut = strOut + "I"
			num = num - 1
			continue

	
	return strOut


try:
	print(int2roman(int(input("Enter a number between 1 ad 4999: "))))
except ValueError:
	print("Invalid number")
