class Node:

  def __init__(self, x: int, y: int, down: int, right: int):
    self.x = x
    self.y = y
    if(down == -1 and right == -1):
      self.type = "block"
      self.down = -1
      self.right = -1
    elif(down == 0 and right == 0):
      self.type = "empty"
      self.set_value(0)
    else:
      self.type = "clue"
      self.down = down
      self.right = right

  def __str__(self) -> str:
    string = ""
    if(self.type == "block"):
      string = " " + "X"
    elif(self.type == "empty"):
      if(self.get_value() != 0):
        string = " " + str(self.get_value())
    else:
      string = " "
      if(self.down == 0):
        string += " "
      else:
        string += str(self.down)
      
      string += "\\"
      if(self.right == 0):
        string += " "
      else:
        string += str(self.right)

    return string + "\t"
  
  
  def set_value(self, value: int):
    self.down = value
    self.right = value

  def get_value(self):
    return self.down

      


