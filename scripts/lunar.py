#!/usr/bin/env python3
"""
阴历/阳历互转脚本
使用 lunardate 库（pip install lunardate）
用法：
  lunar_to_solar(year, month, day, is_leap=False) → datetime.date
  solar_to_lunar(year, month, day) → (year, month, day, is_leap)
"""

from lunardate import LunarDate


def lunar_to_solar(year, month, day, is_leap=False):
    """
    阴历转阳历
    year: 阴历年
    month: 阴历月
    day: 阴历日
    is_leap: 是否闰月
    返回: datetime.date
    """
    try:
        ld = LunarDate(year, month, day, is_leap)
        return ld.toSolarDate()
    except ValueError as e:
        raise ValueError(f"阴历日期无效: {year}-{month}-{day}, 闰月={is_leap}") from e


def solar_to_lunar(year, month, day):
    """
    阳历转阴历
    返回: (year, month, day, is_leap)
    """
    try:
        ld = LunarDate.fromSolarDate(year, month, day)
        return ld.year, ld.month, ld.day, ld.isLeapMonth
    except ValueError as e:
        raise ValueError(f"阳历日期无效: {year}-{month}-{day}") from e


def is_lunar_date(year, month, day):
    """
    启发式判断输入是阴历还是阳历（由调用方根据语义判断更可靠）
    """
    pass


if __name__ == "__main__":
    # 测试
    tests = [
        (1989, 9, 24, "阴历九月廿四"),
        (1995, 6, 12, "阴历六月十二"),
        (1989, 8, 2, "阴历八月初二"),
        (1993, 8, 24, "阴历八月廿四"),
    ]
    for y, m, d, desc in tests:
        solar = lunar_to_solar(y, m, d)
        print(f"{desc} → 阳历 {solar}")
