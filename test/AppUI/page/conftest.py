import os
import time

import pytest

def get_rootdir(request):
    rootdir = request.config.rootdir
    return rootdir

@pytest.fixture(scope="session",autouse=True)
def manage_logs(request):
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    log_name = 'logs/' + now + '.logs'
    request.config.pluginmanager.get_plugin("logging-plugin") \
        .set_log_path(os.path.join(get_rootdir(request), log_name))