import math







from cmath import sqrt
from random import getrandbits
from webbrowser import get


def create_grid(n):
    return [[0 for i in range(n)] for i in range(n)]


def get_region_size(su):
    return int(math.sqrt(su))

def sudoku_to_str1(grid):
    [print(*row) for row in grid]



def sudoku_to_str(grid,compact):
    if not compact :
        sudoku_to_str1(grid)
    else :
        reg_size = get_region_size(len(grid) )
        i=0
        for row in grid:
            if i%reg_size==0 : print("\n")
            i+=1
            j=0
            for e in row : 
                if j%reg_size==0 : print(end="  ")
                j=j+1
                if (e==0) : print("_", end =' ') 
                else : print(e, end =' ') 
            print("  \n")


def load_sudoku(n,s):
    rows = s.split("\n")
    size = len(rows[0])
    grid = create_grid(size)
    for row in range(size):
        for j in range(size):
            grid[row][j]=int(rows[row][j])
    return grid
    

def numbers_in_line(su, i):
    res=[False]*(len(su)+1)
    for el in su[i]:
        res[el]=True
    res[0]=False
    return res


def numbers_in_column(su, i):
    res=[False]*(len(su)+1)
    for line in range(len(su)):
        res[su[line][i]]=True
    res[0]=False
    return res



def numbers_in_region(su, i, j):
    res=[False]*(len(su)+1)
    size = get_region_size(len(su))
    for l in range(size):
        for c in range(size):
            res[su[l+i][c+j]]=True
    res[0]=False
    return res 


def region_of_cell(su, i, j):
    size = get_region_size(len(su))
    return [ i-(i%size), j-(j%size)]

def help_me(su, i, j) : 
    res = []
    col = numbers_in_column(su,j)
    line = numbers_in_line(su,i)
    cor = region_of_cell(su,i,j)
    reg = numbers_in_region(su,cor[0],cor[1])

    for k in range(1,len(line)):
        if not(col[k] or line[k] or reg[k]) : 
            res.append(k)
    return res 

def solve_one_easy(su): 
    size = len(su)
    for i in range(size):
        for j in range(size):
            if su[i][j] == 0 : 
                hm = help_me(su,i,j)
                if (len(hm)==1) : 
                    su[i][j]=hm[0]
                    return [i,j]
    return []

def solve_easy(su) : 
    if solve_one_easy(su) != [] : solve_easy(su)



# tests : 
# print(create_grid(2))
# print(get_region_size(9))
new_su9 = create_grid (9)
new_su9 [1][7] = 4
# print ( sudoku_to_str1 ( new_su9) )
# print ( sudoku_to_str ( new_su9,True ) )


my_su9_str = "080030010\n063000204\n009260007\n000073005\n050040921\n000500470\n840390006\n002000000\n000004000\n"
my_su4_str = "0000\n0300\n0010\n2000\n"
my_su4 = load_sudoku (4 , my_su4_str )
my_su9 = load_sudoku (9 , my_su9_str )
# print(sudoku_to_str(my_su4,True))
# print(numbers_in_line(my_su4, 2))
# print(numbers_in_column(my_su4, 1))
# print(numbers_in_region(my_su4, 2, 0))
# print(region_of_cell(my_su4, 3, 2))
# print(help_me(my_su4, 2, 1))
# print(help_me(my_su9, 0, 6))

# print(solve_one_easy(create_grid(4)))
# print(solve_one_easy(my_su4))
# print(solve_one_easy(my_su9))


solve_easy ( my_su4 )
solve_easy ( my_su9 )
print ( sudoku_to_str ( my_su4 , False ) )
print ( sudoku_to_str ( my_su9 , False ) )



