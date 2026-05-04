import matplotlib.pyplot as plt

'''
============================================================
        IMPORTANT pyplot FUNCTIONS - DETAILED NOTES
============================================================

1. plt.plot()
     - Used to draw line plots showing trends or relationships
       between continuous variables.

   Syntax:
     plt.plot(x, y, color=None, linestyle='-', linewidth=1, marker='symbol', label=None)

   Parameters:
     x         → X-axis data (list, array)
     y         → Y-axis data
     color     → Line color
                 (values: 'red', 'blue', 'green', 'black', etc.)
     linestyle → Style of line
                 (values: '-', '--', '-.', ':')
     linewidth → Thickness of line
                 (values: 1, 2, 3, ...)'
     marker    → Symbol to show the point
                 (values: 'o', 'x', 'p', '^',  or many others) 
     label     → Legend label (string)

------------------------------------------------------------

2. plt.xlabel()
     - Sets label for the X-axis.

   Syntax:
     plt.xlabel("label", fontsize=None)

   Parameters:
     label    → X-axis name (string)
     fontsize → Size of label text
                (values: 10, 12, 14, 16)

------------------------------------------------------------

3. plt.ylabel()
     - Sets label for the Y-axis.

   Syntax:
     plt.ylabel("label", fontsize=None)

   Parameters:
     label    → Y-axis name (string)
     fontsize → Size of label text
                (values: 10, 12, 14, 16)

------------------------------------------------------------

4. plt.title()
     - Adds a title describing
       the entire plot.

   Syntax:
     plt.title("title", fontsize=None)

   Parameters:
     title    → Plot title text (string)
     fontsize → Title text size
                (values: 12, 14, 18, 20)

------------------------------------------------------------

5. plt.legend()
   Explanation:
     - Displays legend explaining
       plotted elements.

   Syntax:
     plt.legend(loc='best')

   Parameters:
     loc → Position of legend
            (values: 'best', 'upper right',
                     'upper left', 'lower right',
                     'lower left')

------------------------------------------------------------

6. plt.grid()
     - Adds grid lines to the plot to improve
       readability, alignment, and value estimation.

   Syntax:
     plt.grid(visible=True, which='major', axis='both',
              linestyle='-', linewidth=0.8, color=None, alpha=0.5)

   Parameters:
     visible   → Show or hide grid
                 (values: True, False)

     which     → Type of grid lines
                 (values: 'major', 'minor', 'both')

     axis      → Axis on which grid is applied
                 (values: 'x', 'y', 'both')

     linestyle → Style of grid lines
                 (values: '-', '--', '-.', ':')

     linewidth → Thickness of grid lines
                 (values: 0.5, 0.8, 1.0, ...)

     color     → Color of grid lines
                 (values: 'gray', 'black', 'blue', etc.)

     alpha     → Transparency level
                 (values: 0.0 to 1.0)


------------------------------------------------------------

============================================================
7.             AXIS LIMITS (xlim & ylim)
============================================================

Axis limits define the visible range of data
on the X-axis and Y-axis.

------------------------------------------------------------

    1. plt.xlim()
        - Sets or returns the visible range of values
        on the X-axis to focus on specific data regions.

    Syntax:
        plt.xlim(left=None, right=None)

    Parameters:
        left   → Minimum value of X-axis
                (values: numeric)

        right  → Maximum value of X-axis
                (values: numeric)

    Notes:
        - If no parameters are passed, current limits are returned.
        - Passing only one limit leaves the other unchanged.

    ------------------------------------------------------------

    2. plt.ylim()
        - Sets or returns the visible range of values
        on the Y-axis for better data emphasis.

    Syntax:
        plt.ylim(bottom=None, top=None)

    Parameters:
        bottom → Minimum value of Y-axis
                (values: numeric)

        top    → Maximum value of Y-axis
                (values: numeric)

    Notes:
        - If no parameters are passed, current limits are returned.
        - Partial limits are allowed.

    ------------------------------------------------------------

    3. Combined Usage (Shortcut Form)

    Syntax:
        plt.xlim(min_value, max_value)
        plt.ylim(min_value, max_value)

    Purpose:
        - Quickly zoom in or out on
        a specific data range.

    ------------------------------------------------------------

    4. Inverted Axis (Important)

    Syntax:
        plt.xlim(max_value, min_value)
        plt.ylim(max_value, min_value)

    Explanation:
        - Reverses the direction of an axis
        (commonly used in ranking plots).

    ------------------------------------------------------------

    5. Best Practices (Professional)

    - Always set axis limits AFTER plotting data.
    - Avoid clipping important data points.
    - Use limits to improve clarity, not to mislead.



============================================================
8.             AXIS TICKS (Matplotlib)
============================================================

Axis ticks are the small marks and labels shown along
the X-axis and Y-axis that indicate data scale and values.

------------------------------------------------------------

    1. plt.xticks()
        - Sets or customizes tick positions and labels
        on the X-axis for better scale control.

    Syntax:
        plt.xticks(ticks=None, labels=None,
                    rotation=0, fontsize=None)

    Parameters:
        ticks     → Positions of ticks on X-axis
                    (values: list or array)

        labels    → Custom tick labels
                    (values: list of strings)

        rotation  → Rotation angle of labels
                    (values: 0, 45, 90)

        fontsize  → Size of tick labels
                    (values: 8, 10, 12, 14)

    ------------------------------------------------------------

    2. plt.yticks()
        - Sets or customizes tick positions and labels
        on the Y-axis for better scale readability.

    Syntax:
        plt.yticks(ticks=None, labels=None,
                    rotation=0, fontsize=None)

    Parameters:
        ticks     → Positions of ticks on Y-axis
                    (values: list or array)

        labels    → Custom tick labels
                    (values: list of strings)

        rotation  → Rotation angle of labels
                    (values: 0, 45, 90)

        fontsize  → Size of tick labels
                    (values: 8, 10, 12, 14)

    ------------------------------------------------------------

    3. Tick Frequency Control (Important)

    Common Methods:
        - plt.xticks(range(start, stop, step))
        - plt.yticks(range(start, stop, step))

    Purpose:
        - Controls number and spacing of ticks
        on an axis.

    ------------------------------------------------------------

    4. Minor Ticks (Advanced but Important)

    Syntax:
        plt.minorticks_on()

    Explanation:
        - Enables minor ticks between major ticks
        for finer scale visualization.

    ------------------------------------------------------------

    5. Tick Direction and Appearance (Using Axes)

    Syntax:
        plt.tick_params(axis='both', which='major',
                        direction='out', length=6, width=1)

    Parameters:
        axis      → Axis to modify
                    (values: 'x', 'y', 'both')

        which     → Type of ticks
                    (values: 'major', 'minor', 'both')

        direction → Direction of ticks
                    (values: 'in', 'out', 'inout')

        length    → Length of tick marks
                    (values: 4, 6, 8)

        width     → Thickness of ticks
                    (values: 0.5, 1, 1.5)

============================================================

tight_layout():
    - Automatically adjusts spacing between subplots
      to prevent overlapping of titles, labels, and ticks.

  Syntax:
    plt.tight_layout()
      OR (Object-Oriented style):
    fig.tight_layout()

  Parameters:
    w_pad
    h_pad
    rec
  
------------------------------------------------------------

9 plt.show():
      - Displays the final plot window
        after all plotting commands.

    Syntax:
      plt.show()

    Parameters:
      None

============================================================
'''



