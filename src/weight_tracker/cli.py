import matplotlib.pyplot as plt
from datetime import datetime


# this function uses matplotlib to show a graph of weight

def show_graph():
    dates = []
    weights = []

    with open('weight.txt', 'r') as file:
        for line in file:
            if "," not in line:
                continue
            date_str, weight_str = [x.strip() for x in line.split(",")]
            dates.append(date_str)
            weights.append(float(weight_str))

    if not dates:
        print("No data to graph")
        return

    plt.plot(dates, weights)
    plt.xlabel("Date")
    plt.ylabel("Weight (lbs)")
    plt.title("Weight Over Time")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# this function adds a new weight at the next line with the given date and weight
def add_weight(date, weight):
  with open('weight.txt', 'a') as file:
    file.write(f'{date}, {weight}\n')
  print('\nadded!\n')

# this function prints the file into terminal
def print_record():
  with open('weight.txt', 'r') as file:
    lines = file.readlines()

  for line in lines:
    print(line)

# this function calculates specific values to track progress
def stats():
    print('broken')



def main():
  while (1):
    print("=========================\n Ryan Weight Calculator\n=========================")
    print("1. Add a weight\n2. View the list\n3. Data\n4. Exit")
    try:
      choice = int(input("Enter Choice: "))
    except ValueError:
      print("\n  --Please enter a valid number--  \n")
      continue
    if (choice == 1):
      date = input("date: YYYY-MM-DD: ")
      weight = input("weight:lbs: ")
      add_weight(date, weight)
      continue
    if (choice == 2):
      try:
        view_type = int(input('1. Printed List\n2. Chart\n'))
      except ValueError:
         print('Please enter a valid number')
         continue
      if view_type == 1:
         print_record()
      if view_type == 2:
         show_graph()
      continue
    if (choice == 3): 
      stats()
      continue
    if (choice == 4):
      break
    else:
      print('invalid choice')



      
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGoodbye!")
