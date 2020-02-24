import os
import hashlib
import json

path_s = 'test1'
ver = {}
ver['version'] = '1.0'
md5_list = []
for filename in os.listdir(path_s):
    if filename != 'version':
        filename = path_s+'/'+filename
        with open(filename, 'rb') as f_s:
            data = f_s.read()
            t_md5 = hashlib.md5(data).hexdigest()
            f_s.close()
            md5_list.append(t_md5)
ver['md5_list'] = md5_list
with open(path_s+'/version', 'wb') as f_s:
    f_s.write(json.dumps(ver).encode())
    print(json.dumps(ver))
    f_s.close()