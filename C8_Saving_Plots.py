import matplotlib.pyplot as plt
import random

'''
savefig():

Work:
    - Saves the current figure to a file
      instead of (or in addition to) displaying it.
      
-----------------------------------------------------

Syntax:
    plt.savefig(filename, dpi=None, bbox_inches=None)
        OR (Object-Oriented style):
    fig.savefig(filename, dpi=None, bbox_inches=None)

-----------------------------------------------------

Parameters:
    fname      → Name of output file
                    (values: 'plot.png', 'chart.jpg',
                                'figure.pdf', 'image.svg')

    dpi           → Resolution (dots per inch)
                    (values: 100, 200, 300)

    bbox_inches   → Controls extra whitespace
                    (values: 'tight', None)

-----------------------------------------------------

IMPORTANT NOTES:
  - Save BEFORE plt.show() to avoid blank images
  - File format is inferred from file extension
  - High dpi is used for print quality

-----------------------------------------------------

WHEN TO USE:
  - Exporting plots for reports or papers
  - Saving ML results and visualizations
  - Reusing plots without rerunning code

-----------------------------------------------------

COMMON MISTAKES:
  - Calling savefig() after plt.show()
  - Forgetting file extension
  - Using low dpi for printed figures

------------------------------------------------------------
'''


def gen_ran_num_list(length, lower_limit ,upper_limit):
      lis = []
      for i in range(length):
            lis.append(random.randint(lower_limit, upper_limit))
      return lis

x = gen_ran_num_list(10, 1, 10)
y = [i*10 for i in x]

plt.plot(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Saving the figrue')
plt.savefig(fname='Line_Graph.png', dpi=250, bbox_inches='tight')
plt.show()
