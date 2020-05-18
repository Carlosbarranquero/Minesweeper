# -*- coding: utf-8 -*-
"""
Created on Sun May 17 20:02:02 2020

@author: Carlos Barranquero Díez
"""
import numpy as np
import pandas as pd
import time

from tabulate import tabulate


class MineSweeper:
    
    def __init__(self, rows_number, columns_number, dificulty):
        
        self.rows_number = rows_number
        self.columns_number = columns_number
        self.dificulty = dificulty # max 10 
        
        self.solve_matrix = self.build_grid_solution()
        self.play_matrix = self.build_grid_playable()


    def build_grid_solution(self):
        
        solution_grid = np.random.randint(-1, self.dificulty , size=(self.rows_number, self.columns_number))
        
        solve_matrix = pd.DataFrame(solution_grid)
        
        for column in range(len(solve_matrix)):
            
            for row in range(len(solve_matrix)):
                
                if(solve_matrix.iloc[row,column] != -1):
                    
                    solve_matrix.loc[row,column] = self.count_mines_around(solve_matrix,row,column)
                    
        return solve_matrix
    
    
    def build_grid_playable(self):
    
        play_grid = np.random.randint(-1, self.dificulty , size=(self.rows_number, self.columns_number))
        
        play_matrix = pd.DataFrame(play_grid)
        
        for column in range(len(play_matrix)):
            
            for row in range(len(play_matrix)):
                
                play_matrix.loc[row, column] = "xxx"
                
        return play_matrix
            

    def count_mines_around(self, solve_matrix, row, col):
    
        count_mines = 0
        
        #arriba_izq
        try:
            if(solve_matrix.iloc[row-1, col-1] == -1 and row != 0 and col!= 0):
                count_mines = count_mines + 1
        except:
            print("")
        
        #arriba_medio
        try:
            if(solve_matrix.iloc[row-1, col] == -1 and row != 0):
                count_mines = count_mines + 1
        except:
            print("")
            
        #arriba_derecha
        try:
            if(solve_matrix.iloc[row-1, col+1] == -1 and row != 0  and col != self.columns_number-1):
                count_mines = count_mines + 1
        except:
            print("")
        
        #medio_izq
        try:
            if(solve_matrix.iloc[row, col-1] == -1 and col != 0):
                count_mines = count_mines + 1
        except:
            print("")
            
        #medio_der
        try:
            if(solve_matrix.iloc[row, col+1] == -1 and col != self.columns_number-1):
                count_mines = count_mines + 1
        except:
            print("")
            
        #abajo_izq
        try:
            if(solve_matrix.iloc[row+1, col-1] == -1  and col!= 0 and row != self.rows_number-1):
                count_mines = count_mines + 1
        except:
            print("")
            
        #abajo medio    
        try:
            if(solve_matrix.iloc[row+1, col] == -1 and row != self.rows_number-1):
                count_mines = count_mines + 1
        except:
            print("")
            
        #abajo_der
        try:
            if(solve_matrix.iloc[row+1, col+1] == -1 and row != self.rows_number-1 and col!=self.columns_number-1):
                count_mines = count_mines + 1
        except:
            print("")
        
        return count_mines

    def show_cells_around(self, row, col):
        
        #arriba_izq
        try:
            if(row != 0 and col!= 0):
                self.play_matrix.loc[row-1, col-1] = self.solve_matrix.iloc[row-1, col-1] 
                    
        except:
            print("")
        
        #arriba_medio
        try:
            if(row != 0):
                self.play_matrix.loc[row-1, col] = self.solve_matrix.iloc[row-1, col] 
        except:
            print("")
            
        #arriba_derecha
        try:
            if(row != 0  and col!=self.columns_number-1):
                self.play_matrix.loc[row-1, col+1] = self.solve_matrix.iloc[row-1, col+1]
        except:
            print("")
        
        #medio_izq
        try:
            if(col != 0):
                self.play_matrix.loc[row, col-1] = self.solve_matrix.iloc[row, col-1]
        except:
            print("")
            
        #medio_der
        try:
            if(col!=self.columns_number-1):
               self.play_matrix.loc[row, col+1] = self.solve_matrix.iloc[row, col+1]
        except:
            print("")
            
        #abajo_izq
        try:
            if(col!= 0 and row != self.rows_number-1):
                self.play_matrix.loc[row+1, col-1] = self.solve_matrix.iloc[row+1, col-1]
        except:
            print("")
            
        #abajo medio    
        try:
            if(row != self.rows_number-1):
                self.play_matrix.loc[row+1, col] = self.solve_matrix .iloc[row+1, col]
        except:
            print("")
            
        #abajo_der
        try:
            if(row != self.rows_number-1 and col!=self.columns_number-1):
                self.play_matrix.loc[row+1, col+1] = self.solve_matrix .iloc[row+1, col+1]
        except:
            print("")
        
        return  self.play_matrix



    def show_cell(self, row, colum):
        
        self.play_matrix.loc[row, colum] = self.solve_matrix.iloc[row, colum]
        
        if(self.solve_matrix.iloc[row, colum] == 0):
            
            self.show_cells_around(row,colum)
            
        elif(self.solve_matrix.iloc[row, colum] == -1):
            print("BOoooooooooooOM")
            print("Game over")
            print("Ctl + C")
            time.sleep(3*60)
            
        
        return self.play_matrix


