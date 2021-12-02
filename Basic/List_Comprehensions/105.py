l1 = ['nirvana','offspring','nofx','tool','ataris','greenday']
l2 = ['starcraft','portal','bioshock','sonic','comandos','left4dead']

# print([i for i in l1, l2 if len(i)<7])
print([i for i in l1 if len(i)<7 for i in l2 if len(i)<7])
