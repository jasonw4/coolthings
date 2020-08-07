import random

def create_board(width, height):
  columns = []
  for i in range(height):
    row = []
    columns.append(row)
  for i in columns:
    for n in range(width):
      i.append(None)
  gameboard = columns
  return gameboard


def bury_mines(gameboard, n):
  mine_counter = 0
  height = len(gameboard)
  width = len(gameboard[0])
  while mine_counter < n:
    rows = random.randint(0, height-1)
    columns = random.randint(0, width-1)
    if gameboard[rows][columns] != '-1':
      gameboard[rows][columns] = '-1'
      mine_counter += 1
    else:
      continue
        

def get_minecount(gameboard,x,y):
  adj_mines = 0
  height = len(gameboard)
  width = len(gameboard[0])
  for i in range(x-1, x+2):
    if i >= 0 and i <= height-1:
      for n in range(y-1, y+2):
        if n >= 0 and n <= width-1:
          checked_position = gameboard[i][n]
          if checked_position == '-1':
            adj_mines += 1
  return (adj_mines)
  

def print_mines(gameboard):
  for i in gameboard:#for each row
    print_version = str(i)
    print_version = print_version.replace('[', '')
    print_version = print_version.replace(']', '')
    print_version = print_version.replace(',', '')
    print_version = print_version.replace("'", "")
    print(print_version.replace('None', '.'))    


def print_board(gameboard):
  height = len(gameboard)
  width = len(gameboard[0]) 
  hidden_gameboard = gameboard
  for i in range(0,height):
    for n in range(0, width):
      if hidden_gameboard[i][n] == None :
        hidden_gameboard[i][n] = get_minecount (gameboard,i,n)
  print_mines(hidden_gameboard)
    

def user_view(gameboard):
  width = len(gameboard[0])
  user_gameboard = gameboard
  column_list = '  '
  for i in range (0, width):
    column_list = column_list + str(i) + ' '
  
  print(column_list)
  print('-' * 2 * width)
  row_counter = 0
  for i in user_gameboard:
    user_version = str(i)
    user_version = user_version.replace('None', '?')
    user_version = user_version.replace('-1', '?')
    user_version = user_version.replace('[', '')
    user_version = user_version.replace(']', '')
    user_version = user_version.replace(',', '')
    user_version = user_version.replace("'", "")
    user_version = str(row_counter) + '|' + user_version
    row_counter += 1
    print(user_version)


def uncover_board(gameboard,x,y):
  height = len(gameboard)
  width = len(gameboard[0])
  cell = gameboard[x][y]
  if cell != None:
    return
  elif cell == None:
    gameboard[x][y] = get_minecount(gameboard,x,y)
    if gameboard[x][y] > 0:
      return
    else:
      for i in range(x-1, x+2):
        if i >= 0 and i <= height-1:
          for n in range(y-1, y+2):
           if n >= 0 and n <= width-1:
             uncover_board (gameboard, i, n)




def check_won(gameboard):
  for i in gameboard:
    if None in i:
      return False
  
  return True


def game (height , width , n):
  gameboard = create_board(width, height)
  bury_mines(gameboard, n)
  #for debugging purposes:
  #print_mines(gameboard)
  user_view(gameboard)

  while check_won(gameboard) != True:      
    user_input = input("Please enter row, column: ")
    x = int(user_input[0])
    y = int(user_input[2])
    if gameboard [x][y] == '-1' :
      print ("YOU LOSE")
      break
    uncover_board(gameboard,x,y)
    user_view (gameboard)
    check_won(gameboard)

  if check_won(gameboard) == True:
    print ("You Win")

game(8,8,4)
