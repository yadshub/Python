import time


def biggestPlus(matrix):
  mat = [[int(i) for i in y] for y in matrix]
  h = len(mat[0])
  v = len(mat)
  n = 0

  if h <= 1000 and v <= 5000:

  # matrix to store 1's count
    left = [[0 for x in range(h)] 
        for y in range(v)] 
    right = [[0 for x in range(h)] 
          for y in range(v)] 
    top = [[0 for x in range(h)] 
        for y in range(v)] 
    bottom = [[0 for x in range(h)] 
          for y in range(v)] 

  #   # initialize above four matrix 
    for i in range(h): 
      
      # initialize first row of top 
      top[0][i] = mat[0][i] 

      # initialize last row of bottom 
      bottom[v - 1][i] = mat[v - 1][i] 

    for i in range(v): 
      # initialize first column of left 
      left[i][0] = mat[i][0] 

      # initialize last column of right 
      right[i][h - 1] = mat[i][h - 1] 

    # fill all cells of above four matrix 
    for i in range(v): 
      for j in range(1, h): 
        
        # calculate left matrix (filled 
        # left to right) 
        if (mat[i][j] == 1): 
          left[i][j] = left[i][j - 1] + 1
        else: 
          left[i][j] = 0

        # calculate new value of j to calculate 
        # value of bottom(i, j) and right(i, j) 
        k = h - 1 - j 

        # calculate right matrix 
        if (mat[i][k] == 1): 
          right[i][k] = right[i][k + 1] + 1
        else: 
          right[i][k] = 0

    for i in range(h): 
      for j in range(1, v): 
        
        # calculate top matrix 
        if (mat[j][i] == 1): 
          top[j][i] = top[j - 1][i] + 1
        else: 
          top[j][i] = 0

        # calculate new value of j to calculate 
        # value of bottom(i, j) and right(i, j) 
        k = v - 1 - j 

        # calculate bottom matrix 
        if (mat[k][i] == 1): 
          bottom[k][i] = bottom[k + 1][i] + 1
        else: 
          bottom[k][i] = 0


    # n stores length of longest '+' 
    # found so far 

    # compute longest + 
    for i in range(v): 
      for j in range(h): 
        
        # find minimum of left(i, j), 
        # right(i, j), top(i, j), bottom(i, j) 
        l = min(min(top[i][j], bottom[i][j]), 
            min(left[i][j], right[i][j])) 

      #   print(l)

        # largest + would be formed by 
        # a cell that has maximum value 
        if(l > n): 
          n = l - 1

    # 4 directions of length n - 1 and 1 
    # for middle cell 

    if (n): 
      return n

    # matrix contains all 0's 
    return 0
  return ""



# Driver Code 
if __name__=="__main__": 
  
  # Binary Matrix of size N 
  mat = ["0010010", 
 "1010101", 
 "1111111", 
 "0010000", 
 "0000000"] 
  start_time = time.time()
  print(biggestPlus(mat)) 
  print("--- %s seconds ---" % (time.time() - start_time))


