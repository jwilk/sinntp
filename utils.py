# encoding=UTF-8

# Copyright © 2011
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

import re

_split_host_re = re.compile(
    r'^ (?: \[ ( [^\[\]]+ ) \] | ( [^:]+ ) | ( .* ) ) (?: : ([0-9]+) )? $',
    re.VERBOSE
)

def split_host(host, default_port=None):
    match = _split_host_re.match(host)
    assert match is not None
    host1, host2, host3, port = match.groups()
    host = host1 or host2 or host3
    if port is None:
        port = default_port
    else:
        port = int(port)
    return host, port

# vim:ts=4 sw=4 et
