import os
import sys
from PIL import Image, ImageDraw
import string 

# http://sayakhov.ru/blog/post/14/
# http://habrahabr.ru/sandbox/59849/

catalog1 = str(sys.argv[0][0:len(sys.argv[0])-13])
catalog = ''
a = 0
while a < len(catalog1):
 if catalog1[a] == '\\':
  catalog = catalog + '/'
 else:
  catalog = catalog + catalog1[a]
 a = a + 1

print(catalog + '\n')
find_files = []
for root, dirs, files in os.walk(catalog):
 find_files += [os.path.join(root, name) for name in files ]

result_file = open('log.txt', 'w')
detalied_log = open('log_allfiles.txt', 'w')

result_file.write('root folder: ' + catalog + '\n')
detalied_log.write('root folder: ' + catalog + '\n')
detalied_log.write('total files: ' + str(len(find_files))+ '\n')

print('total files: ' + str(len(find_files)))
k = 0
sx = 0
sy = 0
counter_files = 0
for cur_file in find_files:
 now_ext = cur_file[len(cur_file)-4:len(cur_file)]
 if str.lower(now_ext) == '.jpg' or\
    str.lower(now_ext) == 'jpeg' or\
    str.lower(now_ext) == '.png' or\
    str.lower(now_ext) == '.jpe':
  img = Image.open(cur_file)
  size = img.size
  if size[0] in range(0,32): sx = 32
  if size[0] in range(33,64): sx = 64
  if size[0] in range(65,128): sx = 128
  if size[0] in range(129,256): sx = 256
  if size[0] in range(257,512): sx = 512
  if size[0] in range(513,1024): sx = 1024
  if size[0] in range(1025,2048): sx = 2048
  if size[1] in range(0,32): sy = 32
  if size[1] in range(33,64): sy = 64
  if size[1] in range(65,128): sy = 128
  if size[1] in range(129,256): sy = 256
  if size[1] in range(257,512): sy = 512
  if size[1] in range(513,1024): sy = 1024
  if size[1] in range(1025,2048): sy = 2048
  if sx * sy > 1024 * 1024:
   print(cur_file + ' ' + str(size[0]) + 'x' + str(size[1]) + ' result size: ' + str(sx) + 'x' + str(sy) + '\n')
   result_file.write(cur_file + ' ' + str(size[0]) + 'x' + str(size[1]) + ' result size: ' + str(sx) + 'x' + str(sy) + '\n')
   k = k + 1
  counter_files = counter_files +1
  detalied_log.write('file N' + str(counter_files) + ' ' + str(cur_file) + ' size:' + str(size[0]) + 'x' + str(size[1]) + ' result size: ' + str(sx) + 'x' + str(sy) + '\n' )
print(k)
result_file.write('\n')
result_file.write('found files: ' + str(k))
result_file.close()