import csv
import os

with open("Program.csv", "r", newline="", encoding="UTF-8") as ifp, \
open("new_Program.txt", "w", newline="", encoding="UTF-8") as ofp:
	reader = csv.reader(ifp)
	writer = csv.writer(ofp)
	headers = next(reader)
	for i, row in enumerate(reader):
		for j, header in enumerate(headers):
			writer.writerow([i+1, header, row[j]])

with open("new_Program.txt", "r", newline="", encoding="UTF-8") as ifp, \
open("prefix.txt", "w", newline="", encoding="UTF-8") as ofp:
    reader = csv.reader(ifp)
    writer = csv.writer(ofp)
    for row in reader:
        if row[1] in ["Ημέρα", "Ώρα έναρξης", "Ώρα λήξης"]:
            label = "l:"
        else:
            label = "u:"
        writer.writerow(["b:"+row[0], row[1], label+row[2]])

os.remove("new_Program.txt")

with open('prefix.txt', 'r', newline = '') as ifp, open('uri.txt', 'w', newline = '') as ofp:
	reader = csv.reader(ifp)
	writer = csv.writer(ofp)
	for s,p,o in reader:
		p = '<http://host/sw//myvocab#' + p.replace(" ", "%20") + '>'
		if o[0] == 'u':
			o = '<http://host/sw/you/resource/' + o.replace(" ", "%20")[2:] + '>'
		writer.writerow([s,p,o])

os.remove("prefix.txt")

with open('uri.txt', 'r', newline = '') as ifp, open('rdf.txt', 'w', newline = '') as ofp:
	reader = csv.reader(ifp)
	writer = csv.writer(ofp)
	for s,p,o in reader:
		s = s.replace("b:", "_")
		if o.startswith("l:"):
			content  = o.split("l:")[1]
			o = s.replace("l:","_")
			if "#Start%20time" or "#End%20time" in p:
				time = '"' + content + ':00"'
				new_o = time + "^^" + "<" + p +"#time" +">"
			elif "#Day" in p:
				new_o = '"' +content +'"'
		print(s,p,o)
		writer.writerow([s,p,o])

os.remove("uri.txt")
