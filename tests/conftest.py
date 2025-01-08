import sys
import os

# Add the root directory to the PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from framework.base_driver import BaseDriver

import pytest

@pytest.fixture
def driver():
    driver = BaseDriver.get_driver()
    yield driver
    driver.quit()
