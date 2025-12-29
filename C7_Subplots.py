
import matplotlib.pyplot as plt

'''
============================================================
        plt.subplots() — WORKING WITH MULTIPLE AXES
============================================================

fig, ax = plt.subplots(nrows, ncolumns, figsize=(heght, width))

THEORY (How this works)
----------------------
- plt.subplots() creates:
    1) A Figure object (fig)
    2) Multiple Axes objects (ax)

- Axes are returned as:
    • A single Axes object → if only one subplot
    • An array of Axes     → if multiple subplots

- Each ax[i] represents one plotting area.
- Methods like plot(), bar(), set_title() act
  ONLY on that specific Axes.


IMPORTANT POINTS:

- plt.subplots() follows Object-Oriented API
- fig controls the entire figure
- ax controls individual plotting areas
- ax[index] selects a specific subplot
- fig.suptitle() sets global title
- Preferred over plt.subplot() for real projects
============================================================
'''

'''
============================================================
        METHODS USED WITH plt.subplots() (fig & ax)
============================================================

When using:
    fig, ax = plt.subplots()

- fig → Figure-level methods (whole canvas)
- ax  → Axes-level methods (individual plot)


----------------FIGURE OBJECT METHODS (fig)-----------------

1. fig.suptitle(): Sets a common title for the entire figure.

    Syntax:
    fig.suptitle(text, fontsize=None, color=None)

    Parameters:
    text     → Title text (string)
    fontsize → Size of title
                (values: 10, 12, 16, 20)
    color    → Title color
                (values: 'black', 'blue', etc.)

------------------------------------------------------------

2. fig.set_size_inches(): Sets figure width and height.

    Syntax:
    fig.set_size_inches(width, height)

    Parameters:
    width  → Width in inches (e.g., 8, 10)
    height → Height in inches (e.g., 4, 6)

------------------------------------------------------------

3. fig.tight_layout(): Automatically adjusts spacing between subplots.

    Syntax:
    fig.tight_layout()

    Parameters:
    None

------------------------------------------------------------

4. fig.savefig(): aves the figure to a file.

    Syntax:
    fig.savefig(filename, dpi=None)

    Parameters:
    filename → File name (string)
    dpi      → Resolution
                (values: 100, 300)



------------------AXES OBJECT METHODS (ax)-------------------

1. ax.plot()
2. ax.scatter()
3. ax.bar()
4. ax.hist()

5. ax.set_title(): Sets title for a specific subplot.
    Syntax:
    ax.set_title(title, fontsize=None)

    Parameters:
    title    → Subplot title (string)
    fontsize → Size
                (values: 10, 12, 16)

------------------------------------------------------------

6. ax.set_xlabel(): Sets X-axis label.
    Syntax:
    ax.set_xlabel(label)

------------------------------------------------------------

7. ax.set_ylabel(): Sets Y-axis label.
    Syntax:
    ax.set_ylabel(label)

------------------------------------------------------------

8. ax.set_xlim(): Sets X-axis range.
    Syntax:
    ax.set_xlim(min, max)

    Parameters:
    min → Lower limit
    max → Upper limit

------------------------------------------------------------

9. ax.set_ylim(): Sets Y-axis range.
    Syntax:
    ax.set_ylim(min, max)

------------------------------------------------------------

10. ax.grid()
11. ax.legend()


------------------------------------------------------------

12. ax.tick_params(): Customizes axis ticks.
    Syntax:
    ax.tick_params(axis='x', labelsize=10)

    Parameters:
    axis      → 'x', 'y', 'both'
    labelsize → Tick label size
                (values: 8, 10, 12)


SUMMARY:
    - fig controls entire canvas
    - ax controls individual plots
    - ax methods replace plt.*
    - Object-Oriented API is preferred
    - More control, cleaner code
    
============================================================
'''


'''
------------------------------------------------------------
EXAMPLE 1: 1 ROW x 2 COLUMNS (SIDE-BY-SIDE COMPARISON)
------------------------------------------------------------
'''
# Create figure with 1 row and 2 columns
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

# First subplot (Line plot)
ax[0].plot(x, y, color='blue')
ax[0].set_title('Line Plot')
ax[0].set_xlabel('X values')
ax[0].set_ylabel('Y values')

