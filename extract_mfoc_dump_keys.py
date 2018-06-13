### Script by J4S0N.H in CYCU
### 2018 / 06 / 13

import datetime as dt

key_file = input('[*] Please enter key file name: ')
if key_file == '':
    print('[!] Not enter any word, exiting program.')
    exit()
output_file = 'output_keys_' + dt.datetime.now().strftime('%Y%m%d') + '.txt'

offset_1 = 0x30
offset_2 = 0x04
try:
    with open(key_file, 'rb') as fin:
        with open(output_file, 'w') as fout:
            for i in range(16):
                fin.read(offset_1)
                key = fin.read(6)
                fout.write(key.hex() + '\n')
                fin.read(offset_2)
                key = fin.read(6)
                fout.write(key.hex() + '\n')
    print('[*] Extract successful, all keys saved to [' + output_file + ']')
except:
    print('[!] Something wrong, maybe you can check if the file is correct?')

