import time


class Timer:
    def __init__(self):
        self.timer_status = True    #To control the pause of the timer
        self.main_status = True     #To stop loop from stopping in case of time pausing

    def start(self, target_time):
        self.target_time = target_time
        self.x = 0           #out of loop so that the value becomes 0 only once
        while self.main_status:
            while self.timer_status:
                while self.x<=self.target_time:
                    time_remianing = self.target_time-self.x
                    print(f"Time Remaining: {time_remianing}")
                    time.sleep(1)
                    self.x += 1
                    break
                if self.x>=self.target_time:             #To break loop after the time is up
                    self.timer_status = False
                    self.main_status = False
                else:
                    break


    def stop(self):
        self.main_status=False

    def reset(self):
        self.x=0

    def resume(self):
        self.timer_status=True

    def pause(self):
        self.timer_status=False
        

if __name__ == '__main__':
    test = Timer()
    test.start(30)