import matplotlib.pyplot as plt

def show_graph():
    dates = []
    weights = []

    with open('weightpy.txt', 'r') as file:
        for line in file:
            date, weight = line.strip().split(',')
            dates.append(date)
            weights.append(float(weight))

    plt.plot(dates, weights)
    plt.xlabel("Date")
    plt.ylabel("Weight (lbs)")
    plt.title("Weight Over Time")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def add_weight(date, weight):
  with open('weightpy.txt', 'a') as file:
    file.write(f'{date}, {weight}\n')
  print('\nadded!\n')

def stats():
  with open('weightpy.txt', 'r') as file:
    lines = file.readlines()

  for line in lines:
    print(line)

def modify_entry(date, modify_type):
    with open('weightpy.txt', 'r') as file:
        lines = file.readlines()

    new_lines = []
    found = False

    for line in lines:
        d, w = line.strip().split(",")
        if d == date:
            found = True
            if modify_type == 1:
                continue  # remove
            elif modify_type == 2:
                new_date = input("new date: ")
                new_lines.append(f"{new_date}, {w}\n")
                continue
            elif modify_type == 3:
                new_weight = input("new weight: ")
                new_lines.append(f"{d}, {new_weight}\n")
                continue
        new_lines.append(line)

    if not found:
        print("\ndate not found\n")
        return

    with open('weightpy.txt', 'w') as file:
        file.writelines(new_lines)

    print("\nmodified!\n")

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
      modify_type = int(input("1. Remove\n2.Change Date\n3.Change weight\n4.Cancel\n"))
      if modify_type in (1, 2, 3):
        modify_entry(date, modify_type)
      continue
    if (choice == 3):
      show_graph()
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
 