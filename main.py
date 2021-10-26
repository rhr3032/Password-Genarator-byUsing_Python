import random

caracteres = 'sadfjh@hksjf#hkgjdf//asdfjh#@!gjszdf#@3ndjs998!@#ghdks'
length = 12
password = "".join(random.sample(caracteres, length))

print('John: '+ password)