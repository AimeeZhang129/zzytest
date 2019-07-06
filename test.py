def main():
	# test_array=[100,213,314]
	name_card = {
		"zhangmiaoxi":18,
		"zhaozhiyu":6,
		"tanzhen":3
	}
	a = 1  
	b = 2
	c = 3

	test_array = []

	for i in range(0,100):
		test_array.append(i)

	print a+b+c
	print test_array
	print name_card

	for number in test_array:
		print number

if __name__ == '__main__':
    main()
