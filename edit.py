slok=[47,72,43,42,29,47,30,28,34,42,55,20,35,27,20,24,28,78]
for ch in range(1,19):
	#print(f"mkdir {ch}")
	for sl in range(1,1+slok[ch-1]):
		#print(f"mkdir {ch}/{sl}") 
		print(f'mv ./output/BG_{ch}_{sl}.md ./{ch}/{sl}/README.md')
			
		#with open(f"./output/BG_{ch}_{sl}.md", 'r+') as fp:
		# read an store all lines into list
		#	content = fp.read()
		#	fp.seek(0, 0)
		#	txt = f'<img src="../../asset/BG_{ch}_{sl}.png"/>'
		#	fp.write(txt+ '\n' + content)
		#	fp.close
