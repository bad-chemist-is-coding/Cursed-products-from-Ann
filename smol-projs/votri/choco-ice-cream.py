import time

while True:
    var = input('Bạn có vô tri không? (nhập Y)\n')
    if var.lower().startswith('y'):
        break

while True:
    for i in range(1, 12):
        print('💩' * i)
        time.sleep(0.1)
    for k in range(12, 1, -1):
        print('💩' * k)
        time.sleep(0.1)

# import time
# while True:
#     var = input('Bạn có vô tri không?\n')
#     if var.lower().startswith('có'):
#         i = 0
#         while i<299:
#             print("💩")
#             time.sleep(0.1)
#             print("💩💩")
#             time.sleep(0.1)
#             print("💩💩💩")
#             time.sleep(0.1)
#             print("💩💩💩💩")
#             time.sleep(0.1)
#             print("💩💩💩💩💩")
#             time.sleep(0.1)
#             print("💩💩💩💩💩💩")
#             time.sleep(0.1)
#             print("💩💩💩💩💩💩💩")
#             time.sleep(0.1)
#             print("💩💩💩💩💩💩💩💩")
#             time.sleep(0.1)
#             print("💩💩💩💩💩💩💩💩💩")
#             time.sleep(0.1)
#             print("💩💩💩💩💩💩💩💩💩💩")
#             time.sleep(0.1)
#             print("💩💩💩💩💩💩💩💩💩💩💩")
#             time.sleep(0.1)
#             print("💩💩💩💩💩💩💩💩💩💩")
#             time.sleep(0.1)
#             print("💩💩💩💩💩💩💩💩💩")
#             time.sleep(0.1)
#             print("💩💩💩💩💩💩💩💩")
#             time.sleep(0.1)
#             print("💩💩💩💩💩💩💩")
#             time.sleep(0.1)
#             print("💩💩💩💩💩💩")
#             time.sleep(0.1)
#             print("💩💩💩💩💩")
#             time.sleep(0.1)
#             print("💩💩💩💩")
#             time.sleep(0.1)
#             print("💩💩💩")
#             time.sleep(0.1)
#             print("💩💩")
#             time.sleep(0.1)
#             print("💩")
#             time.sleep(0.1)
#
#             i+=1
#
#         break

