import random

class Matrix:

    def __init__(self, nrowsA, ncolsA, nrowsB, ncolsB):
        """Construct a (nrows X ncols) matrix"""
       #construct A[]
        A = []
        nrowsA = int(input("Enter A matrix's rows:"))
        ncolsA = int(input("Enter A matrix's cols:"))
        self.nrowsA = nrowsA
        self.ncolsA = ncolsA
        for i in range (0, self.nrowsA):
            A.append([])
            for j in range(0, self.ncolsA):
                A[i].append(random.randint(0,9))
        print("Matrix A:")
        for i in range(0, self.nrowsA):
            for j in range(0, self.ncolsA):
                print(A[i][j], end=" ")
            print()
        
        #construct B[]
        B = []
        nrowsB = int(input("Enter B matrix's rows:"))
        ncolsB = int(input("Enter B matrix's cols:"))
        self.nrowsB = nrowsB
        self.ncolsB = ncolsB
        for i in range (0, self.nrowsB):
            B.append([])
            for j in range(0, self.ncolsB):
                B[i].append(random.randint(0,9))
        print("Matrix B:")
        for i in range(0, self.nrowsB):
            for j in range(0, self.ncolsB):
                print(B[i][j], end=" ")
            print()
        
        #renew A[]&B[]
        self.A = A
        self.B = B
        pass

    def add(self, m):
        """return a new Matrix object after summation"""
        C = []
        if self.nrowsA == self.nrowsB and self.ncolsA == self.ncolsB :
            for i in range(0, self.nrowsA):
                C.append([])
                for j in range(0, self.ncolsA):
                    C[i].append(self.A[i][j] + self.B[i][j])
        self.C = C
        pass

    def sub(self, m):
        """return a new Matrix object after substraction"""
        D = []
        if self.nrowsA == self.nrowsB and self.ncolsA == self.ncolsB :
            for i in range(0, self.nrowsA):
                D.append([])
                for j in range(0, self.ncolsA):
                    D[i].append(self.A[i][j] + self.B[i][j])
        self.D = D
        pass

    def mul(self, m):
        """return a new Matrix object after multiplication"""
        E = []
        if self.ncolsA == self.nrowsB:
            for i in range(0, self.nrowsA):
                E.append([])
                for j in range (0, self.ncolsB):
                    E[i].append(0)
                    for k in range(0, self.ncolsA):
                        E[i][j] += self.A[i][k]*self.B[k][j]
        self.E = E
        pass

    def transpose(self):
        """return a new Matrix object after transpose"""
        F = []
        E = self.E
        if self.ncolsA == self.nrowsB:
            for i in range(0, self.nrowsA):
                F.append([])
                for j in range(0, self.ncolsB):
                    F[i].append(self.E[j][i])
        self.F = F
        pass
    
    def display(self):
        """Display the content in the matrix"""
        # add
        print("========== A + B ==========")
        C = self.C
        if self.nrowsA == self.nrowsB and self.ncolsA == self.ncolsB :
            for i in range(0, self.nrowsA):
                for j in range(0, self.ncolsA):
                    print(C[i][j], end=" ")
                print()    
        else:
            print("Matrixs' size should be in the same size")
        
        # sub
        print("========== A - B ==========")
        D = self.D
        if self.nrowsA == self.nrowsB and self.ncolsA == self.ncolsB :
            for i in range(0, self.nrowsA):
                for j in range(0, self.ncolsA):
                    print(D[i][j], end=" ")
                print()    
        else:
            print("Matrixs' size should be in the same size")
        
        # mul
        print("========== A * B ==========")
        E = self.E
        if self.ncolsA == self.ncolsB :
            for i in range(0, self.nrowsA):
                for j in range(0, self.ncolsA):
                    print(E[i][j], end=" ")
                print()    
        else:
            print("Matrixs' size is wrong")

        #transpose
        print("========== A * B transpose ==========")
        F = self.F
        if self.ncolsA == self.ncolsB :
            for i in range(0, self.ncolsA):
                for j in range(0, self.nrowsA):
                    print(F[i][j], end=" ")
                print()    
        else:
            print("Matrixs' size is wrong")
                
        pass

R = Matrix(1, 1, 1, 1)
R.add(1)
R.sub(1)
R.mul(1)
R.transpose()
R.display()