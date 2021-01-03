import requests
import re
import matplotlib.pyplot as plt

counter = {}
for line in requests.get('https://reports.opengroup.org/all.shtml').text.split('\n'):
	# regex : company name
	r1 = re.search(r'(<td>)([\w\s]+)(</td>)', line)
	# regex : country
	r2 = re.search(r'(<td class="r">)([\w\s]+)(</td>)', line)
	if r1 is None or r2 is None:
		continue
	else:
		company = r1.group(2)
		country = r2.group(2)

		if country not in counter:
			counter[country] = 1
		else:
			counter[country] += 1

countries = list(counter.keys())
counters = [counter[company] for company in counter]

plt.bar(countries, counters)
plt.xlabel('Countries')
plt.xticks(rotation=90)
plt.xlabel('# of members')
plt.savefig('mafirstplothahahah.png', dpi=400)
