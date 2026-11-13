import sys
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

sys.path.insert(0, str(Path(__file__).parent))


@pytest.fixture
def driver():
    """Фикстура с драйвером Chrome.

    Yields:
        WebDriver: экземпляр браузера Chrome в развёрнутом окне.
    """
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
    """Фикстура с драйвером Firefox.

    Yields:
        WebDriver: экземпляр браузера Firefox.
    """
    service = webdriver.FirefoxService(GeckoDriverManager().install())
    d = webdriver.Firefox(service=service)
    d.maximize_window()
    yield d
    d.quit()
