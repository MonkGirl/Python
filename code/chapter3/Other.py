from math import pi
import string

print("{num:10}".format(num=3))
print("{name:10}".format(name="Bob"))
print("Pi day is {pi:5.2f}".format(pi=pi))

print("{:010.2f}".format(pi))
print("{0:<10.2f}\n{0:^10.2f}\n{0:>10.2f}".format(pi))

print(":$^15".format(" WIN BIG "))
print("{0:10.2f}\n{1:10.2f}".format(pi, -pi))
print("{0:10.2f}\n{1:=10.2f}".format(pi, -pi))

print("{1:-.2f}\n{0:-.2f}".format(pi, -pi))
print("{1:+.4}\n{0:+.4}".format(pi, -pi))

print("{:b}".format(42))
print("{:#b}".format(42))
print("{:#x}".format(42))
print("{:#o}".format(42))

print("The Middle by Jimmy Eat World".center(39))
print("The Middle by Jimmy Eat World".center(39, "*"))

print("With a moo-moo here, and a moo-moo there".find("moo"))
title = "Monty Python's Flying Cirus"
print(title.find("Monty"))
print(title.find("Python"))
print(title.find("Flying"))
print(title.find("Zirquss"))

subject = "$$$ Get rich now !!! $$$"
print(subject.find("$$$"))
print(subject.find("$$$", 1))
print(subject.find("!!!"))
print(subject.find("!!!", 0, 16))

seq = ['1', '2', '3', '4', '5']
sep = "+"
print(sep.join(seq))
dirs = "", "usr", "bin", "env"
print("/".join(dirs))
print("C:" + "\\".join(dirs))

print("Trondheim Hammer Dance".lower())

if "Gumby" in ["gumby", "smith", "jones"]:
    print("Found it!")
name = "Gumby"
names = ["gumby", "smith", "jones"]
if name.lower() in names:
    print("Found it!")

print("that's all folks".title())

print(string.capwords("that's all, folks"))

print("This is a test".replace("is", "eez"))

print("1+2+3+4+5".split("+"))
print("/usr/bin/env".split("/"))
print("Using the default".split())
print("         internal whitespace is kept    ".strip())

table = str.maketrans('cs', 'kz', ' ')
print(table)
print("this is an incredible test".translate(table))

print("3239420".isdigit())
print("wese3".isalpha())
