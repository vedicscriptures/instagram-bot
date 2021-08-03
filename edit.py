txt = "<p>https://docs.bhagavadgitaapi.in/</p><p>#API #bhagavadgitaapi #slok #nodejs #js #api #gitaapi #krishna #hinduism #vedic #ISKCON #shreemadbhagavadgita #technology</p></center>"
slok=[47,72,43,42,29,47,30,28,34,42,55,20,35,27,20,24,28,78]
for ch in range(1,19):
	for sl in range(1,1+slok[ch-1]): 
		with open(f"./output/BG_{ch}_{sl}.svg", 'r+') as fp:
		# read an store all lines into list
			lines = fp.readlines()
			# move file pointer to the beginning of a file
			fp.seek(0)
			# truncate the file
			fp.truncate()

			# start writing lines except the last line
			# lines[:-1] from line 0 to the second last line
			fp.writelines("<center>")
			fp.writelines(lines[31:35])
			fp.writelines(lines[36].replace("</center></div></foreignObject></svg>",txt))
			fp.close()
			print(f"BG_{ch}_{sl}.svg")