# #utilities
        
    def count_zeros(self):
        
        c_ceros = 0
        
        for n_col in range(self.columns_number):
            
            for n_row in range(self.rows_number):
                
                if(self.play_matrix.iloc[n_row,n_col] == 0):
                    
                    c_ceros = c_ceros + 1
                    
        return c_ceros   
    
        
    def check_zeros(self):
        
        start_zeros = 0
        end_zeros = 1
        
        while(start_zeros != end_zeros):
            
            start_zeros = self.count_zeros()
            
        
            for n_col in range(self.columns_number):
                    
                for n_row in range(self.rows_number):
                    
                    if(self.play_matrix.iloc[n_row,n_col] == 0):
                        
                        self.show_cell(n_row, n_col)
                                   
            end_zeros = self.count_zeros()
            
        return self.play_matrix
    
  
    def check_cell(self, r, c):
        
        if(self.solve_matrix.iloc[r,c] == -1):
            
            self.play_matrix.iloc[r,c] = " * "
            
            self.game_state()
            
        else:
            print("Game over!")
            print("Ctl + c")
            time.sleep(3*60)
            
            
        return self.play_matrix
    
        
    def make_a_roll(self, r, c):
        
        self.show_cell(r, c)
        
        self.check_zeros()
        
        is_play = self.game_state()
        
        return is_play, self.play_matrix
    
    
    def game_state(self):
        is_play=True
        discovered =0 
        real = 0 
        
        for n_col in range(self.columns_number):
                    
                for n_row in range(self.rows_number):
                    
                    if(self.play_matrix.iloc[n_row,n_col] == " * "):
                        
                        discovered = discovered + 1
                        
                    
        for n_col in range(self.columns_number):
                    
                for n_row in range(self.rows_number):
                    
                    if(self.solve_matrix.iloc[n_row,n_col] == -1):
                        
                        real = real + 1
                        
        print("mines discovered:", discovered, "/", real)                        
        
        if(discovered == real):
            is_play=False
        
        return is_play
    




def main():
    print("*****************************************************")
    print("Welcome to Minesweeper!!")
    print("")
    print("Intructions:")
    print("")
    print("1) To show a cell enter the coordinates directly (row, columns)")
    print("")
    print("2) If you want to deactivate a mine, you must enter the symbol '*' followed by the coordinates")
    print("")
    print("3) To start playing enter the number of rows, columns and the dificulty")
    print("*****************************************************")
    
    print("Rows number")
    
    rows = input()
    
    print("Columns number")
    
    columns = input()
    
    print("Dificulty (five is fine)")
    
    dificulty = input()
    
    game = MineSweeper(int(rows),int(columns), int(dificulty))
    
    is_play =True
    
    print(tabulate(game.play_matrix,  headers='keys', tablefmt='grid'))
    
    while(is_play):
        
        print("show cell:")
        
        print("row")
    
        r = input()
        
        if(r != "*"):
        
            print("column")
        
            c = input()
        
            is_play, play = game.make_a_roll(int(r),int(c))
            
            print(tabulate(play,  headers='keys', tablefmt='grid'))
            
            print("\n")
            
        else:
            
            print("Deactivate mine!!!")
            
            print("row")
        
            r = input()
        
            print("column")

            c = input()
        
            play = game.check_cell(int(r),int(c))
        
            print(tabulate(play,  headers='keys', tablefmt='grid'))
                

    print("YOU WIN !!!!!!!!!")    
    
    
    

if __name__ == "__main__":
    main()

