from typing import Generator
import matplotlib.pyplot as plt

DATA_SEPERATOR = ","
KEY_VALUE_SEPERATOR = ":"

def get_all_indexes(line, character):
  all_indexes = []
  for character_index in range(0, len(line)):
    if line[character_index] == character:
      all_indexes.append(character_index)
  return all_indexes

def get_keys(line):
  keys = []
  KV_seperators = get_all_indexes(line, KEY_VALUE_SEPERATOR)    
  data_seperators = get_all_indexes(line, DATA_SEPERATOR)

  if len(KV_seperators) == 0:
    for x in range(0, len(data_seperators)):
      keys.append(f"Line{x}")
  else:
    for x in range(0, len(data_seperators)):
      keys.append(line[data_seperators[x] + 1 : KV_seperators[x]])
    
  return keys

# Creates the formatted output
def setup():
  first_line = "," + file.readlines()[0].strip("\n")
  keys = get_keys(first_line)

  output_list = []
  for x in range(0, len(keys)):
    data_set = {keys[x] : []}
    output_list.append(data_set)
  return output_list

def run(data_input, output):
  lines = data_input.readlines()
  for line in lines:
    for data_set_index in range(0, len(output)):
      if len(get_all_indexes(line, KEY_VALUE_SEPERATOR)) == 0:
        pass
      else:
        key = output(data_set_index).keys()[data_set_index]
        data_starting_index = line.find(key) + len(key)
        line = line + ","
        data_seperator_indexes = get_all_indexes(DATA_SEPERATOR)
        data = line[data_starting_index + 1 : data_seperator_indexes[]]
      


      




if __name__ == "__main__":
  # with open('input.txt', 'r') as file:
  #   output_list = setup()

  #   run(file, output_list)









  # # plt.plot(x, y)
  # # plt.show()
  # my_array = [[1,2,3,4], [1,2,3,4]]
  # print(len(my_array))



  # string = "this"
  # print(string.find("h"))
  # print(string[:string.find("h")])

  string = "thisthattheother"
  index = string.find("this") + len("this")
  print(index)