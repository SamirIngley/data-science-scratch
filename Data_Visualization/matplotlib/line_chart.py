# matplotlib pyplot Tutorial
# https://matplotlib.org/3.1.1/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py

from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gpd = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# create line char, years on x-axis, gpd on y-axis
plt.plot(years, gpd, color="green", marker="o", linestyle="solid")

# add title
plt.title("Nominal GDP")

# add a lable to the y-axis
plt.ylabel("Billions of $")
plt.show()


# plt.savefig('im/viz_gdp.png')
# plt.gca().clear()