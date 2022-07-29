import numpy as np
import matplotlib.pyplot as plt
import random
import time
from matplotlib import cm

x_size = 19
y_size = 19

x = 4
p = -15
pre_cursor = []
post_cursor = []

#for x in range(-15):
while x > -16:

    pre_cursor.append(str(x))
    post_cursor.append(str(p))
    p += 1
    x -= 1

#BERT = np.array(None,None)
'''
BERT = np.empty((x_size, y_size))

for y in range(x_size):
    for t in range(y_size):
        BERT[t,y] = random.randint(20, 350)
'''
BERT = np.array([ 
      [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],#4
      [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],#3
      [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],#2
      [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],#1
      [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2],#0
      [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2],#-1
      [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 0, 1, 1, 2, 2],#-2
      [2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 2],#-3
      [2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 2],#-4
      [2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 2],#-5
      [2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2],#-6
      [2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],#-7
      [2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],#-8
      [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2],#-9
      [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2],#-10
      [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 1, 2],#-11
      [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 1, 2, 2],#-12
      [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 2, 2, 2],#-13
      [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2],#-14
      [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]#-15

                    
                    ])

fig, ax = plt.subplots()
im = ax.imshow(BERT, cmap=cm.bwr)

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(post_cursor)), labels=post_cursor)
ax.set_yticks(np.arange(len(pre_cursor)), labels=pre_cursor)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
'''
for i in range(len(pre_cursor)):
    for j in range(len(post_cursor)):
        text = ax.text(j, i, BERT[i, j],
                       ha="center", va="center", color="w")
'''

ax.set_title("Fir sweep space")
fig.tight_layout()
plt.show()