import os

path = 'data'
with open('faces.csv', 'w') as f:
    for filename in sorted(os.listdir(path)):
        if filename.endswith('.pgm'):
            f.write(f'{filename};0\n')