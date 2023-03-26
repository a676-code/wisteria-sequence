
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# returns the product of the nonzero digits in num
def productNonzeroDigits(num):
    string = [char for char in str(num)]
    product = 1
    for s in string:
        if int(s) != 0:
            product *= int(s)
    return product

# generates the wisteria sequence up to the n-th number
def generate_wisteria(n):
    sequence = []
    i = 1
    while len(sequence) < n:
        sequence.append(i - productNonzeroDigits(i))
        i += 1
    return sequence

print(generate_wisteria(30))

# Basic scatterplots
n = 100
sequence = generate_wisteria(n)
df = pd.DataFrame(sequence, columns=['Number'])
df['index'] = [i for i in range(n)]
sns.scatterplot(x="index",y = "Number", data=df)
plt.show()

n = 1000
sequence = generate_wisteria(n)
df = pd.DataFrame(sequence, columns=['Number'])
df['index'] = [i for i in range(n)]
sns.scatterplot(x="index",y = "Number", data=df)
plt.show()

n = 10000
sequence = generate_wisteria(n)
df = pd.DataFrame(sequence, columns=['Number'])
df['index'] = [i for i in range(n)]
sns.scatterplot(x="index",y = "Number", data=df)
plt.show()

n = 100000
sequence = generate_wisteria(n)
df = pd.DataFrame(sequence, columns=['Number'])
df['index'] = [i for i in range(n)]
sns.scatterplot(x="index",y = "Number", data=df)
plt.show()

# Plots of Averages
n = 100
sequence = generate_wisteria(n)
average_sequence = []
total = 0
for i, s in enumerate(sequence):
    total += s
    average = total / (i + 1)
    average_sequence.append(average)

df = pd.DataFrame(average_sequence, columns=["Average"])
df['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y="Average", data=df)
plt.show()

n = 1000
sequence = generate_wisteria(n)
average_sequence = []
total = 0
for i, s in enumerate(sequence):
    total += s
    average = total / (i + 1)
    average_sequence.append(average)

df = pd.DataFrame(average_sequence, columns=["Average"])
df['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y="Average", data=df)
plt.show()

n = 10000
sequence = generate_wisteria(n)
average_sequence = []
total = 0
for i, s in enumerate(sequence):
    total += s
    average = total / (i + 1)
    average_sequence.append(average)

df = pd.DataFrame(average_sequence, columns=["Average"])
df['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y="Average", data=df)
plt.show()

n = 100000
sequence = generate_wisteria(n)
average_sequence = []
total = 0
for i, s in enumerate(sequence):
    total += s
    average = total / (i + 1)
    average_sequence.append(average)

df = pd.DataFrame(average_sequence, columns=["Average"])
df['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y="Average", data=df)
plt.show()