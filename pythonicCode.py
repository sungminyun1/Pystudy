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

alist = ['a1','a2','a3']
blist = ['b1','b2','b3']

for a,b in zip(alist,blist):
    print(a,b)


alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']

for i, (a, b) in enumerate(zip(alist, blist)):
    print(i, a, b)

f= lambda x,y: x+y
print(f(1,4))

ex = [1,2,3,4,5]
print(list(map(lambda x: x **2 if x %2 ==0 else x, ex)))