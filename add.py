slok=[47,72,43,42,29,47,30,28,34,42,55,20,35,27,20,24,28,78]
for ch in range(1,19):
	for sl in range(1,1+slok[ch-1]):	
		fin = open(f"./{ch}/{sl}/README.md", "rt")
		data = fin.read()
		data = data.replace('https://docs.bhagavadgitaapi.in/', 'https://bhagavadgitaapi.in/')
		fin.close()
		fin = open("README.md", "wt")
		fin.write(data)
		fin.close()
		print(f"./{ch}/{sl}/README.md")
