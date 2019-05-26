import hashlib


def md5_encoding(string):
    md5 = hashlib.md5()
    md5.update(string.encode(encoding="utf-8"))
    return md5.hexdigest()[8:-8]


if __name__ == '__main__':
    print(md5_encoding("123456"))
