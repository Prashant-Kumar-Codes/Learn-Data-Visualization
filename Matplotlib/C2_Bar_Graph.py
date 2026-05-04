import matplotlib.pyplot as plt
import pandas as pd

'''
------------------------------------------------------------
                        BAR GRAPH
------------------------------------------------------------

plt.bar():
     - Used to represent categorical data using
       rectangular bars, showing comparison between categories.

   Syntax:
     plt.bar(x, height, color=None, width=0.8, label=None,
             edgecolor=None, align='center', alpha=1.0)

   Parameters:
     x         → Categories or positions (list, array)
     height    → Bar heights/values (list, array)
     color     → Bar fill color
                 (values: 'blue', 'orange', 'green', etc.)
     width     → Width of bars
                 (values: 0.2 to 0.9)
     label     → Legend label (string)
     edgecolor → Border color of bars
                 (values: 'black', 'gray', etc.)
     align     → Alignment of bars relative to x
                 (values: 'center', 'edge')
     alpha     → Transparency of bars
                 (values: 0.0 to 1.0)

   Notes:
     - Can be used for single or grouped bar charts.
     - Works with positive and negative values.
     - Combining with plt.xticks() improves readability.


------------------------------------------------------------
'''

data = {
    'salesMonth' : ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'salesAmount' : [200000, 120000, 250000, 300000, 600000],
}
df = pd.DataFrame(data)

#plt.bar(x, height, color=None, width=0.8, label=None, edgecolor=None, align='center', alpha=1.0)


#using minimun parameters
plt.bar(df['salesMonth'], df['salesAmount'], color='yellow', label='Prices of different Vehicles')
plt.xlabel('Month')
plt.ylabel('Sales Amount')
plt.title('BarGraph - Prices of different vehicles in 2025')
plt.legend()
plt.show()


#customizing everything using more paramters and other functions
plt.bar(df['salesMonth'], df['salesAmount'], color='yellow', label='Prices of different Vehicles', width=0.5, edgecolor='red', align='edge', alpha=1)
plt.xlabel('Month')
plt.ylabel('Sales Amount')
plt.title('BarGraph - Prices of different vehicles in 2025')
plt.grid(True, 'both', 'y', linestyle=':', color='blue', linewidth='.5', alpha=0.6)
plt.legend()
plt.show()






