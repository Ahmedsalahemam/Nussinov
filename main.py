# your code goes here# your code goes here# your code goes here
RNAsequence = input("Enter the RNA sequecne\n")
RNAsequence = RNAsequence.lower()

n = len(RNAsequence)
matrix = []


def initializematrix(matrix, n):
    for i in range(n):
        col = []
        for j in range(n):
            col.append(0)
        matrix.append(col)
        matrix[i][i] = 0
        if i > 0:
            matrix[i][i - 1] = 0


def bifurication(matrix, n, start, end):
    mx = 0
    s = 0
    e = 0
    s = min(start, end)
    e = max(start, end)
    for k in range(s + 1, e):
        mx = max(mx, matrix[start][k] + matrix[k + 1][end])
    return mx


def printMatrix():
    for i in range(n):
        print(matrix[i])


def fillmatrix(matrix, n):
    for s in range(1, n):
        for i in range(0, n - 1):
            j = s + i
            if j >= n: break
            left = matrix[i][j - 1]
            down = matrix[i + 1][j]
            if RNAsequence[i] == 'c' and RNAsequence[j] == 'g':
                diagonal = matrix[i + 1][j - 1] + 1
            elif RNAsequence[i] == 'g' and RNAsequence[j] == 'c':
                diagonal = matrix[i + 1][j - 1] + 1
            elif RNAsequence[i] == 'a' and RNAsequence[j] == 'u':
                diagonal = matrix[i + 1][j - 1] + 1
            elif RNAsequence[i] == 'u' and RNAsequence[j] == 'a':
                diagonal = matrix[i + 1][j - 1] + 1
            # elif RNAsequence[i] == 'g' and RNAsequence[j] == 'u':   in case wooble pair
            #     diagonal = matrix[i + 1][j - 1]+1
            # elif RNAsequence[i] == 'u' and RNAsequence[j] == 'g':
            #     diagonal = matrix[i + 1][j - 1]+1
            else:
                diagonal = matrix[i + 1][j - 1]

            burif = bifurication(matrix, n, i, j)
            matrix[i][j] = max(left, diagonal, down, burif)
            # print (i,' ',j)
            # printMatrix()
            #
            # print('\n')


initializematrix(matrix, n)
fillmatrix(matrix, n)
printMatrix()


# print("I am here !!!")

# so2ale, hoa e7na m4 bnm4e diagonal fe L pair & bno2f 3nd L cell L max
# fe 7alet L unpaired!!

def traceback():
    x = 0
    y = n - 1
    str1 = ''
    str2 = ''
    while matrix[x][y] != 0 and x < n and y >= 0:
        if RNAsequence[x] == 'c' and RNAsequence[y] == 'g':
            str1 += '('
            c = ')'
            c += str2
            str2 = c
            x = x + 1
            y = y - 1


        elif RNAsequence[x] == 'g' and RNAsequence[y] == 'c':
            str1 += '('
            c = ')'
            c += str2
            str2 = c
            x = x + 1
            y = y - 1

        elif RNAsequence[x] == 'a' and RNAsequence[y] == 'u':
            str1 += '('
            c = ')'
            c += str2
            str2 = c
            x = x + 1
            y = y - 1

        elif RNAsequence[x] == 'u' and RNAsequence[y] == 'a':
            str1 += '('
            c = ')'
            c += str2
            str2 = c
            x = x + 1
            y = y - 1


        else:
            tempx = x
            tempy = y

            str1 += '.'
            c = '.'
            c += str2
            str2 = c

            mx = -100
            # check down!
            if matrix[x + 1][y] >= mx:
                mx = matrix[x + 1][y]
                x = tempx + 1

            # check left!
            if matrix[x][y - 1] >= mx:
                mx = matrix[x][y - 1]
                y = tempy - 1

            # check left diagonal!
            if matrix[x + 1][y - 1] >= mx:
                mx = matrix[x + 1][y - 1]
                x = tempx + 1
                y = tempy - 1

    print(str1 + str2)


traceback()






