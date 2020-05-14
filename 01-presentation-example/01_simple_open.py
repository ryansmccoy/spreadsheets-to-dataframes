

filename = r'data\WMT_US.csv'

f = open(filename, 'r')

print(f)

data = f.read()

print(data)

f.close()

f = open(filename, 'r')  # open file

for line in f:
    print(line)

f.close()  # close file
