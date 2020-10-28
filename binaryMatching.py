def binaryPatternMatching(pattern, s):
	letters = []		   
	for char in s:	  
		if char.lower() not in 'aeiouy':
			letters.append('1') 
		else:
			letters.append('0')		
	print(letters)
	newLetter = ''.join(letters)
	pat = pattern
	M = len(pat) 
	N = len(s) 
	res = 0
  
	# A loop to slide pat[] one by one 
	# for i in range(N): 
	i = 0
	j = M
	while(i + j <= N): 
		print(newLetter[i:i + j])
		if (newLetter[i:i + j] == pat): 
			res = res + 1
		i += 1
  
		# # If pat[0...M-1] = txt[i, i+1, ...i+M-1] 
		# if (j == pat): 
		# 	res += 1
		# 	j = 0	
	return res

print(binaryPatternMatching('010', 'amazing')	)	