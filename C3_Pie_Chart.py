import matplotlib.pyplot as plt
import pandas as pd

'''
plt.pie():
     - Used to represent proportions of data
       as slices of a circular chart.

   Syntax:
     plt.pie(data, labels=None, autopct=None, startangle=0,
             colors=None, explode=None, shadow=False,
             counterclock=True)

   Parameters:
     data/values → Values for each slice(numeric data only)
                    (list or array)
     labels      → Slice labels
                    (list of strings)
     autopct     → Percentage display format
                    (values: '%1.1f%%', '%1.0f%%')
     startangle  → Starting rotation angle
                    (values: 0, 90, 180)
     colors      → Colors for slices
                    (list of color names or hex codes)
     explode     → Separation of slices
                    (values: list like [0, 0.1, 0])
     shadow      → Adds shadow effect
                    (values: True, False)
     counterclock → Direction of slice drawing
                     (values: True, False)

   Notes:
     - Sum of data values represents 100%.
     - Best used for small datasets.
     - Avoid using too many slices for clarity.

------------------------------------------------------------
'''

student_df = pd.DataFrame({
    'StudentID': range(1, 21),
    'Age': [18, 19, 20, 21, 18, 19, 20, 21, 22, 18,
            19, 20, 21, 22, 18, 19, 20, 21, 22, 23],
    'Marks': [72, 85, 78, 90, 66, 88, 74, 92, 81, 69,
              87, 76, 91, 83, 70, 89, 75, 93, 84, 86],
    'Attendance': [85, 90, 88, 95, 80, 92, 87, 96, 89, 82,
                   91, 86, 94, 90, 83, 93, 88, 97, 91, 92],
    'StudyHours': [2, 3, 2.5, 4, 1.5, 3.5, 2, 4.5, 3, 1.8,
                   3.2, 2.4, 4.1, 3.6, 2, 3.8, 2.6, 4.7, 3.9, 4]
})

x = ['Mon', 'Tue', 'Web', 'Thru', 'Fri', 'Sat', 'Sun']
y = [1000, 2000, 3000, 2200, 3211, 9000, 6790]

#Syntax: 
#   plt.pie(data, labels=None, autopct=None, startangle=0, colors=None, explode=None, shadow=False, counterclock=True)

values = [1000, 2000, 3000, 2200, 3211, 9000, 6790]
labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# ------------------------------------------------
# 1) Basic pie chart
# ------------------------------------------------
plt.pie(values, labels=labels)
plt.title("Weekly Sales")
plt.show()


# ------------------------------------------------
# 2) Pie chart with percentage display
# ------------------------------------------------
plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title("Weekly Sales (%)")
plt.show()


# ------------------------------------------------
# 3) Pie chart with start angle
# ------------------------------------------------
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Weekly Sales (Rotated)")
plt.show()


# ------------------------------------------------
# 4) Pie chart with exploded slices
# ------------------------------------------------
explode = [0, 0, 0, 0, 0.1, 0.2, 0]  # highlight Fri & Sat

plt.pie(values, labels=labels, autopct='%1.1f%%', explode=explode)
plt.title("Highlighted High Sales Days")
plt.show()


# ------------------------------------------------
# 5) Pie chart with shadow effect
# ------------------------------------------------
plt.pie(values, labels=labels, autopct='%1.1f%%', shadow=True)
plt.title("Weekly Sales with Shadow")
plt.show()


# ------------------------------------------------
# 6) Counter-clockwise pie chart
# ------------------------------------------------
plt.pie(values, labels=labels, autopct='%1.1f%%', counterclock=False)
plt.title("Clockwise Pie Chart")
plt.show()


# ------------------------------------------------
# 7) Pie chart without labels (legend-style usage)
# ------------------------------------------------
plt.pie(values, autopct='%1.1f%%')
plt.legend(labels, loc='lower left')
plt.title("Weekly Sales (Legend Based)")
plt.show()

