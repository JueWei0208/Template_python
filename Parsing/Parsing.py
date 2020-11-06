# -*- coding=utf-8-*-
from Crypto.Cipher import DES
import base64
class DESUtil:
    __BLOCK_SIZE_8 = BLOCK_SIZE_8 = DES.block_size
    @staticmethod
    def encryt(str, key):
        cipher = DES.new(key, DES.MODE_CBC,key)
        x = DESUtil.__BLOCK_SIZE_8 - (len(str) % DESUtil.__BLOCK_SIZE_8)
        if x != 0:
            str = str + chr(x)*x
        msg = cipher.encrypt(str)
        msg = base64.b64encode(msg)
        return msg
    @staticmethod
    def decrypt(enStr, key):
        cipher = DES.new(key, DES.MODE_CBC,key)
        decryptByts = base64.b64decode(enStr)
        msg = cipher.decrypt(decryptByts)
        paddingLen = ord(msg[len(msg)-1])
        return msg[0:-paddingLen]

#案例解析
if __name__ == "__main__":
    key = "12345678"
    res = DESUtil.encryt("hongtao", key)
    print (res)
