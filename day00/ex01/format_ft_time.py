import time

epoch = time.time()
# epoch_struct= time.gmtime()
local_time = time.localtime()

#string fornatting 
print(f"Seconds since January 1, 1970: {epoch:,.4f} or {epoch:.2e} in scientific notation")
# print(time.strftime("%b %d %Y", epoch_struct))
print(time.strftime("%b %d %Y", local_time))