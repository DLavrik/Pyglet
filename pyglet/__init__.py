#!/usr/bin/env python
# ----------------------------------------------------------------------------
# pyglet
# Copyright (c) 2006-2007 Alex Holkner
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions 
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright 
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of the pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

'''pyglet is a cross-platform games and multimedia package.

Detailed documentation is available at http://www.pyglet.org
'''

__docformat__ = 'restructuredtext'
__version__ = '$Id$'

def _require_ctypes_version(version):
    # Check ctypes version
    import ctypes
    req = [int(i) for i in version.split('.')]
    have = [int(i) for i in ctypes.__version__.split('.')]
    if not tuple(have) >= tuple(req):
        raise ImportError('pyglet requires ctypes %s or later.' % version)
_require_ctypes_version('1.0.0')

#: Global dict of pyglet options.  To change an option from its default, you
#: must import `pyglet` before any sub-packages.  For example::
#:
#:      import pyglet
#:      pyglet.options['gl_error_check'] = False
#:
#: The options are:
#:
#: gl_error_check
#:     If True, all calls to OpenGL functions are checked afterwards for
#:     errors using ``glGetError``.  This will severely impact performance,
#:     but provides useful exceptions at the point of failure.  By default,
#:     this option is enabled if ``__debug__`` is (i.e., if Python was not run
#:     with the -O option.
#:
options = {
    'gl_error_check': __debug__,
}
