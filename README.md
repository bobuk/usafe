# usafe
μSafe - oversimplistic secret data storage with cryptography protection

This package contains an `usafe` module and `usafe-a` script.
First one is needed to prepare password protected archive file with all the files what you need to use in your application.
All this files must be relatively small because it will be loaded in memory.

```bash
$ usafe-a privkey.pem id_rsa.key
Password: <input your password>
File privkey.pem writen (1441)
File id_rsa.key writen (1549)
... file `secret` writen
```

As you can see usafe-a got a list of files which needs to be prepared and save an archive to file `secret`.

```python
>>> from usafe import uSafe
>>> dt = uSafe('secret')
Password: <input your password>
>>> dt['privkey.pem'].decode().split('\n')[0]
-----BEGIN CERTIFICATE-----
```

So there's only one class `uSafe`, contructor have two parameters: `path=` with default 'secret' - filename of file with data, `passwd=` - use password to decode data or ask password in console. Object of this class can be used as `dict` with data from source filenames.

Warning: be very carefull, this is not real protection for highly private data, because all this data will be accessable in memory.