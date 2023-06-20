import os
import time

# set _ to 0 and clear the cmd (cmd is the console)
_ = 0
os.system('cls' if os.name == 'nt' else 'clear')

# print message here
while True:
    # change color to mod of _ and 9
    os.system('color '+['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'][_ % 9])
    # add 1 to _
    _ += 1
    # wait for 0.05 seconds
    time.sleep(0.05)
