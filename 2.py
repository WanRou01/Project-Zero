# 任務二：讓 Copilot 生成單元測試，並貼上測試程式碼
# 請用 Copilot 或其他工具自動產生 safe_division 的單元測試，並將程式碼
# 上傳至 GitHub
import unittest
def safe_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    return result
class TestSafeDivision(unittest.TestCase):
    def test_normal_division(self):
        self.assertEqual(safe_division(10, 2), 5.0)
        self.assertEqual(safe_division(-10, 2), -5.0)
        self.assertEqual(safe_division(10, -2), -5.0)
        self.assertEqual(safe_division(-10, -2), 5.0)

    def test_division_by_zero(self):
        self.assertEqual(safe_division(10, 0), "Error: Division by zero is not allowed.")
        self.assertEqual(safe_division(0, 0), "Error: Division by zero is not allowed.")
if __name__ == '__main__':
    unittest.main()