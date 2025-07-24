from time import time, localtime, strftime

epoch = time()
local_time = localtime()

print(f"Seconds since January 1, 1970: {epoch:,.4f}", end='')
print(f" or {epoch:.2e} in scientific notation")
print(strftime("%b %d %Y", local_time))

# ',' is the thousands separator, Inserts a comma every 3 digits for
# integer presentation type 'd' and floating-point presentation types
# '.3e' formats the number in scientific (exponential)
# notation with 3 decimal places
