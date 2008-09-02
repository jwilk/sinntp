def debug(*args, **kwargs):
    print 'debug(*%r, **%r)' % (args, kwargs)

def strip_headers(headers = 'To,Cc,Bcc', message = None):
    headers = headers.split(',')
    for header in headers:
        del message[header]
    return message

def mimify(type = 'text/plain', charset = 'US-ASCII', message = None):
    if 'Content-Type' not in message:
        message['Content-Type'] = '%(type)s; charset=%(charset)s' % locals()
    return message

# vim:ts=4 sw=4 et
