## tracker

This program is to help me track my weight (simple!). 

#### Version I -- File IO + Manual Entry

Version I is a barebones version with nearly no automation. Each day add_weight() must be called, and the "mm--dd-yy", "weight" variables must be manually inputted to be written to the file. The stats function calculates "average of the average weight gain per week", a flawed statistic (becuase of outlier weeks). Option to print the list to terminal or display a **MatPlotLib** chart.

#### Version II - File IO + **Flask**
Version II served as my introduction to **Flask**. I learned the basic **POST** and **GET** methods and used them via the shortcuts application on my iPhone. Now I could log my weight while I was in the gym, without my laptop. The catch is that without a hosting platform, my laptop needed to be running api.py for the change to go through.

#### Version 2.1 - CLI - API (Flask) - Replit
It was apparent I needed a hosting platform. I used **Replit** to import by github repository and host it for free. 
