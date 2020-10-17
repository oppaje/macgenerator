from random import choice
import traceback


string = '0123456789ABCDEF'

def duplicate(path):
  f = open(path, 'r', errors='ignnore').readlines()
  old = len(f)
  new_f = set(f)
  new = len(new_f)
  o = open(path, 'w')
  for line in new_f:
    o.write(line)
  print(f"{old - new} duplicate(s) have been removed!")
  print("\nFinished! Results have been saved in MacAddresses.txt")


def mode1():
  mac = ''.join(choice(string) for _ in range(6))
  return f"00:1A:79:{mac[0:2]}:{mac[2:4]}:{mac[4:6]}\n"


def mode2(custom):
  list1 = []
  for letter in custom:
    if letter == '*':
      letter = letter.replace('*', ''.join(choice(string)))
    list1.append(letter)
  return ''.join(list1) + "\n"


def generator(mode, custom):
  file = 'MacAddresses.txt'

  with open(file, 'w') as o:
    for x in range(number):
      if mode == '1':
        o.write(mode1())
      elif mode == '2':
        o.write(mode2(custom))
      print(f"Generated: {x + 1} MAC addresses", end='\r')
  print("\nRemoving duplicates...", end='\r')
  duplicate(file)


if __name__ == '__main__':
  try:
    print("""
                             __  __    _    ____    ____                           _             
                            |  \/  |  / \  / ___|  / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
                            | |\/| | / _ \| |     | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
                            | |  | |/ ___ \ |___  | |_| |  __/ | | |  __/ | | (_| | || (_) | |   
                            |_|  |_/_/   \_\____|  \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|  
                            
                                            Coded by: oppaje For NeThinGoez.com
                                      """)
    mode = input("""Select Mode:
    1. Default: 00:1A:79:**:**:**
    2. Custom (Example: 00:1A:79:*8:1B:**)
    > """)
    if mode == '2':
      custom = input("Enter custom mode: ")
    else:
      custom = None
    number = int(input("Enter the amount of Macs to generate: "))
    generator(mode, custom)
  except:
    print(traceback.format_exc())
    print('Something went wrong, please try again. If the same error keeps happening contact oppaje.')
  input("Press enter to close: ")
