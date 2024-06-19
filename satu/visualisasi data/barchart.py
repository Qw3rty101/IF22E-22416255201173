import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [5, 12, 8, 15]

plt.bar(categories, values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title("Bar Chart Example")

plt.show()