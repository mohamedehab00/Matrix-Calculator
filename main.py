class Matrix:
    # Matrix Constructor
    def __init__(self, rows=0, cols=0):
        self.matrix = []
        self.setRows(rows)
        self.setCols(cols)

    # Operators Overloading
    def __add__(self, other):
        M = Matrix(self.getRows(), self.getCols())
        if isinstance(other, Matrix):
            for i in range(self.getRows()):
                temp = list()
                for j in range(self.getCols()):
                    temp.append(self.matrix[i][j]+other.matrix[i][j])
                M.matrix.append(temp)
        else:
            print("Can't make addition!!!")
        return M

    def __sub__(self, other):
        M = Matrix(self.getRows(), self.getCols())
        if isinstance(other, Matrix):
            for i in range(self.getRows()):
                temp = list()
                for j in range(self.getCols()):
                    temp.append(self.matrix[i][j] - other.matrix[i][j])
                M.matrix.append(temp)
        else:
            print("Can't make subtraction!!!")
        return M

    def __mul__(self, other):
            M = Matrix(self.getRows(), self.getCols())
            if isinstance(other, Matrix):
                for i in range(self.getRows()):
                    temp = []
                    for j in range(other.getCols()):
                        res = 0
                        for k in range(self.getCols()):
                            res += self.matrix[i][k] * other.matrix[k][j]
                        temp.append(res)
                    M.matrix.append(temp)
            else:
                for i in range(self.getRows()):
                    temp = list()
                    for j in range(self.getCols()):
                        temp.append(self.matrix[i][j] * other)
                    M.matrix.append(temp)
            return M

    def __pow__(self, power, modulo=None):
        data = Matrix(self.getRows(), self.getCols())
        data.matrix = self.matrix
        powered = Matrix()
        for i in range(power-1):
            data = data * self
        powered = data
        return powered

    # Setters & Getters
    def setRows(self, value):
        self.__rows = value

    def setCols(self, value):
        self.__cols = value

    def getRows(self):
        return self.__rows

    def getCols(self):
        return self.__cols

    def __setMatrixItem(self, i, j, value):
        self.matrix[i][j] = value

    # This function checks if the values is a valid
    def __checkValue(self, rows, cols):
        if rows > 0 and cols > 0:
            return True
        else:
            return False

    # This function inputs the shape of the Matrix
    def __shapeInput(self):
        r, c = map(int,input("Enter The Shape of The Matrix : ").split())
        while not self.__checkValue(r, c):
            r, c = map(int,input("Enter a valid Shape : ").split())
        return r, c

    def set_shape(self):
        r, c = self.__shapeInput()
        self.setRows(r)
        self.setCols(c)


    # Transpose Function
    def transpose(self):
        temp = []
        for row in range(self.getRows()):
            sub_temp = []
            for col in range(self.getCols()):
                sub_temp.append(self.matrix[col][row])
            temp.append(sub_temp)
        self.matrix = temp

    # Determinant Functions
    @classmethod
    def __minMatrix(cls, Mtx, i, j):
        temp = [[0] * (len(Mtx.matrix) - 1) for i in range(len(Mtx.matrix) - 1)]
        n, m = 0, 0
        for x in range(len(Mtx.matrix)):
            for y in range(len(Mtx.matrix)):
                if x == i or y == j:
                    continue
                temp[n][m] = Mtx.matrix[x][y]
                m += 1
                if m == len(Mtx.matrix) - 1:
                    n += 1
                    m = 0
        new = Matrix()
        new.matrix = temp
        return new

    @classmethod
    def calculateDeterminant(cls, M):
        if len(M.matrix) == 2:
            return (M.matrix[0][0] * M.matrix[1][1]) - (M.matrix[0][1] * M.matrix[1][0])
        else:
            res = 0
            sign = 0
            i = 0
            for j in range(len(M.matrix)):
                if sign == 0:
                    res += M.matrix[i][j] * cls.calculateDeterminant(cls.__minMatrix(M, i, j))
                elif sign == 1:
                    res -= M.matrix[i][j] * cls.calculateDeterminant(cls.__minMatrix(M, i, j))
                sign = 1 - sign
            return res

    # Inverse Functions
    def cofactor(self):
        Cof = Matrix(self.getRows(), self.getCols())
        cof = []
        sign = 1
        for row in range(self.getRows()):
            sub_cof = []
            for col in range(self.getCols()):
                temp = Matrix.__minMatrix(self, row, col)
                new_dta = Matrix.calculateDeterminant(temp)
                sub_cof.append(sign*new_dta)
                sign = -(sign)
            cof.append(sub_cof)
        Cof.matrix = cof
        return Cof

    def adjoint(self):
        adj = self.cofactor()
        adj.transpose()
        return adj

    def inverse(self):
        inv = Matrix(self.getRows(), self.getCols())
        if len(self.matrix) == 1:
            inv = self
        elif len(self.matrix) == 2:
            data = self.matrix
            data[0][0], data[1][1] = (data[1][1]), (data[0][0])
            data[0][1], data[1][0] = -(data[1][0]), -(data[0][1])
            inv.matrix = data
            inv = inv * (1/Matrix.calculateDeterminant(self))
            inv.transpose()
        else:
            inv = self.adjoint() * (1/Matrix.calculateDeterminant(self))
        return inv

    # Cast the Matrix from float to int
    def float_T_int(self):
        for i in range(self.getRows()):
            for j in range(self.getCols()):
                self.matrix[i][j] = int(self.matrix[i][j])
        return self

    # This function inputs the Matrix
    def matrixInput(self):
        self.matrix.clear()
        self.set_shape()
        print('Enter the Elements of The Matrix :')
        for i in range(self.getRows()):
            temp = list()
            for j in range(self.getCols()):
                temp.append(int(input("Element[ "+str(i)+" ][ "+str(j)+" ] = ")))
            self.matrix.append(temp)

    # This function prints the Matrix
    def printMatrix(self):
        for i in range(self.__rows):
            if i == 0:
                print('[', end="")
            if i == 0:
                print('[', end='')
            else:
                print('[', end=' ')

            for j in range(self.__cols):
                if j == self.__cols-1:
                    print(self.matrix[i][j], end='')
                else:
                    print(self.matrix[i][j], end=',')
            if i == self.__rows-1:
                print(']]')
            else:
                print(']')
