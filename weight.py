def add_weight(date, weight):
  with open('weightpy.txt', 'a') as file:
    file.write(f'{date}, {weight}\n')
  print('\nadded!\n')

def stats():
  with open('weightpy.txt', 'r') as file:
    lines = file.readlines()

  for line in lines:
    parts = line.strip().split(",")


def main():
  while (1):
    print("1. Add a weight\n2. Modify the list\n3. View The List\n4. Data\n5. Exit")
    choice = int(input(""))
    if (choice == 1):
      date = input("date:XX-XX-XX: ")
      weight = input("weight:lbs: ")
      add_weight(date, weight)
      continue
    if (choice == 2):
      date = input("modifing date: ")
      modify_type = int(input("1. Remove\n2.Change Date\n3.Change weight\n"))
      # you can make one function with modify_type as parameter
      continue
    if (choice == 3):
      print("hi")
      #print the list
      continue
    if (choice == 4): 
      stats()
      continue
    if (choice == 5):
      break
    else:
      print('invalid choice')
if __name__ == "__main__":
    main()
 