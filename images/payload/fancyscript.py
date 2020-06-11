import time
import sys

print('this is a user script.. computing sth important')

inputfile = sys.argv[1]
outputfile = sys.argv[2]

for i in range(20):
    print(f'compute {i}')
    time.sleep(1)

with open(inputfile,'r') as inp:
    with open(outputfile,'w') as out:
        out.write('--- this is the output of the fancy script\n')
        out.write('--- based on input:\n')
        out.write(inp.read())
        out.write('\n')
        out.write('--- done!\n')

print(f'computing done.. output at {outputfile}')