

class Board:
  current_player = ""

  player1 =  "x"

  player2 = "o"

  board = [["_", "_", "_"],["_", "_", "_"], ["_", "_", "_"]]

  visual = ""

  def printVisual(self):
    self.visual = ""
    for row in self.board:
      for i in range(len(row)):
        if i == 2:
          self.visual += row[i]+"\n"
        else:
          self.visual += row[i]
    print(self.visual)
  
  def turn(self):
    while self.current_player != "":
      print(self.current_player + "... it is your turn")
      inputs = input()
      print(inputs)
      self.board[int(inputs[0])][int(inputs[1])] = self.current_player
      self.printVisual()
      self.horizontal()
      self.vertical()
      self.dia()
      self.switch()


  def start(self):
    self.current_player = self.player1

  def switch(self):
    if self.current_player == self.player1:
      self.current_player = self.player2
    else:
      self.current_player = self.player1

  def horizontal(self):
    for row in self.board:
       if row[0] == row[1] and row[0] == row[2]:
        print(self.current_player + " is the winner")
        self.current_player = ""
        break

  def vertical(self):
    for i in range(len(self.board)):
      if self.board[0][i] == self.board[1][i] and self.board[0][i] == self.board[2][i]:
        print(self.current_player + " is the winner")
        self.current_player = ""
        break
  
  def dia(self):
    if (self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2]):
      print(self.current_player + " is the winner")
      self.current_player = ""
    if (self.board[0][2] == self.board[1][1] and self.board[0][2] == self.board[2][0]):
      print(self.current_player + " is the winner")
      self.current_player = ""


game = Board()
game.start()
print(game.current_player)

# for i in range(len(game.visual)):

game.turn()




  



