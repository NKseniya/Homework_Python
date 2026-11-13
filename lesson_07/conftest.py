import sys
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager

sys.path.insert(0, str(Path(__file__).parent))


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    service = webdriver.ChromeService(ChromeDriverManager().install())
    d = webdriver.Chrome(service=service, options=options)
    d.maximize_window()
    yield d
    d.quit()


@pytest.fixture
def firefox_driver():
    options = FirefoxOptions()
    service = webdriver.FirefoxService(GeckoDriverManager().install())
    d = webdriver.Firefox(service=service, options=options)
    yield d
    d.quit()
