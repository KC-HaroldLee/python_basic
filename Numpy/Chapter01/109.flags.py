import numpy as np

a = np.array([1,2,3,4])
print(a.flags) 
# C_CONTIGUOUS : True
# F_CONTIGUOUS : True
# OWNDATA : True
# WRITEABLE : True
# ALIGNED : True
# WRITEBACKIFCOPY : False
# UPDATEIFCOPY : False

npa = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[0,0,0]]])
npa_flatten = npa.flatten()
npa_raveled = npa.ravel()

print(npa.flags)
print(npa_flatten.flags)
print(npa_raveled.flags)

# 비교를 위해 
# C_CONTIGUOUS : True / True / True
# F_CONTIGUOUS : False / True / True
# OWNDATA : True / True / False
# WRITEABLE : True / True / True
# ALIGNED : True / True / True
# WRITEBACKIFCOPY : False / False / False
# UPDATEIFCOPY : False / False / False

npa_ref = npa
npa_copy = np.array(npa)

print(npa_ref.base is npa) # False
print(npa_copy.base is npa) # False
print(npa_flatten.base is npa) # False
print(npa_raveled.base is npa) # True

npa_frombuffer = np.frombuffer(npa)
print(npa_frombuffer.flags)
#   C_CONTIGUOUS : True
#   F_CONTIGUOUS : True
#   OWNDATA : False
#   WRITEABLE : True
#   ALIGNED : True
#   WRITEBACKIFCOPY : False
#   UPDATEIFCOPY : False
print(npa_frombuffer.base is npa) # True