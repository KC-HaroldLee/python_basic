numbers = [5,4,3,2,1]
print('{numbers}'.format(**locals()))
print('{numbers[1]}'.format(**locals()))
print('{numbers}'.format(**vars()))
print('{numbers[0]}'.format(**vars()))