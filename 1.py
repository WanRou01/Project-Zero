# •	任務一：撰寫防呆 safe_division 函式
# o	請用 Python 寫一個 safe_division(a, b) 函式，能防止除以零，並將程式碼
# 上傳至 GitHub
def safe_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    return result
# 測試範例
print(safe_division(10, 2))  # 輸出: 5.0
print(safe_division(10, 0))  # 輸出: Error: Division by zero is not allowed.
# •	任務二：撰寫單元測試
import unittest
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