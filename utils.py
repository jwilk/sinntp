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

import os
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

class xdg(object):

    '''
    Tiny replacement for xdg.BaseDirectory.
    '''

    xdg_data_home = os.environ.get('XDG_DATA_HOME') or os.path.join(os.path.expanduser('~'), '.local', 'share')

    @classmethod
    def save_data_path(xdg, resource):
        path = os.path.join(xdg.xdg_data_home, resource)
        try:
            os.makedirs(path, 0700)
        except OSError:
            if not os.path.isdir(path):
                raise
        return path

# vim:ts=4 sw=4 et
