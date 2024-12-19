# case 1
import matplotlib.pyplot as plt
age_men = [25,11,68,18,27,28,15,43,58,63,43,65,51,36,33,26,23,35,49,58]
plt.hist(age_men, bins=6)
plt.show()

# case 2)
bins =[10,20,30,40,50,60,70]
plt.hist(age_men, bins=bins, edgecolor='r', )
plt.show()

# case 3)
from matplotlib import style
style.use('fivethirtyeight')
plt.hist(age_men, bins=10,edgecolor='y', color='g', rwidth=0.7)
plt.xlabel('Age of people', fontsize=20)
plt.ylabel('Number of people', fontsize=20)
plt.title('Age vs number of people', fontsize=20)
plt.show()

# case 4)
age_men = [25,11,68,18,27,28,15,43,58,63,43,65,51,36,33,26,23,35,49,58]
age_women = [48,57,59,25,19,37,18,56,22,25,56,25,14,49,53,45,46,19,28,70, 31]
plt.figure(figsize=(6,6))
style.use('ggplot')
bins =[10,20,30,40,50,60,70]
plt.hist([age_men, age_women], bins=bins, color=['blue', 'orange'],rwidth=0.5, label=['men', 'women'])
plt.xlabel('Age of people', fontsize=20)
plt.ylabel('Number of people', fontsize=20)
plt.title('Age vs number of people', fontsize=20)
plt.legend(loc='upper right')
plt.show()


#b


import matplotlib.pyplot as plt
exp_vals = [1400,600,300,410,250]
exp_labels = ["Home Rent","Food","Phone/Internet Bill","Car ","Other Utilities"]
plt.pie(exp_vals,labels=exp_labels, shadow=True)
plt.show()

# pie chart with perfect circle
plt.pie(exp_vals,labels=exp_labels, shadow=True,
autopct='%0.1f%%',radius=1.5)
plt.show()

# Explode
plt.pie(exp_vals,labels=exp_labels, shadow=True,
autopct='%1.1f%%',radius=1.5,explode=[0,0,0,0.2,0.1])
plt.show()

# counterclock and angle properties
plt.pie(exp_vals,labels=exp_labels, shadow=True, autopct='%1.1f%%',
radius=1.5,explode=[0,0,0,0.1,0.2],counterclock=False, startangle=30)
plt.show()
