# Copyright © 2008-2015
#   Piotr Lewandowski <piotr.lewandowski@gmail.com>,
#   Jakub Wilk <jwilk@jwilk.net>.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License, version 2, as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

from __future__ import print_function

def debug(*args, **kwargs):
    print('debug(*%r, **%r)' % (args, kwargs))

def strip_headers(headers='To,Cc,Bcc', message=None):
    headers = headers.split(',')
    for header in headers:
        del message[header]
    return message

def mimify(type='text/plain', charset='US-ASCII', message=None):
    if 'Content-Type' not in message:
        message['Content-Type'] = '{tp}; charset={cs}'.format(tp=type, cs=charset)
    return message

__all__ = [
    'debug',
    'mimify',
    'strip_headers',
]

# vim:ts=4 sts=4 sw=4 et
