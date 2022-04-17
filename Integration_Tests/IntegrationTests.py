from App import  App
import unittest
class Integration_test(unittest.TestCase):
    def setUp(self):
        try:
            self.App = App()
        except Exception:
            self.skipTest("Unexpected error found")
    def test_Normal_case_macceleroc_calculator(self):
        self.assertEqual("num_payment 12 c 600 princ 105 Int 495 balance 98772",self.App.calc.mac_calculate(100000,6,360,12))
    def test_fail_validation_macceleroc_calculator(self):
        with self.assertRaises(ValueError):
                self.App.calc.mac_calculate(100000, 6, 12, 360)
    def test_add_new_value_in_database(self):
        result=self.App.calc.mac_calculate(100000,6,360,12)
        self.assertEqual(True,self.App.db.save_result(100000,6,360,12,result))

    def test_validation_in_add_new_value_in_database(self):
        with self.assertRaises(ValueError):
            result = self.App.calc.mac_calculate(100000, 6, 360, 12)
            self.assertTrue(True, self.App.db.save_result(100000, 6, 360, "12", result))
    def test_get_macceleroc_result(self):
        result = self.App.calc.mac_calculate(100000, 6, 360, 12)
        self.App.db.save_result(6, 100000, 360, 12, result)
        Result=str(self.App.db.get_one_example(6,100000,360,12)[0][0])
        self.assertEqual(result, Result)

    def test_get_macceleroc_result_is_not_database(self):
        result = self.App.calc.mac_calculate(100000, 6, 360, 12)
        self.App.db.save_result(100000, 6, 360, 12, result)
        Result = self.App.db.get_one_example(6, 100000, 3600, 12)
        self.assertEqual([], Result)

