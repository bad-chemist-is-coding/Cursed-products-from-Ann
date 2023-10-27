import time

while True:
    var = input('Bạn có thích ai không?\n')
    if var.lower().startswith('có'):
        break

while True:
    for i in range (1,11):
        print('SIMP!' * i)
        time.sleep(0.5)
    for k in range (12, 1, -1):
        print('SIMP!' * k)
        time.sleep(0.5)


