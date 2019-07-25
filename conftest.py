import pytest



@pytest.fixture(params=["chrome"],scope="class")
def driver_init(request):
    from selenium import webdriver
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path='../ENV/chromedriver')
    if request.param == "firefox":
        web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    yield
    web_driver.close()
