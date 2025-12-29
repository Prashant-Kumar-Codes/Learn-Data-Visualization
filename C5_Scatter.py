import matplotlib.pyplot as plt
import random
'''
============================================================
                      plt.scatter()
============================================================

plt.scatter()
   Explanation (≤30 words):
     - Used to plot individual data points to analyze
       relationships, distribution patterns, and clustering
       between two numerical variables.

   Syntax:
     plt.scatter(x, y,
                 c=None,
                 s=None,
                 marker='o',
                 alpha=None,
                 label=None,
                 edgecolors=None,
                 cmap=None)

   Parameters:
     x, y        → X and Y axis data points
                    (list, array, Series)

     c / color   → Color of points
                    (values: 'red', 'blue', 'green',
                             list of colors, numeric array)

     s           → Size of points (area in points²)
                    (values: 10, 30, 100, ...)

     marker      → Shape of points
                    (values: 'o', '^', 's', '*', 'x', 'D')

     alpha       → Transparency of points
                    (values: 0.0 to 1.0)

     label       → Legend label
                    (string)

     edgecolors  → Border color of points
                    (values: 'black', 'none')

     cmap        → Colormap for numeric color values
                    (values: 'viridis', 'plasma', 'coolwarm')

IMPORTANT NOTES
---------------
- If `c` is numeric, `cmap` must be used.
- `s` represents AREA, not radius.
- `alpha` helps visualize overlapping points.
- Best for correlation and outlier detection.

COMMON USE CASES
----------------
- Relationship between two variables
- Cluster visualization
- Outlier detection
- Data distribution comparison

------------------------------------------------------------
'''

dic = {
  'x' : [10, 20, 12, 31, 3 ,43 ,2, 2, 4, 6,3 ,2, 11, 35, 2,5, 6,2,28, 0, 32, 5],
  'y' : [20, 2, 4, 22, 4, 5, 3,2,9 ,22, 46, 7,4,2,21, 43, 23, 22, 7, 36, 32, 4]
}

x = []
y = []

for i in range(0,20):
      x.append(random.randint(0, 50))
      y.append(random.randint(20, 70))

#scatter plot 1
plt.scatter(dic['x'], dic['y'], s=8, marker='o', color='red')
plt.grid(alpha= 0.5)
plt.xlabel('x-axis')
plt.ylabel('y-axix')
plt.show()

#scatter plot 2
plt.scatter(x= x, y= y, s = 6 )
plt.show()



# ============================================================
#         plt.scatter() — USAGE IN DIFFERENT WAYS
# ============================================================

# ------------------------------------------------------------
# 1) BASIC SCATTER PLOT
# ------------------------------------------------------------
# Used to show relationship between two variables.

plt.scatter(x, y)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()


# ------------------------------------------------------------
# 2) SCATTER WITH COLOR
# ------------------------------------------------------------
# Used to visually distinguish data points.

plt.scatter(x, y, color='blue')
plt.show()


# ------------------------------------------------------------
# 3) SCATTER WITH POINT SIZE (s)
# ------------------------------------------------------------
# Used to emphasize importance or magnitude.

plt.scatter(x, y, s=50)
plt.show()


# ------------------------------------------------------------
# 4) SCATTER WITH DIFFERENT MARKERS
# ------------------------------------------------------------
# Used to differentiate categories.

plt.scatter(x, y, marker='^')
plt.show()


# ------------------------------------------------------------
# 5) SCATTER WITH TRANSPARENCY (alpha)
# ------------------------------------------------------------
# Used when points overlap heavily.

plt.scatter(x, y, alpha=0.6)
plt.show()


# ------------------------------------------------------------
# 6) SCATTER WITH EDGE COLORS
# ------------------------------------------------------------
# Used to make points clearer.

plt.scatter(x, y, color='pink', edgecolors='black')
plt.show()


# ------------------------------------------------------------
# 7) SCATTER WITH LEGEND
# ------------------------------------------------------------
# Used when plotting multiple datasets.

plt.scatter(dic['x'], dic['y'], label='Group A')
plt.scatter(x, y, label='Group B')
plt.legend()
plt.show()


# ------------------------------------------------------------
# 8) SCATTER WITH COLORMAP (Numeric Coloring)
# ------------------------------------------------------------
# Used to represent third variable via color.

plt.scatter(x, y, c='z', cmap='viridis')
plt.colorbar(label='Z values')
plt.show()


# ------------------------------------------------------------
# 9) SCATTER FOR OUTLIER DETECTION
# ------------------------------------------------------------
# Used to identify abnormal data points.

plt.scatter(x, y)
#plt.axhline(y=threshold)
plt.show()


# ------------------------------------------------------------
# 10) SCATTER VS LINE (NO CONNECTION)
# ------------------------------------------------------------
# Scatter does NOT connect points like plot().

plt.scatter(x, y)
plt.show()
