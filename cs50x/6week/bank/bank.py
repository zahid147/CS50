import cs50

x = cs50.get_string("Greeting: ");

if 'Hello' in x:
    print('$' + '0')
    exit()
if 'H' in x:
    print('$' + '20')
else:
    print('$' + '100')