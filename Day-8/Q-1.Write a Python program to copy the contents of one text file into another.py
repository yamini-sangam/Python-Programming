# open both files
with open('source.txt', 'r') as firstfile, open('destination.txt', 'a') as secondfile:
    # read content from first file
    for line in firstfile:
        # append content to second file
        secondfile.write(line)
