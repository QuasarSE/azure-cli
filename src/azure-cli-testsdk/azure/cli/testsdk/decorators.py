# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest
from azure.cli.core.profiles import supported_api_version
from .const import ENV_LIVE_TEST


def live_only():
    return unittest.skipUnless(
        os.environ.get(ENV_LIVE_TEST, False),
        'This is a live only test. A live test will bypass all vcrpy components.')


def record_only():
    return unittest.skipUnless(
        not os.environ.get(ENV_LIVE_TEST, False),
        'This test is excluded from being run live. To force a recording, please remove the recording file.')


def api_version_constraint(resource_type, **kwargs):
    return unittest.skipUnless(supported_api_version(resource_type, **kwargs),
                               "Test not supported by current profile.")
