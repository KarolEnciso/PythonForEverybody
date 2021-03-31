# Open the file romeo.txt and read it line by line. For each line, split the
# line into a list of words using the split() method. The program should build
# a list of words For each word on each line check to see if the word is
# in the list and if not append it to the list. When the program completes,
# already sort and print the resulting words in alphabetical order.

fname = input("Enter file name: ")
fh = open(fname)
rd = fh.read()
sep = rd.split()
sep.sort()
pals_uq = list()
for pal in sep:
    if pal not in pals_uq:
        pals_uq.append(pal)
print(pals_uq)
