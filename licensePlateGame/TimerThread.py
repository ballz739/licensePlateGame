import threading
import time
from Logger import * 

class TimerThread(threading.Thread):
    def __init__(self, name, delay, logger):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay
        self.logger = logger
        self.exitFlag = False
        return

    #def start(self):
        #self.logger.writeLog('Starting ' + self.name, LogLevel.Inf)
        #self.exitFlag = False
        #self.doWork(self.name, self.delay)

    def run(self):
        while not self.exitFlag:
            time.sleep(self.delay)
            self.logger.writeLog('%s: %s' % (self.name, time.ctime(time.time())), LogLevel.Inf)
        self.logger.writeLog('Exiting ' + self.name, LogLevel.Inf)
        return

    def stop(self):
        self.exitFlag = True
        
