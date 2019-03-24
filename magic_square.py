def magic_sqaure(n):

	ms=[]
	for i in range(n):
		l=[]
		for j in range(n):
			l.append(0)
		ms.append(l)	 

	i = n//2
	j = n-1

	num = n*n
	count = 1

	while(count<=num):
		if i==-1 and j==n:
			i=0
			j=n-2
		else:
			if j==n:
				j=0

			if i<0:
				i=n-1
		
		if (ms[i][j]!=0):
			i=i+1
			j=j-2
			continue

		else:
			ms[i][j] = count
			count =count+1

		i=i-1
		j=j+1

	for i in range(n):
		for j in range(n):
			print(ms[i][j],end=" ")
		print()

	print("The sum of each row/column/diagonal is = " +str(n*(n**2+1)/2))

magic_sqaure(3)
