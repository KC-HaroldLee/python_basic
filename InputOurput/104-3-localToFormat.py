band = 'nirvana'
name = 'cobain'

print('{0[name]} in {0[band]}'.format(locals()))
print('{0[name]} in {0[band]}'.format(vars()))
print('{0[name]} in {0[band]}'.format(globals()))