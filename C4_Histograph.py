import matplotlib.pyplot as plt

'''
============================================================
                    plt.hist()
============================================================

Explanation (≤30 words):
  - Used to display the frequency distribution of
    numerical data by grouping values into bins.

------------------------------------------------------------

Syntax:
  plt.hist(data, bins=10, range=None, density=False,
           color=None, edgecolor=None, alpha=1.0,
           cumulative=False)

------------------------------------------------------------

Parameters:
  data        → Input numerical data
                 (list, array, pandas Series)

  bins        → Number or sequence of bins
                 (values: 5, 10, 20, or list)

  range       → Lower and upper range of bins
                 (values: (min, max))

  density     → Normalize histogram to probability
                 (values: True, False)

  color       → Color of bars
                 (values: 'blue', 'green', 'orange')

  edgecolor   → Border color of bars
                 (values: 'black', 'gray')

  alpha       → Transparency level
                 (values: 0.0 to 1.0)

  cumulative  → Cumulative frequency
                 (values: True, False)

------------------------------------------------------------

When to Use plt.hist():
  - To understand data distribution
  - To detect skewness or spread
  - To analyze frequency of values
  - Common in statistics, ML, and EDA
'''

# Syntax:
#     plt.hist(data, bins=10, range=None, density=False, color=None, edgecolor=None, alpha=1.0, cumulative=False)

# ------------------------------------------------------------
# Examples: Different Ways to Use plt.hist()
# ------------------------------------------------------------


data = [12, 15, 18, 20, 22, 25, 30, 35, 40, 42, 45]

# ------------------------------------------------
# 1) Basic histogram
# ------------------------------------------------
plt.hist(data)
plt.title("Basic Histogram")
plt.show()


# ------------------------------------------------
# 2) Histogram with custom bins
# ------------------------------------------------
plt.hist(data, bins=5)
plt.title("Histogram with 5 Bins")
plt.show()


# ------------------------------------------------
# 3) Histogram with color and edge color
# ------------------------------------------------
plt.hist(data, bins=6, color='skyblue', edgecolor='black')
plt.title("Styled Histogram")
plt.show()


# ------------------------------------------------
# 4) Normalized histogram (probability density)
# ------------------------------------------------
plt.hist(data, bins=6, density=True, color='green')
plt.title("Normalized Histogram")
plt.show()


# ------------------------------------------------
# 5) Cumulative histogram
# ------------------------------------------------
plt.hist(data, bins=6, cumulative=True, color='orange')
plt.title("Cumulative Histogram")
plt.show()


# ------------------------------------------------
# 6) Histogram with transparency
# ------------------------------------------------
plt.hist(data, bins=6, alpha=0.6, color='purple')
plt.title("Histogram with Transparency")
plt.show()

# ------------------------------------------------
# 7) Use Explicit Bin Ranges (Best Practice)
# ------------------------------------------------

plt.hist(data, bins=range(0, 50, 5), color='pink', edgecolor='black', label='Distribution of Data')
plt.title('Histrogram with custom Bins range()')
plt.grid(alpha=0.3)
plt.legend(loc='best')
plt.show()
'''
------------------------------------------------------------

Important Notes (Professional):
  - Histogram works ONLY with numerical data
  - bins control smoothness vs detail
  - density=True is common in probability analysis
  - Do NOT confuse histogram with bar chart

============================================================
'''

'''
============================================================
        plt.hist(..., density=True) — DETAILED EXPLANATION
============================================================

WHAT density=True DOES
----------------------
- Converts the histogram from FREQUENCY (counts)
  to PROBABILITY DENSITY.
- The Y-axis no longer shows how many values fall
  in a bin.
- Instead, it shows how "dense" the data is in that range.

CORE RULE
---------
- Total AREA of all histogram bars = 1
- (Not the sum of bar heights)

MATHEMATICAL FORMULA
--------------------
For each bin:

density = (number of values in the bin) /
          (total number of values x bin width)

This is why bar heights are usually small decimals.

WHY BIN WIDTH MATTERS
---------------------
- Wider bins → smaller density values
- Narrower bins → larger density values
- Same data can look taller or shorter depending on bin width

->>BIN STRUCTURE EXAMPLE
--------------------------
bins = range(0, 101, 20)

This creates bins:
[0-20), [20-40), [40-60), [60-80), [80-100)

Each bin width = 20

EXAMPLE CALCULATION
-------------------
Assume:
- Total data points = 20
- Values between 20-40 = 6

density = 6 / (20 x 20)
        = 0.015

So the bar height ≈ 0.015, not 6.

HOW TO READ THE HISTOGRAM
------------------------
- Bar HEIGHT → probability density
- Bar WIDTH  → bin range
- Bar AREA   → probability that a value lies in that range

Example:
If the area of a bar = 0.30
→ 30% of the data lies in that bin

IMPORTANT DISTINCTION
---------------------
density=True:
- Height ≠ number of values
- Area   = probability

density=False (default):
- Height = number of values
- Area   = meaningless

WHEN TO USE density=True
------------------------
- Comparing distributions with different dataset sizes
- Studying distribution shape
- Overlaying probability density functions (PDFs)
- Statistical analysis

WHEN NOT TO USE
---------------
- When you want exact frequencies
- When dataset is very small and interpretation becomes unclear

COMMON CONFUSION
----------------
- Seeing small values like 0.01 does NOT mean 1%
- It means probability per unit on X-axis

ONE-LINE SUMMARY
----------------
density=True normalizes histogram so that
the total probability equals 1.
============================================================
'''
