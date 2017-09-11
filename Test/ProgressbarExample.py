from progressbar import ProgressBar
import time

bar = ProgressBar()
for i in bar(range(50)):
    time.sleep(0.1)
    print()

