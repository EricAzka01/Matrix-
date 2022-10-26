#Linear Algebra
#Eric Azka Nugroho
#5025211064

#Function to create a minor matrix (to solve cofactor)
def CreateMinorMatrix(Matrix, selected_row, selected_col):
    minormatrix = []

    #Selecting the pivot rows and columns to be calculate as minor matrix
    for i in range(len(Matrix)):
        temp = []
        for j in range(len(Matrix[i])):
            if i != selected_row and j != selected_col:
                temp.append(Matrix[i][j])
        if len(temp) != 0:
                minormatrix.append(temp)

    return minormatrix


#Function to transpose matrix to calculate inverse function
def TransposingMatrix(Matrix):
    matrixtranspose = []

    for i in range(len(Matrix[0])):
        temp = []
        for j in Matrix:
            temp.append(j[i])
        matrixtranspose.append(temp)

    return matrixtranspose



#Function to calculate determinants
def CalculateDeterminants(Matrix, axis=0):
    if len(Matrix) == 1:
        return Matrix[0][0]
    elif len(Matrix) == 2:
        return (Matrix[0][0] * Matrix[1][1]) - (Matrix[0][1] * Matrix[1][0])
    else:
        determinants = 0
        i = axis
        for j in range(len(Matrix)):
            cofactor = (-1)**(i + j) * Matrix[i][j] * CalculateDeterminants(
                CreateMinorMatrix(Matrix, i, j))
            determinants += cofactor
        return determinants

#Function to calculate inverse
def CalculateInverse(Matrix):
    # Build the determinant matrix
    determinant_matrix = []


    for i in range (len(Matrix)):
        temp = []
        for j in range(len(Matrix[i])):
            temp.append(CalculateDeterminants(CreateMinorMatrix(Matrix, i, j)))
        determinant_matrix.append(temp)

    #Then, transpose the determinant
    #Then, multiply with 1/determinant

    InverseMatrix = TransposingMatrix(determinant_matrix)
    Determinants = CalculateDeterminants(Matrix)

    for i in range(len(InverseMatrix)):
        for j in range(len(InverseMatrix[i])):
            InverseMatrix[i][j] = (-1)**(i + j) * InverseMatrix[i][j] * (1.0 / Determinants)

    return InverseMatrix



def main():
    #Initialization of Matrix
    Matrix = []

    print("Project Linear Algebra!")
    print("Enter the number of rows: ")
    rows = int(input())

    #The program will not run if the number of rows is less than 1
    if rows < 1:
        print("Matrix can't be done")
        return

    print("Input the elements of Matrix: ")
    print("Write it down seperately, ex: 1 2 3")

    #Looping for user to input the number of elements
    for i in range(rows):
        elements = input("Row  " + str(i + 1) + ":")
        Matrix.append([float(v) for v in elements.split()])


    for i in range(len(Matrix)):
        if rows != len(Matrix[i]):
            print("Matrix is not square")
            return

    print("Which Problems do you want to Solve: ")
    print("1. Determinants")
    print("2. Inverse")
    option = int(input())

    if option == 1:
        print(CalculateDeterminants(Matrix))

    if option == 2:
        if CalculateDeterminants(Matrix) == 0:
            print("Determinants are zero, therefore inverse does not exist")
        if CalculateDeterminants(Matrix) != 0:
            print("\n".join(["".join([f"{v:8.2f}" for v in row]) for row in CalculateInverse(Matrix)]))




if __name__ == "__main__":
    main()