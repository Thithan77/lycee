def coplanaire(u,v,w):
	alpha = None
	beta = None
	zeros = []
	if(0 in u+v+w):
		for i,j in enumerate(u+v+w):
			print(str(i)+" "+str(j))
			if(j == 0):
				zeros.append((i,i//3,i%3))
				#print(f"Index {i} vector {i//3} index {i%3}")
		for i in zeros:
			if(i[1] == 0):
				print("Skip")
			elif(i[1] == 1):
				beta = u[i[2]] / w[i[2]]
				#print(f"Beta {beta}")
			elif(i[1] == 2):
				alpha = u[i[2]] / v[i[2]]
				#print(f"Alpha {alpha} {i[0]}")
	if(alpha):
		if(beta == None and w[0] != 0):
			beta = (u[0] - v[0]*alpha)/w[0]
			#print(f"Beta {beta}")
		elif(beta == None and w[1] != 0):
			beta = (u[1] - v[1]*alpha)/w[1]
			#print(f"Beta {beta}")
		if(beta == None and w[2] != 0):
			beta = (u[2] - v[2]*alpha)/w[2]
			#print(f"Beta {beta}")
	if(beta):
		if(alpha == None and v[0] != 0):
			alpha = (u[0] - w[0]*beta)/v[0]
			#print(f"Beta {beta}")
		elif(alpha == None and w[1] != 0):
			alpha = (u[1] - v[1]*beta)/v[1]
			#print(f"Beta {beta}")
		if(alpha == None and w[2] != 0):
			alpha = (u[2] - v[2]*beta)/v[2]
			#print(f"Beta {beta}")
	if(alpha and beta):
		if(u[0] == alpha*v[0]+beta*w[0] and u[1] == alpha*v[1]+beta*w[1] and u[2] == alpha*v[2]+beta*w[2]):
			print("Colinéaires")
			return True
	else:
		beta = (u[0]*v[1] - u[1]*v[0])/(w[0]*v[1] - w[1]*v[0])
		#print(f"Beta {beta}")
		if(alpha == None and v[0] != 0):
			alpha = (u[0] - w[0]*beta)/v[0]
			#print(f"Alpha {alpha}")
		elif(alpha == None and w[1] != 0):
			alpha = (u[1] - v[1]*beta)/v[1]
			#print(f"Alpha {alpha}")
		if(alpha == None and w[2] != 0):
			alpha = (u[2] - v[2]*beta)/v[2]
			#print(f"Alpha {alpha}")
	if(alpha and beta):
		if(u[0] == alpha*v[0]+beta*w[0] and u[1] == alpha*v[1]+beta*w[1] and u[2] == alpha*v[2]+beta*w[2]):
			print("Colinéaires")
			return True
		else:
			print("Non colinéaires")
			return False
	else:
		print("Non colinéaires")
		return False	

if __name__ == "__main__":
	coplanaire((-5,2,1),(-1,-4,3),(3,-2,1))
	coplanaire((-7,4,-5),(2,-2,-4),(-21,6,-53))
	coplanaire((4,-3,5),(7,6,7),(3,5,3))
	coplanaire((-67,27,37),(-5,-3,-1),(7,-7,-7))