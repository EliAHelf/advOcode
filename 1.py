import re

lang = {
	'one': '1',
	'two': '2',
	'three': '3',
	'four': '4',
	'five': '5',
	'six': '6',
	'seven': '7',
	'eight': '8',
	'nine': '9',
}

# def present(line):
	# return line.find('one') > -1 or line.find('two') > -1 or line.find('three') > -1 or line.find('four') > -1 or line.find('five') > -1 or line.find('six') > -1 or line.find('seven') > -1 or line.find('eight') > -1 or line.find('nine') > -1
	
# def first(line):
	# dic = {}
	# dic.update({'one': line.find('one')})
	# dic.update({'two': line.find('two')})
	# dic.update({'three': line.find('three')})
	# dic.update({'four': line.find('four')})
	# dic.update({'five': line.find('five')})
	# dic.update({'six': line.find('six')})
	# dic.update({'seven': line.find('seven')})
	# dic.update({'eight': line.find('eight')})
	# dic.update({'nine': line.find('nine')})
	# return list(dic.keys())[list(dic.values()).index(min([i for i in dic.values() if i > -1]))]

# def conv(line):
	# while(present(line)):
		# line = line.replace(first(line), lang[first(line)] + first(line)[len(first(line)) - 1])
	# return line

file1 = open('1.txt', 'r')
Lines = file1.readlines()

total = 0

for line in Lines:
	l = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line.strip())
	a = l[0] if l[0].isnumeric() else lang[l[0]]
	b = l[len(l)-1] if l[len(l)-1].isnumeric() else lang[l[len(l)-1]]
	sum = a + b
	total += int(sum)
	# print(line)
	# fixed = conv(line)
	# m = fixed.strip()
	# r = m[::-1]
	# num = ''
	# for c in m:
		# if c.isnumeric():
			# num += c
			# break
	# for c in r:
		# if c.isnumeric():
			# num += c
			# break
	# total += int(num)
	# print(num)

print(total)


	

