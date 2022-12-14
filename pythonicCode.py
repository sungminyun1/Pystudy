from collections import deque
from collections import OrderedDict
from collections import defaultdict
from collections import Counter

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

def asterisk_test(a,*args):
    print (args)
    print(type(args))


asterisk_test(1,2,3,3,4,5,5)

def asterisk_test2(a, **args):
    print(args)
    print(type(args))

asterisk_test2(1,c=1,b=2)


deq_list = deque()
for i in range(10):
    deq_list.append(i)
print(deq_list)

d= OrderedDict()
d['x'] = 1
d['y'] = 2
d['a'] = 3
print(d)

d= defaultdict(object)
print(d['first'])

c = Counter('gallahad')
print(c)