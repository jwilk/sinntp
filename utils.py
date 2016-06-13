# encoding=UTF-8

# Copyright © 2011-2016
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

import itertools
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
    tiny replacement for PyXDG's xdg.BaseDirectory
    '''

    xdg_data_home = os.environ.get('XDG_DATA_HOME') or ''
    if not os.path.isabs(xdg_data_home):
        # “All paths […] must be absolute. If an implementation encounters a
        # relative path […] it should consider the path invalid and ignore it.
        #
        # […]
        #
        # If $XDG_DATA_HOME is either not set or empty, a default equal to
        # $HOME/.local/share should be used.”
        #
        # (XDG Base Directory Specification 0.8)
        xdg_data_home = os.path.join(os.path.expanduser('~'), '.local', 'share')

    @classmethod
    def save_data_path(xdg, resource):
        path = os.path.join(xdg.xdg_data_home, resource)
        try:
            os.makedirs(path, 0o700)
        except OSError:
            if not os.path.isdir(path):
                raise
        return path

def join_lines(lst):
    r'''
    join the list of lines;
    ensure there's trailing \n at the end
    '''
    if not lst:
        return '\n'
    if lst[-1].endswith('\n'):
        itr = iter(lst)
    else:
        itr = itertools.chain(lst, [''])
    return '\n'.join(itr)

__all__ = [
    'join_lines',
    'split_host',
    'xdg',
]

# vim:ts=4 sts=4 sw=4 et
