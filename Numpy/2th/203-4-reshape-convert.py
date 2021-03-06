# 그외의 함수들
import numpy as np

# order F,C
a = np.arange(1, 61)

b = np.reshape(a, (5,4,3), order='C')
# print(b)
c = np.reshape(a, (5,4,3), order='F')
# print(c)

d = np.arange(1,101)
e = np.reshape(d, (10, 10), order='C')
# print(e)
# [[  1   2   3   4   5   6   7   8   9  10]
#  [ 11  12  13  14  15  16  17  18  19  20]
# (...)
#  [ 81  82  83  84  85  86  87  88  89  90]
#  [ 91  92  93  94  95  96  97  98  99 100]]

f = np.reshape(d, (10, 10), order='F')
# print(f)
# [[  1  11  21  31  41  51  61  71  81  91]
#  [  2  12  22  32  42  52  62  72  82  92]
# (...)
#  [  9  19  29  39  49  59  69  79  89  99]
#  [ 10  20  30  40  50  60  70  80  90 100]]


g = np.reshape(f, (10, 10), order='C')
# print(g) # f와 같음
h = np.reshape(f, (10, 10), order='F')
# print(h) # f와 같음

i = np.reshape(f, (5, 20), order='C')
print(i)
# [[  1  11  21  31  41  51  61  71  81  91   2  12  22  32  42  52  62  72  82  92]
#  [  3  13  23  33  43  53  63  73  83  93   4  14  24  34  44  54  64  74  84  94]
#  [  5  15  25  35  45  55  65  75  85  95   6  16  26  36  46  56  66  76  86  96]
#  [  7  17  27  37  47  57  67  77  87  97   8  18  28  38  48  58  68  78  88  98]
#  [  9  19  29  39  49  59  69  79  89  99  10  20  30  40  50  60  70  80  90 100]]

j = np.reshape(f, (5, 20), order='F')
print(j)
# [[  1   6  11  16  21  26  31  36  41  46  51  56  61  66  71  76  81  86  91  96]
#  [  2   7  12  17  22  27  32  37  42  47  52  57  62  67  72  77  82  87  92  97]
#  [  3   8  13  18  23  28  33  38  43  48  53  58  63  68  73  78  83  88  93  98]
#  [  4   9  14  19  24  29  34  39  44  49  54  59  64  69  74  79  84  89  94  99]
#  [  5  10  15  20  25  30  35  40  45  50  55  60  65  70  75  80  85  90  95 100]]