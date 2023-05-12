import numpy as np  # import the numpy library
import statistics  # import the statistics module

# Open file(input.txt) and read the file
with open('input.txt') as fin:
    text = fin.read()

# open file(out.txt) in write mode
f = open("out.txt", "w")

for line in text.split('\n'):  # loop through each line of the text file
    # split the line into the operation and the list of numbers
    op, nums = line.split(':')

    op = op.strip()  # strip any whitespace from the operation

    nums = map(float, nums.strip().split(','))  # convert the list of numbers to floats and strip any whitespace

    if op == 'Avg':  # if the operation is Average
        # write the mean of numbers to the file
        f.write('\n The value of average of {} is {}'.format(nums, str(statistics.mean(nums))))

    if op == 'Min':  # if the operation is min
        # write the min of numbers to the file
        f.write('\n The value of min of {} is {}'.format(nums, str(min(nums))))

    if op == 'Max':  # if the operation is max
        # write the max of numbers to the file
        f.write('\n The value of max of {} is {}'.format(nums, str(max(nums))))

f.close()  # close the file

# open the file out.txt in read mode
f = open("out.txt", "r")

# print the contents of the file
print(f.read())

# Please Check this code in your IDLE , I am having issues importing the statistics module
