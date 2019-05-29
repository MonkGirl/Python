from string import Template
from math import pi
from math import e

format = "Hello, %s, %s enough for ya?"
values = ('world', 'Hot')
print(format % values)

tmpl = Template("Hello, $who! $what enough for ya?")
tmpl.substitute(who="Mars", what="Dusty")
print(tmpl)

print("{}, {} and {}".format("first", "second", "third"))
print("{0}, {1} and {2}".format("first", "second", "third"))
print("{3} {0} {2} {1} {3} {0}".format("be", "not", "or", "to"))

print("{name} is approximately {value:.20f}.".format(value=pi, name="π"))
print(f"Euler's constant is roughly {e}.")
print("Euler's constant is roughly {e}.".format(e=e))

print("{{ceci n'est pas une replacement field}}".format())

print("{foo} {} {bar} {}".format(1, 2, bar=4, foo=3))

fullname = ["Alfred", "Smoketoomuch"]
print("Mr {name[1]}".format(name=fullname))

print("{pi!s} {pi!r} {pi!a}".format(pi="∏"))

print("The number is {num}".format(num=42))
print("The number is {num:f}".format(num=42))
print("The number is {num:b}".format(num=42))
