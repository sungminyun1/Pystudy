colors = ['a','b','c','d']

result = ''.join(colors)

print(result)

result = 'hello world'.split(' ')

print(result)

result = ' '.join([str(i) for i in range(10)])

print(result)

words = 'The quick brown fox jumps over the lazy dog'.split()

result = [[i.upper(),i.lower(),len(i)]for i in words]

print(result)