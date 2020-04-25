import csv
from datetime import datetime
import matplotlib.pyplot as plt

ipaddr = '192.168.250.59'
k = 1
free = 1000

data = []
q = 0

times = []
timee = []
bytes = []

wor = {}

with open('dataset.csv') as csvfile:
	reader = csv.DictReader(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
	for row in reader:
		if row.get('sa') == ipaddr or row.get('da') == ipaddr:
			times.append(datetime.strptime(row.get('te'), '%Y-%m-%d %H:%M:%S'))
			bytes.append(int(row.get('ibyt')))
			q+=int(row.get('ibyt'))


q = q/1024
total = (q-free)*k

print(total)

plt.plot(times, bytes)
plt.title('Статистика объема трафика')
plt.grid(True)
plt.show()
