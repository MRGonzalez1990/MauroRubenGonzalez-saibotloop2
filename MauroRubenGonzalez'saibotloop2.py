adult=['18','19','20','21']
while True:
    age=input('What is your age?')
    while int(age) == int(age):
        if int(age)>=18:
            print('Good.')
            break
        elif int(age)<=18:
            print('Underaged.')
            break
        elif age =='end':
            break
        else:
            continue
    real_age=input('What is your real age?')
    print (real_age)
    name=input('What is your name?')
    print (name)