# The main menu
def menu():
    print("  Matrix Calculator  ".center(50,'*'))
    print("""
    # 1- add two matrices
    # 2- subtract two matrices
    # 3- multiply matrix with scalar
    # 4- multiply two matrices
    # 5- divide two matrices
    # 6- get the power of matrix
    # 7- get the inverse of matrix
    # 8- Transpose matrix
    # 9- calculate determinant
    """)
    choice = int(input("Choice : "))
    if choice < 1 or choice > 9:
         menu()
    if choice == 1:
        M1 = Matrix()
        M1.matrixInput()
        M2 = Matrix()
        M2.matrixInput()
        M3 = M1 + M2
        M3.printMatrix()
    elif choice == 2:
        M1 = Matrix()
        M1.matrixInput()
        M2 = Matrix()
        M2.matrixInput()
        M3 = M1 - M2
        M3.printMatrix()
    elif choice == 3:
        constant = int(input("Enter the constant : "))
        M1 = Matrix()
        M1.matrixInput()
        M2 = M1 * constant
        M2.printMatrix()
    elif choice == 4:
        M1 = Matrix()
        M1.matrixInput()
        M2 = Matrix()
        M2.matrixInput()
        M3 = M1 * M2
        M3.printMatrix()
    elif choice == 5:
        M1 = Matrix()
        M1.matrixInput()
        M2 = Matrix()
        M2.matrixInput()
        M3 = M1 * M2.inverse()
        M3 = M3.float_T_int()
        M3.printMatrix()
    elif choice == 6:
        constant = int(input("Enter the constant : "))
        M1 = Matrix()
        M1.matrixInput()
        M2 = M1 ** constant
        M2.printMatrix()
    elif choice == 7:
        M1 = Matrix()
        M1.matrixInput()
        inv = M1.inverse()
        inv.printMatrix()
    elif choice == 8:
        M1 = Matrix()
        M1.matrixInput()
        M1.transpose()
        M1.printMatrix()
    elif choice == 9:
        M1 = Matrix()
        M1.matrixInput()
        print(Matrix.calculateDeterminant(M1))

# The main function
if __name__ == '__main__':
    while True:
        menu()
        choice = input('Do you want to exit??? [y/Y] [n/N]')
        if choice in ['Y','y']:
            break