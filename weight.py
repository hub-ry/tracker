import matplotlib.pyplot as plt
from datetime import datetime
import requests
url = "http://127.0.0.1:8000/get_weights"
response = requests.get(url)
weights = response.json()["weights"]

for w in weights:
    print(w["date"], w["weight"])

# this function uses matplotlib to show a graph of weight
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

# this function adds a new weight at the next line with the given date and weight
def add_weight(date, weight):
  with open('weightpy.txt', 'a') as file:
    file.write(f'{date}, {weight}\n')
  print('\nadded!\n')

# this function prints the file into terminal
def print_record():
  with open('weightpy.txt', 'r') as file:
    lines = file.readlines()

  for line in lines:
    print(line)

# this function modifies an entry
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
                continue 
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

# this function calculates specific values to track progress
def stats():
    records = []
    with open('weightpy.txt', 'r') as file:
        lines = file.readlines()

    for line in lines:
        date_str, weight_str = line.strip().split(',')
        date = datetime.strptime(date_str.strip(), "%m-%d-%y")
        weight = float(weight_str.strip())
        records.append((date, weight))
    
    if len(records) < 2:
        print('not enough records')
        return

    weekly_rates = []

    for i in range(len(records) - 1):
        d1, w1 = records[i]
        d2, w2 = records[i + 1]
        delta_weight = w2 - w1
        delta_days = (d2 - d1).days
        if delta_days == 0:
            continue
        weeks = delta_days / 7
        weekly_rate = delta_weight / weeks
        weekly_rates.append(weekly_rate)

    if not weekly_rates:
        print('no valid intervals')
        return

    avg_of_avgs = sum(weekly_rates) / len(weekly_rates)
    print(f"Average of weekly averages: {avg_of_avgs:.2f} lbs/week")



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
      view_type = int(input('1. Printed List\n2. Chart\n'))
      if view_type == 1:
         print_record()
      if view_type == 2:
        show_graph()
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
 