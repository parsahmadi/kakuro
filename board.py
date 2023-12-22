from node import *

class Board:

  def __init__(self, size: int, board_information: list):
    self.size = size
    self.board = []
    for i in range(size):
      temp_list = []
      for j in range(size):
        if(type(board_information[i][j]) == int):
          temp_list.append(Node(j, i, board_information[i][j], board_information[i][j]))
        else:
          temp_list.append(Node(j, i, board_information[i][j][0], board_information[i][j][1]))
      
      self.board.append(temp_list)

    
  def print(self):
    for i in range(self.size):
      print('|', end="")
      for j in range(self.size):
        print(self.board[i][j], end="|")
      
      print("")
    
    print()


  def backtrack_solve(self):
    empty_nodes = []
    for i in range(self.size):
      for j in range(self.size):
        if(self.board[i][j].type == "empty"):
          empty_nodes.append(self.board[i][j])

    i = 0
    while i < len(empty_nodes):
      legal_numbers = self.legal_numbers(empty_nodes[i])
      if not legal_numbers:
        i -= 1
        continue
      else:
        if(empty_nodes[i].get_value() == 0):
          empty_nodes[i].set_value(legal_numbers[0])
          i += 1
          continue
        else:
          find_something = False
          for number in legal_numbers:
            if number > empty_nodes[i].get_value():
              empty_nodes[i].set_value(number)
              i += 1
              find_something = True
              break
          
          if(find_something):
            continue

          empty_nodes[i].set_value(0)
          i -= 1
          


  def ordering_backtrack_solve(self):
    # finding empty nodes
    empty_nodes = []
    for i in range(self.size):
      for j in range(self.size):
        if(self.board[i][j].type == "empty"):
          empty_nodes.append(self.board[i][j])

    # sorting empty nodes by number of legal numbers
    number_of_legal_numbers = []
    for node in empty_nodes:
      number_of_legal_numbers.append(len(self.legal_numbers(node)))
    
    for i in range(len(empty_nodes)):
      for j in range(i, 0, -1):
        if number_of_legal_numbers[j] < number_of_legal_numbers[j - 1]:
          empty_nodes[j], empty_nodes[j - 1] = empty_nodes[j - 1], empty_nodes[j]
          number_of_legal_numbers[j], number_of_legal_numbers[j - 1] = number_of_legal_numbers[j - 1], number_of_legal_numbers[j]


    #backtracking
    i = 0
    while i < len(empty_nodes):
      legal_numbers = self.legal_numbers(empty_nodes[i])
      if not legal_numbers:
        i -= 1
        continue
      else:
        if(empty_nodes[i].get_value() == 0):
          empty_nodes[i].set_value(legal_numbers[0])
          i += 1
          continue
        else:
          find_something = False
          for number in legal_numbers:
            if number > empty_nodes[i].get_value():
              empty_nodes[i].set_value(number)
              i += 1
              find_something = True
              break
          
          if(find_something):
            continue

          empty_nodes[i].set_value(0)
          i -= 1      

    


  def legal_numbers(self, node: Node):
    legal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    #vertical

    i = node.y
    zero_numbers = 0
    vertical_sum = 0
    while i >= 1:
      i -= 1
      if(self.board[i][node.x].type == "clue"):
        down_clue = self.board[i][node.x].down
        break
      else:
        vertical_sum += self.board[i][node.x].get_value()
        if self.board[i][node.x].get_value() == 0:
          zero_numbers += 1
        elif self.board[i][node.x].get_value() in legal_numbers:
          legal_numbers.remove(self.board[i][node.x].get_value())

    i = node.y
    while i < self.size - 1:
      i += 1
      if(self.board[i][node.x].type == "clue" or self.board[i][node.x].type == "block"):
        break
      else:
        vertical_sum += self.board[i][node.x].get_value()
        if self.board[i][node.x].get_value() == 0:
          zero_numbers += 1
        elif self.board[i][node.x].get_value() in legal_numbers:
          legal_numbers.remove(self.board[i][node.x].get_value())

    if zero_numbers == 0:
      if down_clue - vertical_sum in legal_numbers:
        legal_numbers = [down_clue - vertical_sum]
      else:
        return []
    else:
      maximum_possible_number = down_clue - vertical_sum - (zero_numbers * (zero_numbers + 1) / 2)
      legal_numbers = [number for number in legal_numbers if number <= maximum_possible_number]



    #horizontal
    
    j = node.x
    zero_numbers = 0
    horizontal_sum = 0
    while j >= 1:
      j -= 1
      if(self.board[node.y][j].type == "clue"):
        right_clue = self.board[node.y][j].right
        break
      else:
        horizontal_sum += self.board[node.y][j].get_value()
        if self.board[node.y][j].get_value() == 0:
          zero_numbers += 1
        elif self.board[node.y][j].get_value() in legal_numbers:
          legal_numbers.remove(self.board[node.y][j].get_value())

    j = node.x
    while j < self.size - 1:
      j += 1
      if(self.board[node.y][j].type == "clue" or self.board[node.y][j].type == "block"):
        break
      else:
        horizontal_sum += self.board[node.y][j].get_value()
        if self.board[node.y][j].get_value() == 0:
          zero_numbers += 1
        elif self.board[node.y][j].get_value() in legal_numbers:
          legal_numbers.remove(self.board[node.y][j].get_value())

    if zero_numbers == 0:
      if right_clue - horizontal_sum in legal_numbers:
        legal_numbers = [right_clue - horizontal_sum]
      else:
        return []
    else:
      maximum_possible_number = right_clue - horizontal_sum - (zero_numbers * (zero_numbers + 1) / 2)
      legal_numbers = [number for number in legal_numbers if number <= maximum_possible_number]

    return legal_numbers