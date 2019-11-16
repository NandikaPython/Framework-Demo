from FrameworkDemo import Login
import pytest
from selenium import webdriver

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class TestClassDemo():

    @pytest.fixture(autouse=True)
    def classSetUp(self):
        self.log_in=Login()
        print("class level set up of PyPi org")
        yield
        print("Logging out of Pypi org")

        def test_tc123_verify_login(self):

            assert self.log_in.Login_to_account()
            assert self.log_in.verify_login()
