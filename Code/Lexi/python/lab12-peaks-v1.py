# Lab 12 - GUI

# givens
data = [1 ,2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# make sequences - lists are easiest to change
peaks = []
valleys = []      # Sam helped me with lines 14, 16 - list wasn't populating
peaks_n_valleys = []

# go through each of the above sequences
for i in range(1, len(data)-1):           #for loop (begin, end)
  if data[i] > data[i-1] and data[i] > data[i+1]:
    peaks.append(i)        # adding to peaks set
  if data[i] < data[i-1] and data[i] < data[i+1]:         # SAM caught this dumb mistake I did I switched out i-1 with i+1
    valleys.append(i)      # adding to valley set

# add them into line 9's set
peaks_n_valleys = peaks + valleys

# Graphical User Interface (something an end user comprehends)
for i in range(max(data), min(data), -1):
# above for loop sets what we 'go through' in our below loop (beginning, end, how we go through)

  for j in range(len(data)): # taking our list on line 4 and going through
    if data[j] >= i:         # if the number in our data list is greater than
      print("X", end=" ")
    else:
      print(" ", end=" ")
  print()

# need to print out the above for loop in line 22

print(f'The data is {data}')
print(f'The peaks are: {peaks}')
# only this print statement is working
print(f'The respective valleys are at: {valleys}')