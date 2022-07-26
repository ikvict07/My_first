"""Stack usage"""


class _stack(list):
	def push(self, x):
		self.append(x)
	def pop(self):
		x = self[-1]
		del self[-1]
		return x
	def size(self):
		return len(self)
	def clear(self) -> None:
		del self[:]

stack = _stack()
sequence = '([)]()()((([][])))'
def is_brackets_correct(sequence: str) -> bool:

	for i in sequence:
		if i in '([':
			stack.push(i)
		else:
			assert i in ")]", "Ожидалась закрывающая скобка"
			if stack.size() == 0:
				return False

			left = stack.pop()
			right = ')' if left == '(' else ']'
			if right != i:
				return False

	return stack.size() == 0

print(is_brackets_correct('()[]([])(())(((())))[([()])]'))

def rpn(lst: list[str | int]):
	'''обратная польская нотация reverse polish notation
	(2+7)*5 --> [2,7,+,5,*]
	2+7*5   --> [2,7,5,*,+]
	'''
	stack = _stack()
	for i in lst:
		if type(i) is int or i.isdigit():
			stack.push(i)
		else:
			x = stack.pop()
			y = stack.pop()
			result = eval(str(y) + i + str(x))
			stack.push(result)

	return stack.pop()
print(rpn(['2',7,'+',5,'*']))
print(rpn([2,7,5,'*','+']))

