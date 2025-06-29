from time import time, strftime, gmtime

epoch = time()
epoch_struct= gmtime()

#string fornatting 
print(f"Seconds since January 1, 1970: {epoch:,.4f} or {epoch:.3} in scientific notation")
print(strftime("%b %d %Y", epoch_struct))