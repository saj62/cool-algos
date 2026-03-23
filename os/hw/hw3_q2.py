import threading
import time

count = 0
flag = [False, False]
turn = 0
ROUNDS = 8

def petersons(i):
    global count
    global turn
    
    for _ in range(ROUNDS):
        j = i - 1 # j is the "other" process
        flag[i] = True
        turn = j
        
        while flag[j] and turn == j:
            pass
        
        # critical section
        print(f"For Thread {i}, count = {count}")
        count += 1
        
        # set flag to False to exit critical section
        flag[i] = False
        
        
t0 = threading.Thread(target=petersons, args=(0,))
t1 = threading.Thread(target=petersons, args=(1,))

t0.start()
t1.start()

t0.join()
t1.join()

print("Final count =", count)