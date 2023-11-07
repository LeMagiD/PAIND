import matplotlib.pyplot as plt
import time
from IPython.display import clear_output, display

data = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]

data_1=data[::-1]

fig, ax = plt.subplots()
ax.table(cellText=data, loc='center')

display(fig)
plt.show()
time.sleep(1)
clear_output(wait=True)
display(fig)






