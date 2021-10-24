# Q1

def custom_transpose(input_matrix):
	n = len(input_matrix)
	m = len(input_matrix[0])
	new = [[0 for i in range(n)] for j in range(m)]
	for i in range(n):
		for j in range(m):
			new[j][i] = input_matrix[i][j]
	return new

output = custom_transpose(([[10,8],[2,4],[1,7]]))
for i in range(len(output)):
	print(output[i])