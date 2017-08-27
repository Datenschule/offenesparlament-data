import json
from collections import defaultdict
from bs4 import BeautifulSoup

filepath = 'classes.json'

with open(filepath) as infile:
	answers = json.load(infile)
	cleaned_entries = []

	# building groups of answers for the same TOP
	groupings = defaultdict(list)
	for obj in answers:
		key = obj['info']['session'] + '-' + obj['info']['number']
		groupings[key].append(obj)
	groups = groupings.values()

	# check if entries have the same shape, if not take the first classification
	for group in groups:
		categories = [item['info']['categories'] for item in group ]
		length = len(categories[0])
		if any(len(lst) != length for lst in categories):
			print('Error: not the same length for session:' + group[0]['info']['session'] + ', TOP:' + group[0]['info']['number'] + '')
		else:
			zipped = zip(*categories)
			for cat_list in zipped:
				if not all(x == cat_list[0] for x in cat_list):
					print("Error: different categories for session:" + group[0]['info']['session'] + ', TOP: ' + group[0]['info']['number'])

		cleaned_entries.append(group[0]['info'])
	print(cleaned_entries)