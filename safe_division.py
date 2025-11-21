"""
safe_division.py

提供 safe_division(a, b) 函式：當除數為 0 時回傳 None；輸入非數值型態則丟出 TypeError。
"""
from typing import Optional, Union
import numbers

Number = Union[int, float]

def safe_division(a: Number, b: Number) -> Optional[float]:
    """
    將 a 除以 b，若 b 為 0 則回傳 None。
    參數:
        a: 被除數（支援數字類型）
        b: 除數（支援數字類型）
    回傳:
        float 結果，或在 b == 0 時回傳 None
    例外:
        TypeError: 當 a 或 b 不是數值型態時
    """
    # 型別檢查：接受任何符合 numbers.Number 的數值類型（int, float, Decimal, Fraction 等）
    if not isinstance(a, numbers.Number) or not isinstance(b, numbers.Number):
        raise TypeError("safe_division expects numeric types for a and b")
    # 檢查除以零
    if b == 0:
        return None
    return float(a / b)


if __name__ == "__main__":
    # 簡單自我檢查
    assert safe_division(10, 2) == 5.0
    assert safe_division(3, 2) == 1.5
    assert safe_division(5, 0) is None
    try:
        safe_division("10", 2)
    except TypeError:
        pass
    else:
        raise AssertionError("Type checking failed")
    print("safe_division.py: quick checks passed")
