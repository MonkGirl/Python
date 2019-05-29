from copy import deepcopy

phonebook = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
print(phonebook['Beth'])

items = [('name', 'Gumby'), ('age', 42)]
d = dict(items)

s = dict(name='Gumby', age=42)
print(s)

x = {}
x[42] = 'Foobar'
print(x)

print("Cecil's phone number is {Cecil}.".format_map(phonebook))
d.clear()
print(d)

x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy()
x['username'] = 'mlh'
print(x)
print(y)
y['machines'].remove('bar')
print(x)
print(y)

d = {}
d['names'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(d)
d['names'].append('Clive')
print(c)
print(dc)

print(dict.fromkeys(['name', 'age'], 'unknown'))

# print(d['newName'])
print(d.get('newName'))
print(d.items())

it = d.items()
print(len(it))
print(('names', ['Alfred', 'Bertrand', 'Clive']) in it)

print(d.keys())
d.pop('names')
print(it)

d = {'url': 'http://www.python.org', 'spam': 0, 'title': 'Python Web Site'}
d.popitem()
print(d)
d.setdefault('spams', 2)
print(d)

x = {'url': 'https://cn.bing.com'}
d.update(x)
print(d)
print(d.values())
