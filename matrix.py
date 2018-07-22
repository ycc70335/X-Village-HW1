import random

class Matrix:

    def __init__(self, name, nrows, ncols):
        """Construct a (nrows X ncols) matrix"""
        # define an new matrix R
        R = []
        print("Enter ", name, " matrix's rows: ", nrows)
        print("Enter ", name, " matrix's cols: ", ncols)
        for i in range(0, nrows):
            R.append([])
            for j in range(0, ncols):
                R[i].append(random.randint(0,9))
        for i in range(0, nrows):
            for j in range(0, ncols):
                print(R[i][j],end=' ')
            print('')
        print('')
        self.R = R
        self.nrows = nrows
        self.ncols = ncols

    # return value to another matrix 
    def get(self):
        return self.R

    def add(self, m):
        """return a new Matrix object after summation"""
        C = []
        if self.nrows == len(m) and self.ncols == len(m[0]):
            for i in range(0, self.nrows):
                C.append([])
                for j in range(0, self.ncols):
                    C[i].append(self.R[i][j] + m[i][j])
        self.C = C
        self.m_add = m

    def sub(self, m):
        """return a new Matrix object after substraction"""
        D = []
        if self.nrows == len(m) and self.ncols == len(m[0]):
            for i in range(0, self.nrows):
                D.append([])
                for j in range(0, self.ncols):
                    D[i].append(self.R[i][j] - m[i][j])
        self.D = D
        self.m_sub = m
        pass

    def mul(self, m):
        """return a new Matrix object after multiplication"""
        E = []
        if self.nrows == len(m[0]) and self.ncols == len(m):
            for i in range(0, self.nrows):
                E.append([])
                for j in range(0, len(m[0])):
                    E[i].append(0)
                    for k in range(0, len(m[0])):
                        E[i][j] += self.R[i][k] * m[k][j]
        self.E = E
        self.m_mul = m
        pass

    def transpose(self):
        """return a new Matrix object after transpose"""
        F = []
        if self.nrows == len(self.m_mul[0]) and self.ncols == len(self.m_mul):
            for i in range(0, self.nrows):
                F.append([])
                for j in range(0, len(self.m_mul[0])):
                    F[i].append(self.E[j][i])
        self.F = F
        pass

    def display(self):
        """Display the content in the matrix"""
        
        print('========== A + B ==========')
        if self.nrows == len(self.m_add) and self.ncols == len(self.m_add[0]):
            for i in range(0, self.nrows):
                for j in range(0, self.ncols):
                    print(self.C[i][j],end=' ')
                print('')
            print('')
        else:
            print("Matrixs' size should be in the same size.")      
        
        print('========== A - B ==========')
        if self.nrows == len(self.m_sub) and self.ncols == len(self.m_sub[0]):
            for i in range(0, self.nrows):
                for j in range(0, self.ncols):
                    print(self.D[i][j],end=' ')
                print('')
            print('')
        else:
            print("Matrixs' size should be in the same size.") 

        print('========== A * B ==========')
        if self.nrows == len(self.m_mul[0]) and self.ncols == len(self.m_mul):
            for i in range(0, self.nrows):
                for j in range(0, len(self.m_mul[0])):
                    print(self.E[i][j],end=' ')
                print('')
            print('')
        else:
            print("Matrixs' size should be in the same size.") 
        
        print('========== the transpose of A * B ==========')
        if self.nrows == len(self.m_mul[0]) and self.ncols == len(self.m_mul):
            for i in range(0, self.nrows):
                for j in range(0, len(self.m_mul[0])):
                    print(self.F[i][j], end=' ')
                print('')
        else:
            print("Matrixs' size should be in the same size.") 

A = Matrix('A',5,7)
B = Matrix('B',7,5)
A.add(B.get())
A.sub(B.get())
A.mul(B.get())
A.transpose()
A.display()