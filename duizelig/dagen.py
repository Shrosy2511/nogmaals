dag = input('type hier de dag ma/di/wo/do/vrij/za/zo ')
ma = 'maandag'
di = 'dinsdag'
wo = 'woensdag'
do = 'donderdag'
vrij = 'vrijdag'
za = 'zaterdag'
zo = 'zondag'

while dag == 'ma' or dag == 'maandag':
    print(ma)
    break

while dag == 'di' or dag == 'dinsdag':
    print(ma + ' ' + di)
    break

while dag == 'wo' or dag == 'woensdag':
    print(ma + ' ' + di + ' ' + wo)
    break

while dag == 'do' or dag == 'donderdag':
    print(ma + ' ' + di + ' ' + wo + ' ' + do)
    break

while dag == 'vrij' or dag == 'vrijdag':
    print(ma + ' ' + di + ' ' + wo + ' ' + do + ' ' + vrij)
    break

while dag == 'za' or dag == 'zaterdag':
    print(ma + ' ' + di + ' ' + wo + ' ' + do + ' ' + vrij + ' ' + za)
    break

while dag == 'zo' or dag == 'zondag':
    print(ma + ' ' + di + ' ' + wo + ' ' + do + ' ' + vrij + ' ' + za + ' ' + zo)
    break
