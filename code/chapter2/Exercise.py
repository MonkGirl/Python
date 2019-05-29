edward = ['Edward Gumby', 42]
john = ['John Smith', 50]
database = [edward, john]
print(database)

greeting = 'Hello'
print(greeting[0])
print(greeting[-1])

fourth = input('Year: ')[3]
print(fourth)

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'Decemer']
endings = ['st', 'nd', 'rd'] + 17*['th']\
    + ['st', 'nd', 'rd'] + 7*['th']\
    + ['st']

year = input('Year: ')
month = input('Month(1-12): ')
day = input('Day(1-31): ')
month_number = int(month)
day_number = int(day)

month_name = months[month_number-1]
ordinal = day + endings[day_number-1]

print(month_name + ' ' + ordinal + ', ' + year)

tag = '<a href="http://www.python.org">Python web site</a>'
print(tag[9:30])
print(tag[32:-4])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[3:6])
print(numbers[3:])
print(numbers[0:10:2])

print([1, 2, 3] + [4, 5, 6])

print('Python'*8)

sentence = input('Sentence: ')

screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width) // 2

print()
print(' ' * left_margin + '+' + '-' * (box_width-2) + '+')
print(' ' * left_margin + '|' + ' ' * text_width + ' |')
print(' ' * left_margin + '|' + sentence + ' |')
print(' ' * left_margin + '|' + ' ' * text_width + ' |')
print(' ' * left_margin + '+' + '-' * (box_width-2) + '+')
print()
