
import os
import hashlib
import json


path_s = 'tmp'
path_t = 'test2'
class version:
    def md5_check(self):
        path_sv = path_s + '/version'
        path_tv = path_t+'/version'
        with open(path_tv, 'rb') as f_s:
            data = f_s.read()
            self.t_md5 = hashlib.md5(data).hexdigest()
        f_s.close()
        with open(path_sv, 'rb') as f_s:
            data = f_s.read()
            self.s_md5 = hashlib.md5(data).hexdigest()
        f_s.close()
        if self.t_md5 == self.s_md5:
            return True
        else:
            return False
    def download(self,path):
        # 引用 requests文件
        import requests
        # 下载地址
        Download_addres = 'https://raw.githubusercontent.com/Guyue2926/py_update/master/versionn'
        # 把下载地址发送给requests模块
        f = requests.get(Download_addres)
        # 下载文件
        with open(path+'/version', "wb") as f_s:
            f_s.write(f.content)
            f_s.close()


    def update_v(self):
        self.download(path_s)
        if self.md5_check():
            pass
        else:
            self.download(path_t)


class check_file:
    path_tv = 'test2/version'
    with open(path_tv, 'rb') as f_s:
        data = f_s.read()
        list_file = set(json.loads(data)['md5_list'])
        f_s.close()
    def flie_list(self):
        self.list_t = []
        for filename in os.listdir(path_t):
            if filename != 'version':
                with open(path_t+'/'+filename, 'rb') as f_s:
                    data = f_s.read()
                    self.t_md5 = hashlib.md5(data).hexdigest()
                    f_s.close()
                self.list_t.append(self.t_md5)
        if self.list_file.issubset(self.list_t):
            return True
        else:
            return False
    #

ver = version()
ver.update_v()
# print(ver.md5_check())
check = check_file()
print(check.flie_list())
# # print(ver.md5_check())
