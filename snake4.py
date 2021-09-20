M = 4
N = 4

def printf(mat):
    global M, N

    for i in range(M):

   
        if i % 2 == 0:
            for j in range(N):
                print(str(mat[i][j]),
                      end = " ")


        else:
            for j in range(N - 1, -1, -1):
                print(str(mat[i][j]),
                      end = " ")


mat = [[ 0, 2, 3, 4 ],
       [ 8, 0, 6, 5 ],
       [ 9, 10, 0, 12 ],
       [ 16, 15, 14, 0 ]]

printf(mat)