# Second subplot (Bar chart)
ax[1].bar(x, y, color='green')
ax[1].set_title('Bar Chart')
ax[1].set_xlabel('X values')
ax[1].set_ylabel('Y values')

# Common title for entire figure
fig.suptitle('Comparison of Line and Bar Charts')

plt.tight_layout()
plt.show()



'''
------------------------------------------------------------
EXAMPLE 2: 2 ROWS x 1 COLUMN (VERTICAL COMPARISON)
------------------------------------------------------------

THEORY
------
- ax becomes a 1D array with 2 elements:
    ax[0] → top subplot
    ax[1] → bottom subplot
- Useful when plots share the same X-axis.
'''

import matplotlib.pyplot as plt

# Create figure with 2 rows and 1 column
fig, ax = plt.subplots(2, 1, figsize=(6, 8))

x = [1, 2, 3, 4]
y1 = [5, 15, 10, 20]
y2 = [20, 10, 15, 5]

# Top subplot (Scatter plot)
ax[0].scatter(x, y1, color='red')
ax[0].set_title('Scatter Plot')
ax[0].set_ylabel('Y1 values')
ax[0].grid(True)

# Bottom subplot (Histogram)
ax[1].hist(y2, bins=5, color='purple', edgecolor='black')
ax[1].set_title('Histogram')
ax[1].set_xlabel('Values')
ax[1].set_ylabel('Frequency')

# Common title
fig.suptitle('Vertical Subplots Example')

plt.tight_layout()
plt.show()




'''
            IMPORTANT ADDITIONAL CONCEPTS
 ---------------------------------------------------------

sharex:
  - Shares X-axis between subplots.
  - Zooming or changing limits affects all linked plots.
  - Values: True, False

sharey:
  - Shares Y-axis between subplots.
  - Useful for comparing values on same scale.
  - Values: True, False

fig.subplots_adjust():
  - Manually controls spacing between subplots.

  Syntax:
    fig.subplots_adjust(left, right, top, bottom,
                        wspace, hspace)

  Common values:
    wspace → horizontal spacing (0.1 - 0.5)
    hspace → vertical spacing   (0.1 - 0.5)


============================================================
            ADDITIONAL IMPORTANT AXES METHODS
============================================================

ax.text(): Adds simple text at a specific data position.

    Syntax:
    ax.text(x, y, text, fontsize=None, color=None)

    Parameters:
    x, y     → Data coordinates
    text     → Text string
    fontsize → Text size (10, 12, 14)
    color    → Text color

------------------------------------------------------------

ax.annotate(): Adds annotation with arrow pointing to a data point.

    Syntax:
    ax.annotate(text,
                xy=(x, y),
                xytext=(x2, y2),
                arrowprops=dict())

    Parameters:
    text        → Annotation text
    xy          → Point to annotate
    xytext      → Text position
    arrowprops → Arrow style dictionary

============================================================
'''

'''
------------------------------------------------------------
EXAMPLE 3: USING sharex, sharey, text(), annotate(),
           and subplots_adjust()
------------------------------------------------------------
'''

# Create subplots with shared axes
fig, ax = plt.subplots(2, 2, figsize=(10, 8),
                       sharex=True, sharey=True)

x = [1, 2, 3, 4]
y1 = [10, 20, 15, 25]
y2 = [12, 18, 14, 22]

# Plot 1
ax[0, 0].plot(x, y1, color='blue')
ax[0, 0].set_title('Line Plot 1')
ax[0, 0].text(2, 20, 'Peak', fontsize=10, color='red')

# Plot 2
ax[0, 1].plot(x, y2, color='green')
ax[0, 1].set_title('Line Plot 2')

# Plot 3
ax[1, 0].scatter(x, y1, color='purple')
ax[1, 0].set_title('Scatter Plot')

# Annotate a point
ax[1, 0].annotate('Important Point',
                  xy=(3, 15),
                  xytext=(2, 22),
                  arrowprops=dict(arrowstyle='->'))

# Plot 4
ax[1, 1].bar(x, y2, color='orange')
ax[1, 1].set_title('Bar Chart')

# Global title
fig.suptitle('Advanced Subplots Example')

# Adjust spacing manually
fig.subplots_adjust(wspace=0.3, hspace=0.4)

plt.show()


