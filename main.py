# Importing numpy
import numpy
# Importing matplotlib
import matplotlib.pyplot as plt

# Challenge 1

# Numbers ranging from 1 to 20
numbers = numpy.arange(0, 20)

# Finding the Mean from the numbers given
my_mean = numpy.mean(numbers)
print("The mean is: ", my_mean)

# Finding the Standard Deviation from the numbers given
my_std = numpy.std(numbers)
print("The standard deviation is ", my_std)

# Finding the Variance from the numbers given
my_var = numpy.var(numbers)
print("The variance of the marks is  ", my_var)

# Challenge 2

# A range of numbers
nums = [0.5, 0.7, 1, 1.2, 1.3, 2.1]
bins = [0, 1, 2, 3]

result = numpy.histogram(nums, bins)
print("Nums: " + str(nums))
print("Bins: " + str(bins))
print(result)

# Plotting the data on the graph
plt.hist(nums, bins)
# Labeling the x axis
plt.xlabel("Nums")
# Labeling the y axis
plt.ylabel("Bins")
# Giving the histogram a title
plt.title("Histogram of nums against bins")
# Initializing the graph
plt.show()
