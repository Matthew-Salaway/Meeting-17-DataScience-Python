# Copy this code into your own repl. Click the navigation bar in the top left corner and go to My Repl.
# Click the New Repl on the left, create the repl, and paste the code. Or put into another IDE.

# Today we will be finishing our data analysis by utilizing data visualization.
# The question we are trying to answer is likely asked by someone who has no connection
# to computer science, so giving them an array and explaining it to them is impractical

# Thus, we turn the data into a visual that is easy to read and understand, such as a chart or graph

# Certain graphs are better than others, so we will be using a bar graph so it can be easy to read and compare.

# Here is an example of how to create a simple bar graph

import matplotlib.pyplot as plt
import pandas as pd

# create data
df = pd.DataFrame([['A', 10, 20, 10, 30], ['B', 20, 25, 15, 25], ['C', 12, 15, 19, 6],
				['D', 10, 29, 13, 19]],
				columns=['Team', 'Round 1', 'Round 2', 'Round 3', 'Round 4'])
# view data
print(df)

x = df["Team"]      # labels for x axis
y = df['Round 1']   # Corresponding y-values for the lables
plt.bar(x, y)
plt.show()

#---------------------------------------------------------

# Now try with the last top 10 data frame we created last meeting. Make the y value total sales
# I converted the last data frame to a list I can copy and paste with print(topTen.to_numpy().tolist())
# Here is the result: [['Nintendo', 1786.5599999999981, 816.8700000000001, 418.7400000000002, 455.4199999999995], ['Electronic Arts', 1110.3199999999915, 595.069999999998, 371.2699999999965, 14.039999999999958], ['Activision', 727.4599999999983, 429.6999999999991, 215.53000000000037, 6.539999999999987], ['Sony Computer Entertainment', 607.4999999999989, 265.2199999999993, 187.72000000000017, 74.10000000000004], ['Ubisoft', 474.71999999999935, 253.43000000000043, 163.31999999999968, 7.499999999999993], ['Take-Two Interactive', 399.5399999999996, 220.4900000000005, 118.14000000000017, 5.829999999999992], ['THQ', 340.7699999999994, 208.7700000000004, 94.73000000000019, 5.009999999999998], ['Konami Digital Entertainment', 283.639999999998, 92.15999999999998, 69.6900000000002, 91.3], ['Sega', 272.98999999999927, 109.39999999999996, 82.00000000000013, 57.030000000000015], ['Namco Bandai Games', 254.0900000000008, 69.5200000000001, 42.63000000000004, 127.07000000000008]]
topTen = pd.DataFrame([['Nintendo', 1786.5599999999981, 816.8700000000001, 418.7400000000002, 455.4199999999995], ['Electronic Arts', 1110.3199999999915, 595.069999999998, 371.2699999999965, 14.039999999999958], ['Activision', 727.4599999999983, 429.6999999999991, 215.53000000000037, 6.539999999999987], ['Sony Computer Entertainment', 607.4999999999989, 265.2199999999993, 187.72000000000017, 74.10000000000004], ['Ubisoft', 474.71999999999935, 253.43000000000043, 163.31999999999968, 7.499999999999993], ['Take-Two Interactive', 399.5399999999996, 220.4900000000005, 118.14000000000017, 5.829999999999992], ['THQ', 340.7699999999994, 208.7700000000004, 94.73000000000019, 5.009999999999998], ['Konami Digital Entertainment', 283.639999999998, 92.15999999999998, 69.6900000000002, 91.3], ['Sega', 272.98999999999927, 109.39999999999996, 82.00000000000013, 57.030000000000015], ['Namco Bandai Games', 254.0900000000008, 69.5200000000001, 42.63000000000004, 127.07000000000008]], columns = ["Publisher", "Total Sales", "North American Sales", "European Sales", "Japan Sales"])
print(topTen)



#------------------------

# We can also make a grouped bar graph with multiple sub plots like: https://chartio.com/assets/602df8/tutorials/charts/grouped-bar-charts/4dfa611bb816aa179112fb5a362e3feb52f1901781c5fc14f9c8e55e6d45aefd/grouped-bar-options-4.png
# That way we could plot the total, NA, EU, and Japan sales all next to each other.
# However, this is a bit complex and difficult for me to explain as data visualization is new to me.
# Here is what I got to...
