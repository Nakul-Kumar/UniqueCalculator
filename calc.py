q = 0
fil = input('Enter file name: ')
myfil = open(fil)
inf = myfil.read().splitlines()
myfil.close()
rng = len(inf)
while q < rng:
	nums = range(10)
	out = []
	for num in nums:
		out.append(num)

	inp = [line for line in inf]
	numbers = inp[q]
	numbersplt = ([char for char in numbers])
	z = int(numbersplt[0])
	y = int(numbersplt[1])
	x = int(numbersplt[2])
	w = int(numbersplt[3])
	v = int(numbersplt[4])

	a = str(out[z]) + str(out[y])
	e = out[x]
	b = int(a)*int(e)
	c = str(out[w]) + str(out[v])
	d = int(b) + int(c)
	n = str(b)
	s = str(d)

	it = [num for num in n]
	et = [num for num in s]

	fin = [out[z], out[y], e, int(it[0]), int(it[1]), out[w], out[v], int(et[0]), int(et[1])]
	
	if len(set(fin)) != len(fin):
		print('\n')
		print('[-] Incorrect:', numbers)
		q += 1
	else:
		if 0 not in set(fin):
			if d<100:
				print('\n\n')
				print('CORRECT!!!')
				print(numbers)
				print(a)
				print("x"+str(e))
				print('--')
				print(b)
				print('+' +str(c))
				print('--')
				print(d)
				print('\n\n')
				quit()
			else:
				print('\n')
				print('[-] Incorrect:', numbers)
				q = q + 1
		else:
			print('\n')
			print('[-] Incorrect:', numbers)
			q = q + 1

else:
	print('\n\nNone\n\n')