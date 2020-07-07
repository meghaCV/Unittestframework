import unittest
from Package1.TC1_Logintest import Logintest
from Package1.TC2_Signuptest import Signuptest
from Package2.Paymenttest import Paymenttest
from Package2.Paymentreturns import Paymentreturns

# Get all tests from Logintest,signup,paymenttest and payment returns
tc1 = unittest.TestLoader().loadTestsFromTestCase(Logintest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(Signuptest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(Paymenttest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(Paymentreturns)

# Creating test suite

sanitytestsuite = unittest.TestSuite([tc1, tc2])
# unittest.TextTestRunner().run(sanitytestsuite)

functionaltestsuite = unittest.TestSuite([tc3, tc4])
# unittest.TextTestRunner().run(functionaltestsuite)

mastertestsuite = unittest.TestSuite([tc1, tc2, tc4])

unittest.TextTestRunner(verbosity=2).run(mastertestsuite)
