import time

def timer(t):
    x=0
    while x<=t:
        print(f"Time Remaining: {t-x}", end='\r')
        time.sleep(1)
        x+=1

timer(5)
