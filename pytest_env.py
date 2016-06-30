# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import platform

class Environment:

    def __init__(self, platform, python_version):
        self.platform = platform
        self.python_version = python_version
        self.env_all_var = [platform, python_version]

env_var = Environment (
                       platform = platform.platform(),
                       python_version = platform.python_version()
                      )

@pytest.fixture(scope='session', autouse=True)
def environment():
    request.config._environment.extend([
        ('Python', env_var.python_version()),
        ('Platform', env_var.platform())])
    return env_var
