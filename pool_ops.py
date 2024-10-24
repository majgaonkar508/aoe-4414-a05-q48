# pool_ops.py
#
# Usage: pool_ops.py c_in h_in w_in h_pool w_pool s p
# Script to determine the output shape and operation count of 
# an average pooling layer. 
# Parameters:
# c_in: input channel count
# h_in: input height count
# w_in: input width count
# h_pool: average pooling kernel height count
# w_pool: average pooling kernel width count
# s: stride of average pooling kernel
# p: amount of padding on each of the four input map sides
# Output (all int):
#  c_out: output channel count
#  h_out: output height count
#  w_out: output width count
#  adds: number of additions performed
#  muls: number of multiplications performed
#  divs: number of divisions performed
# Written by Mandar Ajgaonkar
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import sys # argv

# initialize script arguments
c_in = float('nan')   
h_in = float('nan')   
w_in = float('nan')   
h_pool = float('nan') 
w_pool = float('nan') 
s = float('nan')      
p = float('nan')

# parse script arguments
if len(sys.argv) == 8:
  c_in = float(sys.argv[1])
  h_in = float(sys.argv[2])
  w_in = float(sys.argv[3])
  h_pool = float(sys.argv[4])
  w_pool = float(sys.argv[5])
  s = float(sys.argv[6])
  p = float(sys.argv[7])
  ...
else:
  print(\
   'Usage: '\
   'python3 pool_ops.py c_in h_in w_in h_pool w_pool s p'\
  )
  exit()

# determine output channel count
c_out = c_in

# calculate height of output map
h_out = (h_in + 2*p - h_pool)/s + 1 

# calculate width of output map
w_out = (w_in + 2*p - w_pool)/s + 1 

# calculate number of additions, multiplications, and divisions
adds = c_in*h_out*w_out*(h_pool*w_pool - 1)
muls = 0 # no multiplications required
divs = c_in*h_out*w_out

# print results
print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed