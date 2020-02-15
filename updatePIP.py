#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
以PIP方式更新LIB库
"""

import pip
from subprocess import call
from pip._internal.utils.misc import get_installed_distributions
import os

counter = 0

for dist in get_installed_distributions():
    counter = counter + 1

    print(
        str(counter) + ". " + dist.project_name + "\t", dist.version + "\t",
        dist.location)
    if dist.project_name != "pip":
        #call("pip show " + dist.project_name, shell=True)
        call("pip install --upgrade " + dist.project_name, shell=True)
