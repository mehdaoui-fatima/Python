from time  import time, localtime, gmtime, strftime

epoch = time()
local_time = localtime()

# epoch_struct= gmtime()
# print(time.strftime("%b %d %Y", epoch_struct))
# print("Seconds since January 1, 1970: {0:,.4f} or {0:.2e} in scientific notation".format(epoch))# were 0 is the position of the arg of format

print(f"Seconds since January 1, 1970: {epoch:,.4f} or {epoch:.2e} in scientific notation")
print(strftime("%b %d %Y", local_time))

# ',' is the thousands separator, Inserts a comma every 3 digits for integer presentation type 'd' and floating-point presentation types
# '.3e' formats the number in scientific (exponential) notation with 3 decimal places