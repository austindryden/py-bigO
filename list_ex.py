listy = [2, 5, 76, -4, 200, 0, 9, 2, -3, 5]

def sumnums(a_list):
    tally = 0
    for i in a_list:
        tally += i
    print(tally)
print("sum the numbers")
sumnums(listy)

def largest(a_list):
    big = a_list[0]
    for  i in a_list:
        if i > big:
            big = i
    print(big)
print("largest number")
largest(listy)

def smallest(a_list):
    small = a_list[0]
    for i in a_list:
        if i < small:
            small = i
    print(small)
print("Smallest Number")
smallest(listy)

def even(a_list):
    for i in a_list:
        if i % 2 == 0:
            print(i)
print("Even Numbers")
even(listy)

def positive(a_list):
    for i in a_list:
        if i > 0:
            print(i)
print("Positive numbers printed")
positive(listy)



def positive2(a_list):
    new_list = []
    for i in a_list:
        if i > 0:
            new_list.append(i)
    return new_list
print("Positive numbers (returned as a list)")
print(positive2(listy))

def multiply_list(a_list, factor):
    new_list = []
    for i in a_list:
        new_list.append(i * factor)
    return new_list

print("Multiply a list")
print(multiply_list(listy, 5))

def mult_vectors(a_list, b_list):
    new_list = []
    if len(a_list) != len(b_list):
        print("Lists must be the same length")
        return
    for i in range(len(a_list)):
        new_list.append(a_list[i] * b_list[i])
    return new_list

print("Multiply Vectors")
print(mult_vectors(listy, listy))

def matrixAdd(a_list, b_list):
    new_list = []
    if len(a_list) != len(b_list):
        print("lists must be the same length")
        return
    for i in range(len(a_list)):
        new_row = []
        if len(a_list[i]) != len(b_list[i]):
            print("lists must be the same length")
            return
        for j in range(len(a_list[i])):
            new_row.append(a_list[i][j] + b_list[i][j])
        new_list.append(new_row)
    return new_list

print("Matrix addition 2")
print(matrixAdd([[1, 2], [3, 4]], [[5, 6], [7, 8]]))

def deDup(a_list):
    new_list =[]
    for i in a_list:
        not_found = True
        for j in new_list:
            if i == j:
                not_found = False
        if not_found:
            new_list.append(i)
    return new_list

print(deDup(listy))

def dotProd(a_list, b_list): #returns the dot product of 2 lists of equal length
    tally = 0
    for i in range(len(a_list)):
        tally += a_list[i] * b_list[i]
    return tally

def column(list, i): #returns column i in a matrix as a list
    new_list = []
    for row in list:
        new_list.append(row[i])
    return new_list

def matrixMult(a_list, b_list): #returns a 2d list(matrix) that is a product of the 2d lists(matricies) passed
    if (len(a_list[0])) != len(b_list):
        print("matricies must be multipliable")
        return
    new_list = []
    new_row_a = []
    new_row_b = []
    for i in range(len(a_list)):
        #row i in matrix a
        new_row_a = a_list[i]
        new_row = []
        for j in range(len(b_list[0])):
            new_row_b = column(b_list, j)
            new_row.append(dotProd(new_row_a, new_row_b))

        new_list.append(new_row)
        new_row = []
    return(new_list)

print("Matrix Multiplication")
print(matrixMult([[1, 3], [2, 4], [2, 5]], [[1, 3, 2, 2], [2, 4, 5, 1]]))
            
                
