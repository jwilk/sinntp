# Copyright © 2008-2009 Piotr Lewandowski <piotr.lewandowski@gmail.com>
# Copyright © 2008-2022 Jakub Wilk <jwilk@jwilk.net>
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License, version 2, as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

def debug(*args, **kwargs):
    print(f'debug(*{args!r}, **{kwargs!r})')

def strip_headers(headers='To,Cc,Bcc', message=None):
    headers = headers.split(',')
    for header in headers:
        del message[header]
    return message

def mimify(type='text/plain', charset='US-ASCII', message=None):
    if 'Content-Type' not in message:
        message['Content-Type'] = f'{type}; charset={charset}'
    return message

__all__ = [
    'debug',
    'mimify',
    'strip_headers',
]

# vim:ts=4 sts=4 sw=4 et
