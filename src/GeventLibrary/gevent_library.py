# Copyright (c) 2022 Eldad Uzman

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import absolute_import
from typing import Any, List

from robotlibcore import DynamicCore  # type: ignore

from .keywords import KW_MAPPING, GeventKeywords


class GeventLibrary(DynamicCore):
    """
    Gevent library enables testers to run a bundle of keywords as coroutines.
    Each keywords gets its own greenlet so that they are executed to completion.
    """

    libraries: List[Any] = [GeventKeywords()]
    ROBOT_LIBRARY_SCOPE = "TEST SUITE"
    ROBOT_LISTENER_API_VERSION = 3

    def __init__(self):
        self.ROBOT_LIBRARY_LISTENER = self
        DynamicCore.__init__(self, GeventLibrary.libraries)

    def start_keyword(self, name, attrs):
        if name.lower() in KW_MAPPING:
            new_kw = KW_MAPPING[name.lower()]
            print(f"replace {name} with {new_kw}")
