import random

f = open('input', 'r');
g = open('output', 'w');

words = []

for line_in_file in f:
	line = line_in_file.strip('\n')
	words.append(line)

random.shuffle(words)

for word in words:
	g.write(word + ' ')

f.close();
g.close();
