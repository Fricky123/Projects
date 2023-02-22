import random

rows = []

def intro():
    line()
    print('Welcome to Minesweeper\n')

    x = input('Would you like to play? ').lower()
    if 'yes' in x:
        line()
        print('[1]Easy [2]Medium [3]Hard\n')
        y = input('Choose difficulty: ')
        if '1' in y[0]:
            grid('easy')
        elif '2' in y[0]:
            grid('medium')
        elif '3' in y[0]:
            grid('hard')
        else:
            invalid()
            intro()
        
    elif 'no' in x:
        print('Bye!')
        exit()
        
    else:
        invalid()
        intro()

def grid(difficulty):
    line()
            
    if difficulty == 'easy':
        generate_grid(1)
        bomb_generator('easy')
        
    elif difficulty == 'medium':
        generate_grid(2)
        bomb_generator('medium')
    
    elif difficulty == 'hard':
        generate_grid(3)
        bomb_generator('hard')
        
    else:
        invalid()
        intro()
    
def generate_grid(grid_number):

    def grid1():
        global rows
        rows = [['   | A | B | C | D | E |\n------------------------'],]
        
        loop = 5
        loop_current = 0
        while loop_current != loop:
            loop_current += 1
            
            rows.append([f' {loop_current} |', ' - |', ' - |', ' - |', ' - |', ' - |',])
                  
    def grid2():
        global rows
        rows = [['   | A | B | C | D | E | F | G |\n--------------------------------'],]
        
        loop = 7
        loop_current = 0
        while loop_current != loop:
            loop_current += 1
            
            rows.append([f' {loop_current} |', ' - |', ' - |', ' - |', ' - |', ' - |', ' - |', ' - |', ])
    
    def grid3():
        global rows
        rows = [['   | A | B | C | D | E | F | G | H | I |\n----------------------------------------'],]
        
        loop = 9
        loop_current = 0
        while loop_current != loop:
            loop_current += 1
            
            rows.append([f' {loop_current} |', ' - |', ' - |', ' - |', ' - |', ' - |', ' - |', ' - |', ' - |', ' - |', ])
    
    if grid_number == 1:
        grid1()
    elif grid_number == 2:
        grid2()
    elif grid_number == 3:
        grid3()
    else:
        print('error')

def bomb_generator(difficulty):
    global rows
    bombs = 5
    bombs_placed = 0
    
    if difficulty == 'easy':
        bombs = 5
    elif difficulty == 'medium':
        bombs = 7
    elif difficulty == 'hard':
        bombs = 9
        
    while bombs_placed != bombs:
        x = random.randint(1, bombs) 
        y = random.randint(1, bombs)

        rows[x][y] = ' O |'
        bombs_placed += 1

def print_grid():
    
    for row in rows:
        string = ''
        for x in row:
            string += x
            
        print(string)  
    
def game():
    try:
        print_grid()
        x = input('row: ').lower()
        
        if 'quit' in x:
            intro()
        else:
            x = int(x)
        
        y = input('column: ').lower()
        input('confirm? ')
        
        if check_spot(x, y) == 'bomb':
            change_spot(x, y, bomb=True)
            print_grid()
            print('[YOU LOST]')
            exit()
        
        change_spot(x, y)
        game()
    except ValueError:
        invalid()
        game()

def change_spot(x, y, bomb=False):
    global rows
    
    letters = ['a', 'b' , 'c' , 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    
    y = letters.index(y) + 1
    
    try:
        rows[x][y] = '   |'
    except IndexError:
        print("[Row/Column Limit: 5]")
        invalid()
        game()

    if bomb == True:
        rows[x][y] = ' X |'
    
    auto_clear(x, y + 1)
    
def auto_clear(x, y):
    
    # -------------HORIZONTAL CLEAR
    def row_clear(x):

        # LEFT CLEAR
        loop1 = 1
        while True:
            
            try:
                if rows[x][y + loop1] == ' O |' and rows[x - 1][y + loop1] == ' O |' and rows[x + 1][y + loop1] == ' O |':
                    break
                
                if rows[x][y + loop1] == ' - |':
                    rows[x][y + loop1] = '   |'
                
                    loop1 += 1

                else:
                    break
                
            except IndexError:
                break
        
        # RIGHT CLEAR
        loop2 = 1
        while True:
            
            try:
                if rows[x][y - loop2] == ' O |' or rows[x - 1][y - loop2] == ' O |' or rows[x - 1][y - loop2] == ' O |':
                    break
                
                if rows[x][y - loop2] == ' - |':
                    rows[x][y - loop2] = '   |'
                    loop2 += 1
                    
                else:
                    break
            
            except IndexError:
                break
        
        
    row_clear(x)
    
    # -------------VERTICAL CLEAR
    
    # DOWN CLEAR
    loop1 = 1
    while True:
        try:
            if rows[x + loop1][y] == ' O |' or rows[x + loop1][y + 1] == ' O |' or rows[x + loop1][y - 1] == ' O |':
                break
            
            if rows[x + loop1][y] == ' - |':
                rows[x + loop1][y] = '   |'
                row_clear(x + loop1)
                loop1 += 1
                
            else:
                break
            
        except IndexError:
            break
    
    # UP CLEAR
    loop2 = 1
    while True:
        try:
            if rows[x - loop2][y] == ' O |' or rows[x - loop2][y + 1] == ' O |' or rows[x - loop2][y - 1] == ' O |':
                break
            
            if rows[x - loop2][y] == ' - |':
                rows[x - loop2][y] = '   |'
                row_clear(x - loop2)
                loop2 += 1

            else:
                break
            
        except IndexError:
            break

def check_spot(x, y):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    
    y = letters.index(y) + 1
    
    if rows[x][y] == " O |":
        return 'bomb'

def line():
    print('-------------------------------------------------------')

def invalid():
    input('[INVALID INPUT] Press any key to continue >')


intro()
game()
