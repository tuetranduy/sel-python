import argparse
import pytest

from dotenv import load_dotenv



def pytest_addoption(parser):
    parser.addoption("--browser", action="store",
                     help="Browser Type. Default is chrome",
                     metavar="")
    parser.addoption("--test-env", action="store",
                     help="Test environment. Default is qa",
                     metavar="")
    parser.addoption("--args", action="store",
                     help="Custom arguments",
                     metavar="")

def pytest_configure(config):
    pytest.browser = config.getoption("--browser", "chrome", True)
    pytest.test_env = config.getoption("--test-env", "qa", True)
    pytest.args = config.getoption("--args", "", True)


@pytest.fixture(scope='session', autouse=True)
def load_env_infor():
    load_dotenv()
