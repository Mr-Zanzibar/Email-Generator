import random
import time


print("""
Cuda Generator :)
""")

chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
r = random.choice


domain = input("Choose a domain:") # if you don't put anything it will generate it automatically
howmuch = int(input("How many emails do you want to generate? "))

print("Generating...")
time.sleep(1)

if domain == '':
    domains = ['outlook.com', 'gmail.com', 'yandex.com', 'yahoo.com', 'pm.me', 'protonmail.com', 'coolmail.com', 'mail.com', 'sexymail.com', 'email.com', 'mymail.com', 'thisismyemail.com', 'freshmail.com', 'coolmail.com', 'easymail.com', 'freemail.com']

    for i in range(howmuch):
        first = ''.join((random.choice(chars) for i in range (4)))
        second = ''.join((random.choice(chars) for i in range (4)))
        third = ''.join((random.choice(chars) for i in range (4)))
        result = first + second + third + '@' + random.choice(domains)
        print(result)
else:
    for i in range(howmuch):
        first = ''.join((random.choice(chars) for i in range (4)))
        second = ''.join((random.choice(chars) for i in range (4)))
        third = ''.join((random.choice(chars) for i in range (4)))
        result = first + second + third + '@' + domain
        print(result)
