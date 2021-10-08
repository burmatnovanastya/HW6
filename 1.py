try:
	number = int(input('Введите количество элементов в массиве: '))
	delta = int(input('Введите delta: '))
	array = []
	min_num = 100000000
	for i in range(number):
		element = int(input('Введите ' + str(i + 1) + ' элемент: '))
		array.append(element)
		if min_num > element:
			min_num = element
	count_delta = 0
	for i in range(0, number):
		if min_num + delta == array[i]:
			count_delta += 1
	print('Найдено', count_delta, 'числа')
except ValueError:
	print('Неправильный ввод данных')