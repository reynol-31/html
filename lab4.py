#a case1
import matplotlib.pyplot as plt
categories = ['0-10', '10-20', '20-30', '30-40','40-50']
values = [55, 48, 25, 68, 90]
plt.bar(categories, values, color='skyblue’)
plt.xlabel('Overs’)
plt.ylabel('Runs’)
plt.title('Bar Plot Showing Runs scored in an ODI Match)
plt.show()

#case2
import matplotlib.pyplot as plt
import numpy as np
categories = ['0-10', '10-20', '20-30', '30-40', '40-50']
values1 = [55, 48, 25, 68, 90]
values2 = [65, 38, 35, 58, 80]
width=0.4
p=np.arange(len(categories))
p1=[j+width for j in p]
plt.xlabel('Overs', fontsize=15)
plt.ylabel('Runs', fontsize=15)
plt.bar(p, values1, width, color='yellow',label='Player1’)
plt.bar(p1, values2, width, color='red',label='Player2’)
plt.legend()
plt.xticks(p+width/2, categories)
plt.title('Bar Plot Showing Runs scored in an ODI Match’)
plt.show()
