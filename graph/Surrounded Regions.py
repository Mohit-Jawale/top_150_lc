class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROW,COL = len(board),len(board[0])
        def dfs(i,j):

            if i<0 or i>=ROW or j<0 or j>=COL:
                return
            if board[i][j]!='O':
                return    

            board[i][j] = '#'
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)
        
        for i in range(ROW):
            dfs(i,0)
            dfs(i,COL-1)

        for j in range(COL):
            dfs(0,j)
            dfs(ROW-1,j)

        for i in range(ROW):
            for j in range(COL):
                if board[i][j] =='O':
                    board[i][j]='X'
                elif board[i][j]=='#':
                    board[i][j]='O'




    
# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """

#         R, C = len(board), len(board[0])
#         convert = set()
#         edges = set()
#         flag = True
#         def dfs(r,c):
            
#             nonlocal flag, convert
        

#             if board[r][c]=="O" and (r,c) not in edges:
#                 board[r][c]="X"
#                 convert.add((r,c))
#                 if r+1<R:dfs(r+1,c)
#                 if c+1<C:dfs(r,c+1)
#                 if r>=1:dfs(r-1,c) 
#                 if c>=1:dfs(r,c-1)
#             if board[r][c]=="O" and (r,c) in edges:
#                  flag = False
       
      

#         for c in range(C):
#             if board[0][c] == 'O':
#                 edges.add((0,c))
#             if board[R-1][c]=='O':
#                 edges.add((R-1,c))

#         for r in range(R):
#             if board[r][0]=='O':
#                 edges.add((r,0))
#             if board[r][C-1]=='O':
#                 edges.add((r,C-1))                


#         for r in range(R):
#             for c in range(C):

#                 if board[r][c]== "O" and (r,c) not in edges:
#                     dfs(r,c)
#                     if not flag:
#                         for i,j in convert:
#                             board[i][j]='O'
                            
#                 convert =set()
#                 flag = True    


        
