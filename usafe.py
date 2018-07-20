import getpass
import privy
import tarfile
import io, os


class uSafe:
    def __init__(self, path='secret', passwd=None):
        if not passwd: passwd = getpass.getpass()
        self.content = self.reader(path, passwd)
        del passwd

    def reader(self, path, passwd):
        res = {}
        tar = tarfile.open("secret", 'r:*', fileobj=open(path, 'rb'))
        for member in tar.getnames():
            res[member] = privy.peek(tar.extractfile(member).read(), passwd)
        return res

    def __getattr__(self, key):
        return self.content[key]
    def __getitem__(self, key):
        return self.content[key]
    
def create_safe(filelist, passwd=None, cb = None):
    if not passwd: passwd = getpass.getpass()
    tar = tarfile.open("secret", "w:")
    for file in filelist:
        content = open(file, 'rb').read()
        secure = privy.hide(content, passwd).encode()
        bt = io.BytesIO()
        bt.write(secure); bt.seek(0)

        info = tarfile.TarInfo(name=os.path.basename(file))
        info.size = len(secure)
        tar.addfile(info, fileobj=bt)
        if cb:
            cb(info)
    tar.close()

def main():
    create_safe(['misc/apns-dev-cert.pem', 'misc/apns-prod-cert.pem'])
    #a = uSafe('secret')
    #print(a.content)

if __name__ == '__main__':
    main()