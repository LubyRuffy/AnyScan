#!/usr/bin/env python
import urlparse
def assign(service, arg):
    if service != "www":
        return
    arr = urlparse.urlparse(arg)
    return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
    url = arg
    code, head, res, errcode, _ = curl.curl(url + '%2F*~1.*%2Fx.aspx')
    if code == 404:
        code, head, res, errcode, _ = curl.curl(url + '%2Fooxx*~1.*%2Fx.aspx')
        if code == 400:
            security_info(url)

            return arg
if __name__== '__main__':
    from dummy import *
