import random
from tkinter import Tk, Canvas





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
        

def get_minecount(gameboard,y,x):
  adj_mines = 0
  height = len(gameboard)
  width = len(gameboard[0])
  for i in range(y-1, y+2):
    if i >= 0 and i <= height-1:
      for n in range(x-1, x+2):
        if n >= 0 and n <= width-1:
          checked_position = gameboard[i][n]
          if checked_position == '-1':
            adj_mines += 1
  return (adj_mines)


def uncover_board(gameboard,y,x):
  height = len(gameboard)
  width = len(gameboard[0])
  cell = gameboard[y][x]
  if cell != None:
    return
  elif cell == None:
    gameboard[y][x] = get_minecount(gameboard,y,x)
    if gameboard[y][x] > 0:
      return
    else:
      for i in range(y-1, y+2):
        if i >= 0 and i < height:
          for n in range(x-1, x+2):
           if n >= 0 and n < width:
             uncover_board(gameboard,i, n)


def check_won(gameboard):
  for i in gameboard:
    if None in i:
      return False
  
  return True

   





def run():
  width = 8
  height = 8
  board = create_board(height, width)
  bury_mines(board, 7)    
  root = Tk()
  root.wm_title ("Minesweeper")
  heightpxls = 50 * height
  widthpxls = 50 * width
  canvas = Canvas(master=root, height=heightpxls,width = widthpxls)
  canvas.pack()
  def handle_click(event):
    
    x = event.x // 50
    y = event.y // 50
    uncover_board(board, y, x)
    print(y,x)
    if board[y][x] == '-1':
      canvas.unbind("<Button-1>")
      
      canvas.create_rectangle ((x*50), (y*50), ((x*50)+50), ((y*50)+50), fill="red", outline="white")
      canvas.create_text ((heightpxls//2),(widthpxls//2),font="arial 36", text = "YOU LOSE")
    elif check_won(board) == True:
      display_board(board, canvas)
      canvas.unbind("<Button-1>")
      canvas.create_text ((heightpxls//2),(widthpxls//2),font="arial 36", text = "YOU WIN")
    else:
      display_board(board, canvas)
  canvas.bind("<Button-1>", handle_click)
  
  display_board(board, canvas)

  root.mainloop()


#widthpxls = canvas.winfo_width()
#heightpxls = canvas.winfo_height()


def display_board(board, canvas):
  row_length = len(board[0])
  for i in range(0,len(board)):
    for n in range (0, row_length):
      x1 = (n * 50 ) #+ 10
      y1 = (i * 50) #+ 10
      if board[i][n] in range (0, 9):
        canvas.create_rectangle(x1, y1, (x1 +50), (y1 + 50), fill= "light grey", outline = "white")
        canvas.create_text((x1 + 25),(y1 + 25),font="arial 20", text=str(get_minecount (board, i, n)))
      elif board[i][n] == None:
        canvas.create_rectangle(x1, y1, (x1 +50), (y1 + 50), fill= "grey", outline = "white")
      else:
       canvas.create_rectangle(x1, y1, (x1 +50), (y1 + 50), fill= "grey", outline = "white") 
      
  
run()

