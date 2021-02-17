# from headers import *
# from objects import *
# from colorama import init

# # Power Ups Class
# class Powerup(Object):
#     def __init__(self, x, y):
#         Object.__init__(self, x, y)

# class Beam(Object):
#     def __init__(self, x, y):
#         self.shape=[0]*20
#         self.canplace=0
#         self.active=0
#         self.angle=0
#         self.onboard=0
#         self.kill=0

#         Objects.__init__(self, x, y)

#     def create_beam(self):
#         for i in range(len(self.shape)):
#             self.shape[i]=BEAM1
#         self.shape[0]=BEAM2
#         self.shape[BEAM_SIZE-1]=BEAM3

       
#     def check_beam(self, x,y, task, grid):
#         #While placing beams
#         if(task==1):
#             #Nothing down
#             for i in range (y,y+BEAM_SIZE):
#                 if(grid[x][i]!=' '):
#                     return 1
#             for i in range (x, x+BEAM_SIZE):
#                 if(grid[i][y]!= ' '):
#                     return 1

#             for i in range (x, x+BEAM_SIZE):
#                 for j in range (y, y+BEAM_SIZE):
#                     if(i-x==j-y):
#                         if(grid[i][j]!=' '):
#                             return 1

#             return 0
    
#     def place_beam(self,angle, grid):
#         x = self.getx()
#         y = self.gety()
#         self.create_beam()
#         self.onboard=1 
#         #AVOID CROSSING BEAMS
#         if (x + BEAM_SIZE > HT-3 or x < 4 or y> WIDTH-30 or y+BEAM_SIZE > WIDTH-10):
#             self.canplace=0
#             return
#         elif (self.check_beam(x,y,1,grid)):
#             self.canplace=0
#             return
#         self.canplace=1  
             
#         temp = 0
#         if(angle == 90):
#             for i in range(x, x+BEAM_SIZE):
#                 grid[i][y] = self.shape[temp]
#                 temp += 1
#         elif(angle == 0):
#             for i in range(y, y+BEAM_SIZE):
#                 grid[x][i] = self.shape[temp]
#                 temp += 1
#         elif(angle == 45):
#             for i in range(x, x+BEAM_SIZE):
#                 for j in range(y, y+BEAM_SIZE):
#                     if(i-x==j-y):
#                         grid[i][j] = self.shape[temp]
#                         temp += 1
    
#     def print_beam(self,angle,grid):
#         x = self.getx()
#         y = self.gety()
#         self.create_beam()
#         temp = 0
#         if(angle == 90):
#             for i in range(x, x+BEAM_SIZE):
#                 grid[i][y] = self.shape[temp]
#                 temp += 1
#         elif(angle == 0):
#             for i in range(y, y+BEAM_SIZE):
#                 grid[x][i] = self.shape[temp]
#                 temp += 1
#         elif(angle == 45):
#             for i in range(x, x+BEAM_SIZE):
#                 for j in range(y, y+BEAM_SIZE):
#                     if(i-x==j-y):
#                         grid[i][j] = self.shape[temp]
#                         temp += 1

#     def clear_beam(self,grid):
#         a=self.angle
#         if(a==0):
#             for i in range(self.gety(), self.gety()+20):
#                 grid[self.getx()][i]=" "
#         elif(a==90):
#             for i in range(self.getx(), self.getx()+20):
#                 grid[i][self.gety()]=" "
#         elif(a==45):
#             for i in range(self.getx(), self.getx()+20):
#                 for j in range(self.gety(), self.gety()+20):
#                     if(i-self.getx()==j-self.gety()):
#                         grid[i][j]= " "
           

# class Bullet(Objects):
#     def __init__(self,x,y):
#         self.shape=[["(","0",")"]]
#         self.start=0
#         self.active=0
#         self.__crash=0
#         Objects.__init__(self,x,y)

#     def set_crash(self,x):
#         self.__crash=x
    
#     def show_crash(self):
#         return self.__crash

#     def clear_bullet(self, grid):
#         x=self.getx()
#         y=self.gety()

#         for i in range(y-2,y+3):
#             if(grid[x][i]==COIN):
#                 grid[x][i]=COIN
#             else:
#                 grid[x][i]=' '
       
#     def shoot(self, grid):
#         self.clear_bullet(grid)

#         if(self.gety()+5 > WIDTH -10):
#             self.active =0
#         else:
#             if(self.active==0):
#                 self.sety(self.gety()+1)                    
#             else:
#                 for i in range(self.gety()-10, self.gety()+10):
#                     if(grid[self.getx()][i]==BEAM1 or grid[self.getx()][i]==BEAM2  or grid[self.getx()][i]==BEAM3):
#                         self.sety(i)
#                         self.set_crash(1)
#                 self.sety(self.gety()+5)
            
            
#             self.show(grid, self.shape,self.getx(),self.gety())
#             self.active=1


#     def check_collision(self, grid,dragon,task):
#         for i in range(3):
#             if(task==1 and grid[self.getx()][self.gety()+i]==BEAM1 or grid[self.getx()][self.gety()+i]==BEAM2 or grid[self.getx()][self.gety()+i]==BEAM3 ):
#                 self.set_crash(1)
#                 return 1
#             elif(task==2 and self.gety()>=dragon.getx() and dragon.gety()<=self.getx()<=dragon.gety()+9):
#                 if(factor<WIDTH-SCREEN-1):
#                     self.clear_bullet(grid)
#                 if(dragon.get_cankill()==1):
#                     dragon.dec_lives()
#                 self.active=0
#                 return 2
#         return 0
