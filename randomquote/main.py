import time
import random

#This will be shown in the command line
print('If you want random motivational quote please type run in start.txt and save')

while True:
    #Open the start.txt and read for 'run'
    start_file = open('./start.txt', 'r')
    linecheck = start_file.readline()
    start_file.close()
    #if 'run' was found start the process for random choosing
    if linecheck == 'run':
        print('Choosing random inspiration quote from file~')

        # read through 100 lines of text and split each lines.
        read_file = open("motivation.txt", 'r')
        line = read_file.read().splitlines()
        read_file.close()

        # overwrite start.txt file by choosing random line.
        random_line = open('./start.txt', 'w')
        random_line.write(random.choice(line))
        random_line.close()

        time.sleep(3)
        print('\nFile Overwritten! check start.txt to see your motivation code!')
        print('\nif different quote wanted type run in the start.txt file')

