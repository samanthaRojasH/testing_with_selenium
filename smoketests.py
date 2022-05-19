from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from test_store import SearchTest
from register_new_user import RegisterNewUser

search_test = TestLoader().loadTestsFromTestCase(SearchTest)
new_user = TestLoader().loadTestsFromTestCase(RegisterNewUser)

smoke_test = TestSuite([search_test, new_user])

kwargs = {
    "output": 'smoke-report'
}

runner = HTMLTestRunner (**kwargs)
runner.run(smoke_test)
"""video 9"""