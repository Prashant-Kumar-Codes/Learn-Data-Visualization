import matplotlib.pyplot as plt
import random

'''
============================================================
        plt.subplot() — DETAILED & EXAM-ORIENTED NOTES
============================================================

plt.subplot()
   Explanation (≤30 words):
     - Used to create multiple plots (subplots)
       in a single figure arranged in rows and columns.

------------------------------------------------------------

SYNTAX:
  plt.subplot(nrows, ncols, index)
  OR (shorthand)
  plt.subplot(nrows * 100 + ncols * 10 + index)

------------------------------------------------------------

PARAMETERS:
  nrows → Number of rows in the figure grid
          (values: 1, 2, 3, ...)

  ncols → Number of columns in the figure grid
          (values: 1, 2, 3, ...)

  index → Position of current subplot
          (values: 1 to nrows*ncols)

------------------------------------------------------------

HOW subplot WORKS
  - Divides the figure into a grid (rows x columns)
  - Activates the subplot at given index
  - All plotting commands apply to that subplot only

------------------------------------------------------------

EXAMPLES — DIFFERENT USAGES
------------------------------------------------------------

1) TWO PLOTS IN ONE ROW

  plt.subplot(1, 2, 1)
  plt.plot(x, y)
  plt.title("Line Plot")

  plt.subplot(1, 2, 2)
  plt.scatter(x, y)
  plt.title("Scatter Plot")

  plt.show()

------------------------------------------------------------

2) TWO PLOTS IN ONE COLUMN

  plt.subplot(2, 1, 1)
  plt.plot(x, y)

  plt.subplot(2, 1, 2)
  plt.hist(y)

  plt.show()

------------------------------------------------------------

3) 2x2 GRID OF SUBPLOTS

  plt.subplot(2, 2, 1)
  plt.plot(x, y)

  plt.subplot(2, 2, 2)
  plt.scatter(x, y)

  plt.subplot(2, 2, 3)
  plt.bar(categories, values)

  plt.subplot(2, 2, 4)
  plt.hist(values)

  plt.show()

------------------------------------------------------------

4) SHORTHAND SYNTAX

  plt.subplot(221)
  plt.plot(x, y)

  plt.subplot(222)
  plt.scatter(x, y)

  plt.subplot(223)
  plt.bar(categories, values)

  plt.subplot(224)
  plt.hist(values)

  plt.show()

------------------------------------------------------------

IMPORTANT NOTES (EXAM):
  - Indexing starts from 1, not 0
  - subplot() is state-based (pyplot)
  - Layout is fixed once created
  - For complex layouts, use subplots()

------------------------------------------------------------

subplot() vs subplots():
  subplot()  → One subplot at a time
  subplots() → Returns Figure & Axes objects (OO-style)

------------------------------------------------------------

WHEN TO USE subplot():
  ✔ Quick comparisons
  ✔ Simple dashboards
  ✔ Small scripts & notebooks

WHEN TO AVOID subplot():
  ✖ Large applications
  ✖ Complex layouts
  ✖ Fine-grained control needed

============================================================
'''

def gen_ran_num_list(length, lower_limit ,upper_limit):
      lis = []
      for i in range(length):
            lis.append(random.randint(lower_limit, upper_limit))
      return lis

x = gen_ran_num_list(10, 1, 10)
y = [i*10 for i in x]

a = gen_ran_num_list(40, 1, 50)
b = gen_ran_num_list(40, 20, 70)

#creating a single row with two column plots
plt.subplot(1, 2, 1)
plt.plot(x,y, color='green')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Line Graph')
plt.grid(alpha=0.5)

plt.subplot(1, 2, 2)
plt.hist(a, bins=5, color='pink', edgecolor='red')
plt.xlabel('x-axis')
# Set custom x-axis ticks
plt.xticks([i for i in range(0, 51, 10)])  # 0,10,20,30,40,50
plt.ylabel('y-axis')
plt.title('Histogram')
plt.grid(alpha=0.5)
plt.tight_layout()
plt.show()