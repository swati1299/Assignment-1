DIMENSION = 9
def read_matrix(filename):
	with open(filename, "r") as f:
		matrix = f.readlines()
		for i,row in enumerate(matrix):
			matrix[i] = list(map(int,matrix[i].split(",")))
	return matrix

def write_matrix(filename, solved_matrix):
	with open(filename, "w") as f:
		f.writelines(','.join(str(j) for j in i) + '\n' for i in solved_matrix)
	print(filename+" for backtracking generated.")

class sudoku():
	def __init__(self, filename):
		self.matrix = read_matrix(filename)

	def solve(self):
		a = self.is_the_cell_empty(0, 0)
		row = a[0]
		col = a[1]
		if a[2] == 0:
			return True

		end = a[2]
		if (end == 1):
			for i in range(9, 0, -1):
				if not self.is_a_good_entry(i, row, col):
					continue
				else:
					self.matrix[row][col] = i
					if self.solve():
						return True
					self.matrix[row][col] = 0
			return False

	def is_a_good_entry(self, n, r, c):
		start = 0
		for i in range(0, DIMENSION):
			if self.matrix[r][i] != n:
				start = start + 1;
				continue
			else:
				# print("broke after "+ start)
				return False
		for i in range(0, DIMENSION):
			if self.matrix[i][c] != n:
				continue
			else:
				return False
		retu = self.calculate(r, c)
		row_start = retu[0]
		col_start = retu[1]
		for i in range(row_start, row_start + 3):
			for j in range(col_start, col_start + 3):
				if self.matrix[i][j] != n:
					continue
				else:
					return False
		return True

	def is_the_cell_empty(self, row, col):
		num_unassign = 0
		check = 0
		for i in range(0, DIMENSION):
			ntrow = 0;
			for j in range(0, DIMENSION):
				ntrow = ntrow + 1;
				check = check + 1
				if (check == DIMENSION ** 2 or ntrow == DIMENSION):
					check = 0
				# print("reached the end")
				if self.matrix[i][j] == 0:
					a = [i, j, 1]
					return a
		a = [-1, -1, num_unassign]
		return a

	def calculate(self, r, c):
		y = (c // 3) * 3
		x = (r // 3) * 3
		z = [x, y, 1]
		return z

	# def number_unassigned(self, row, col):
	#     num_unassign = 0
	#     for i in range(0,SIZE):
	#         for j in range (0,SIZE):
	#             #cell is unassigned
	#             if self.matrix[i][j] == 0:
	#                 row = i
	#                 col = j
	#                 num_unassign = 1
	#                 a = [row, col, num_unassign]
	#                 return a
	#     a = [-1, -1, num_unassign]
	#     return a


	def solve_without_backtracking(self):
		
		MAT = []
		for i in self.matrix:
		    MAT = MAT + i

		# print(MAT)

		unassigned_index_list = []
		unassigned_index_list_2D = []
		for i in range(len(MAT)):
		    if MAT[i]==0:
		        unassigned_index_list.append(i)

		# print(unassigned_index_list)

		for i in unassigned_index_list:
		    unassigned_index_list_2D.append([i//9,i%9])

		# print(unassigned_index_list_2D)

		# for i in unassigned_index_list_2D:
		#     print(self.matrix[i[0]][i[1]])

		LEN = len(unassigned_index_list)
		# print(LEN)

		soln_list = [str(i) for i in range(1,10)]
		new_soln_list = []
		possible_solns = []

		for i in unassigned_index_list_2D:
		    # print(i)
		    possibility_at_that_index =[]
		    for j in range(1,10):
		        if self.is_a_good_entry(j, i[0], i[1]):
		            possibility_at_that_index.append(j)
		    possible_solns.append(possibility_at_that_index)
		    possibility_at_that_index = []

		#print("List of possible values : ")
		#print(possible_solns)
		#print()

		for_sorted_index_order = [len(i) for i in possible_solns]
		sorted_index_order = [] 


		for i in range(1,10):
		    for j in range(len(for_sorted_index_order)):
		        if for_sorted_index_order[j] == i:
		            sorted_index_order.append(j)

		# print(for_sorted_index_order)
		# print(sorted_index_order)


		working_at = 0
		while(True):
		    # print(working_at)
		    if(working_at==(-1)):
		        print("NO SolN using solve_without_backtracking ")
		        break
		    if(working_at==len(unassigned_index_list)):
		        print("Solved using solve_without_backtracking ")
		        break
		    i,j = unassigned_index_list_2D[sorted_index_order[working_at]][0],unassigned_index_list_2D[sorted_index_order[working_at]][1]
		    # print(i,j)
		    possibility_at_that_index = possible_solns[sorted_index_order[working_at]]

		    if self.matrix[i][j]==0:
		        index = -1
		    else:
		        index = possibility_at_that_index.index(self.matrix[i][j])
		    while(True):
		        # print("i am at 84")
		        if self.matrix[i][j] == possibility_at_that_index[-1]:
		            self.matrix[i][j] = 0
		            index = -1
		            working_at = working_at - 1
		            break
		        else:
		            trying = possibility_at_that_index[index+1]
		            index = index + 1
		            if self.is_a_good_entry(trying, i, j):
		                self.matrix[i][j] = trying
		                working_at = working_at+1
		                break
		            else:
		                self.matrix[i][j] = trying

		 

if __name__=="__main__":
	su = sudoku("data.txt")
	su.solve()
	write_matrix("sol.txt", su.matrix)
	#print(su.matrix)
	try:
		su = sudoku("data.txt")
		su.solve_without_backtracking()
		print("Solved sudoku matrix without backtracking:")
		for i in range(9):
			print(*su.matrix[i], sep=" ")
	except Exception as e:
		print(e)



