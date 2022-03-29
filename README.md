# dumpweb

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ee30871b802845469b95bbdb139797fb)](https://app.codacy.com/gh/0x07CB/dumpweb?utm_source=github.com&utm_medium=referral&utm_content=0x07CB/dumpweb&utm_campaign=Badge_Grade_Settings)

_for dump an static website_

## to install

```
git clone https://github.com/0x07CB/dumpweb.git
cd dumpweb/
./install.sh
```

_the location of this script is at `/usr/bin/` with the name `dumpweb`_ 


## force re-install

```
./install.sh -f
```


## show the help

```
dumpweb -h
```

_and see that_

```
usage: dumpweb [-h] webpath

positional arguments:
  webpath     full web adress and path(exemple:
              https://www.mywebsite.com/index.html)

optional arguments:
  -h, --help  show this help message and exit
```


## to use

exemple

```
dumpweb www.website.com
```
_that create an folder, inside all the stuff have been dump (if static)_
