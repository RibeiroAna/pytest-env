# -*- coding: utf-8 -*-

import pytest
import platform

def pytest_addoption(parser):
    group = parser.getgroup('env')
    group.addoption(
        '--env',
        action='store_true',
        help='get the env data'
    )


class Environment:

    def __init__(self, platform, python_version=None, pytest_version=None,
                 py_version=None, pluggy_version=None, root_dir=None,
                 ini_file=None, plugins=None):
        self.platform = platform
        self.python_version = python_version
        self.pluggy_version = pluggy_version
        self.root_dir = root_dir
        self.ini_file = ini_file
        self.plugins = plugins

    def __str__(self):
        str = "Environment details: "
        str += "platform={0} ".format(self.platform)
        str += "python_version={0} ".format(self.python_version)
        str += "pluggy_version={0} ".format(self.pluggy_version)
        str += "root_dir={0} ".format(self.root_dir)
        str += "ini_file={0} ".format(self.ini_file)
        str += "pluggins={0} ".format(self.plugins)
        return str

environment = Environment (
                            platform = platform.platform(),
                            python_version = platform.python_version()
                          )

@pytest.fixture()
def get_environment():
    return environment

def pytest_terminal_summary(terminalreporter):
        terminalreporter.write_sep('-', environment.__str__())
