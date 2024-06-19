import matplotlib.pyplot as plt

labels = ['Category A', 'Category B', 'Category C']
sizes = [25,40,35]

plt.pie(sizes, labels = labels, autopct='1%.1f%%')
plt.title("Pie Chart Example")

plt.show()