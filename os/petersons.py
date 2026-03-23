# Demo Code from https://www.geeksforgeeks.org/dsa/petersons-algorithm-in-process-synchronization/

import threading
import time

N = 2
flag = [False] * N
turn = 0

def process(id):
    global turn
    other = 1 - id

    for _ in range(5): # I set it to manually run for 5 rounds, so it does not run forever
        flag[id] = True
        turn = other

        while flag[other] and turn == other:
            pass
        
        # Critical Section
        print(f"Process {id} is in the critical section")
        
        # Exit critical section
        flag[id] = False
        
        # Remainder Section
        print(f"Process {id} is in the remainder section")


if __name__ == '__main__':
    t1 = threading.Thread(target=process, args=(0,))
    t2 = threading.Thread(target=process, args=(1,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("Done!")