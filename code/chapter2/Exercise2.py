permissions = 'rw'
print('w' in permissions)
print('x' in permissions)

users = ['mlh', 'foo', 'bar']
print(input('Enter your user name: ') in users)

subject = '$$$ Get rich now!!!$$$'
print('$$$' in subject)

database = [
    ['albert', '1234'],
    ['dilbert', '4242'],
    ['smith', '7524'],
    ['jones', '9843']
]

username = input('User name: ')
pin = input('PIN code: ')

if[username, pin] in database:
    print('Access granted')

numbers = [100, 34, 678]
print(len(numbers))
print(max(numbers))
print(min(numbers))

list('Hello')
x = [1, 1, 1]
x[1] = 3
print(x)
names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
del names[1]
print(names)

numbers = [1, 5]
numbers[1:1] = [2, 3, 4]
print(numbers)
# numbers[1:4] = []
del numbers[1:4]
print(numbers)

lists = [1, 2, 3]
lists.append(4)
print(lists)
lists.clear()
print(lists)

a = [1, 2, 3]
b = a
b[1] = 4
print(a)

c = a.copy()
c[2] = 8
print(a)
print(c)

x = ['to', 'be', 'or', 'not', 'to', 'be']
print(x.count('to'))

y = [[1, 2], 1, 1, [2, 1, [1, 2]]]
print(y.count(1))
print(y.count([1, 2]))

a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)
c = [1, 2, 3]
print(c + b)
print(c)

knights = ['We', 'are', 'the', 'knights', 'who', 'say', 'ni']
print(knights.index('the'))
print(knights.index('Icarus'))

numbers = [1, 2, 3, 4, 5, 6, 7]
numbers.insert(0, 0)
numbers[0:0] = [-1]
print(numbers)
print(numbers.pop(8))
print(numbers)
print(numbers.append(7))
print(numbers)
numbers.remove(3)
print(numbers)
numbers.reverse()
pprint(numbers)

x = [4, 8, 2, 78, 21, -9]
y = sorted(x)
print(x)
print(y)

x = ['aardvark', 'aurora', 'abalone', 'acme', 'add', 'aerate']
# x.sort(key=len)
x.sort()
print(x)

x = 43,
print(x)
print(3*(35,))
tuple([4, 5, 9])
tuple((3, 4, 8))
tuple('abc')
