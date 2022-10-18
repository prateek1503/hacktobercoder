import time
import math
con = input("SnowflakeID ")
dec = int(con)/4194304
ms = math.trunc(int(dec)+1420070400000)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ms/1000.)))
