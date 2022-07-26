

def count_patterns_from(firstPoint: str, length: int, firs_call = True, seq = None) -> int:
	'''
	Функция чтобы посчитать количество возможных паролей графического ключа, длины length, если начинать с точки firstPoint
	Первый аргумент - начальная точка, второй - длина пароля, остальные не заполнять.

	вид граф ключа:
	[A] [B] [C]
	[D] [E] [F]
	[G] [H] [I]


	'''


	counter = 0   # То, что мы будем возвращать (количество паролей)

	if seq is None: # Если это первый вызов, то создаём список, в который потом будем записывать составляющие ключа (буквы)
		seq = []

	

	curent_length = length

	curent_point = firstPoint

	seq.append(curent_point)

	# Крайний случай, и случай некоректных данных

	if length > 9 or length < 1:
		return 0
	if length == 1:
		return 1

	# Списки букв, до которых можно дотянуться с определённой точки

	A = ['B', 'E', 'D', 'H', 'F']
	B = ['A', 'C', 'D', 'E', 'F', 'G', 'I']
	C = ['B', 'E', 'F', 'D', 'H']
	D = ['A', 'B', 'C', 'E', 'H', 'I', 'G']
	E = ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I']
	F = ['A', 'B', 'C', 'E', 'G', 'H', 'I']
	G = ['D', 'E', 'H', 'F', 'B']
	H = ['G', 'D', 'A', 'E', 'C', 'F', 'I']
	I = ['H', 'D', 'E', 'B', 'F']

	lst_of_all = [A, B, C, D, E, F, G, H, I]

	my_di = {'A': A, 'B': B, 'C': C,
	         'D': D, 'E': E, 'F': F,
	         'G': G, 'H': H, 'I': I}


	# Если Е участвует в ключе, то список букв, к которым можно дотянуться с определённой буквы, будет больше

	if 'E' in seq:
		A.append('I')
		B.append('H')
		C.append('G')
		D.append('F')
		F.append('D')
		G.append('C')
		H.append('B')
		I.append('A')

	# Буквы не могут дотянуться друг до друга, если между ними есть другая буква, но если эта буква уже зажата, то это возможно
	if 'D' in seq:
		A.append('G')
		G.append('A')
	if 'B' in seq:
		A.append('C')
		C.append('A')
	if 'F' in seq:
		C.append('I')
		I.append('C')
	if 'H' in seq:
		I.append('G')
		G.append('I')


	# Перебор всех возможных ключей нужной длины

	for point in my_di[curent_point]:

		if point not in seq:

			counter += count_patterns_from(point, curent_length-1, firs_call = False, seq = seq)
			
			seq.pop()
		
	return counter


# print(count_patterns_from('B',1))
# print(count_patterns_from('E', 0))
# print(count_patterns_from('C',2))
# print(count_patterns_from('A',10))
# print(count_patterns_from('A',0)) 
# print(count_patterns_from('E',14))
# print(count_patterns_from('B',1))

# print(count_patterns_from('C',2)) 
# print(count_patterns_from('E',2)) 
# print(count_patterns_from('E',4)) 


def total_posible_combs():
	"""
	Сколько есть всего комбинаций для графического ключа телефона (обычно пароль состоит из минимум 4 символов и максимум 9) 
	(
	"""
	count = 0

	for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']:
		for j in range(4,10):
			count += count_patterns_from(i, j)

	print(count)

total_posible_combs()