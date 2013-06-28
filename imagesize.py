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

result_file.write('root folder: ' + catalog + '\n')

print('total files: ' + str(len(find_files)))
k = 0
for cur_file in find_files:
 now_ext = cur_file[len(cur_file)-4:len(cur_file)]
 if str.lower(now_ext) == '.jpg' or\
    str.lower(now_ext) == 'jpeg' or\
    str.lower(now_ext) == '.png' or\
    str.lower(now_ext) == '.jpe':
  img = Image.open(cur_file)
  size = img.size
  if size[0] * size[1] > 1024 * 1024:
   print(cur_file + ' ' + str(size[0]) + 'x' + str(size[1]) + '\n')
   result_file.write(cur_file + ' ' + str(size[0]) + 'x' + str(size[1]) + '\n')
   k = k + 1
print(k)
result_file.write('\n')
result_file.write('found files: ' + str(k))
