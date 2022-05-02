def swapFileData()
with open(File 1, 'r') as a:
data_a=a.read()
with open(File 2, 'w') as b:
data_a=a.read()
with open(File 1, 'w') as a:
a.write(data_b)
with open(File 2, 'r') as b:
a.write(data_a)