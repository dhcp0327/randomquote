import time
import random

print('If you want random motivational quote please type run in start.txt and save')

while True:

    start_file = open('./start.txt', 'r')
    linecheck = start_file.readline()
    start_file.close()
    if linecheck == 'run':
        print('Choosing random inspiration quote from file~')

        # read through 100 lines of text and split each lines.
        read_file = open("motivation.txt", 'r')
        line = read_file.read().splitlines()
        read_file.close()

        # overwrite start.txt file by choosing random line.
        x = open('./start.txt', 'w')
        x.write(random.choice(line))
        x.close()

        time.sleep(3)
        print('\nFile Overwritten! if different quote wanted type run in the start.txt file')
