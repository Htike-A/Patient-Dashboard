from csvProcessor import process_csv

d = process_csv('Feeding Dashboard data.csv')
lst = []
g = []
for i in d:
	if i['referral'] == 1:
	    lst.append(i)
g = lst
print(g[-1])