x = ['Mon', 'Tue', 'Web', 'Thru', 'Fri', 'Sat', 'Sun']
y = [1000, 2000, 3000, 2200, 3211, 9000, 6790]

#plt.plot(x, y, color=None, linestyle='-', linewidth=1, marker='symbol' label=None)

#ploting without using any parameters of the .plot()
plt.plot(x,y)
plt.title('Sales Data')
plt.xlabel('Days')
plt.ylabel('Sales Amount')
plt.tight_layout()
plt.show()

#ploting with using pateters of the .plot()
plt.plot(x,y, color='red', linestyle = ':', linewidth='2', marker='^', label='Data of seles of abc company')
plt.title('Sales Data')
plt.xlabel('Days')
plt.ylabel('Sales Amount')
plt.legend(loc='best')  # it will show when label is set(in .plot())
plt.grid(visible=True, color='gray', which='both', linestyle=':', linewidth=1, axis='both', alpha=.5)
plt.show()

#ploting with using any parameters of the .plot() including Axis Ticks and Axis limits
plt.plot(x,y, color='red', linestyle = ':', linewidth='2', marker='^', label='Data of seles of abc company')
plt.title('Sales Data')
plt.xlabel('Days')
plt.ylabel('Sales Amount')
plt.legend(loc='upper left')  # it will show when label is set(in .plot())
plt.grid(visible=True, color='gray', which='both', linestyle=':', linewidth=1, axis='both', alpha=.5)
plt.xticks([1,2,3,4,5,6,7], ['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7'])
plt.xlim(0, 7)
plt.ylim(0, 10000)
plt.show()