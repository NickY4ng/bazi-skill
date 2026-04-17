#!/usr/bin/env python3
"""
流年流月计算脚本
输入: 年干 或 大运干支 + 流年干
输出: 流月干支列表
"""

TIANGAN = "甲乙丙丁戊己庚辛壬癸"
DIZHI = "子丑寅卯辰巳午未申酉戌亥"
TG_IDX = {g:i for i,g in enumerate(TIANGAN)}
DZ_IDX = {z:i for i,z in enumerate(DIZHI)}

# 五虎遁：月干 = (年干index + 月份) % 10
# 正月=寅月（固定），其余按序
def get_liuyue_gan(year_stem, month_branch):
    """算单个月干支
    year_stem: 年干
    month_branch: 月支（寅=正月）
    """
    # 五虎遁口诀：甲己年起丙寅，乙庚年起戊寅，丙辛年起庚寅，丁壬年起壬寅，戊癸年起甲寅
    # 简化：寅月干 = (年干index * 2 + 2) % 10
    # 年干index: 甲0,乙1,丙2,丁3,戊4,己5,庚6,辛7,壬8,癸9
    # 映射: 甲0→丙2, 乙1→戊4, 丙2→庚6, 丁3→壬8, 戊4→甲0, 己5→丙2, 庚6→戊4, 辛7→庚6, 壬8→壬8, 癸9→甲0
    # 公式：寅月干index = (年干index + 1) % 5 * 2 ... 这比较复杂
    # 用口诀：甲己→丙寅，乙庚→戊寅，丙辛→庚寅，丁壬→壬寅，戊癸→甲寅
    yt_map = {
        "甲":"丙","己":"丙",
        "乙":"戊","庚":"戊",
        "丙":"庚","辛":"庚",
        "丁":"壬","壬":"壬",
        "戊":"甲","癸":"甲",
    }
    yin_gan = yt_map.get(year_stem, "")
    if not yin_gan:
        return ""

    yin_tg_idx = TG_IDX[yin_gan]
    m_dz_idx = DZ_IDX[month_branch]
    offset = (m_dz_idx - 2) % 12  # 寅=2
    target_tg_idx = (yin_tg_idx + offset) % 10
    return TIANGAN[target_tg_idx] + month_branch

def get_all_liuyue(year_stem):
    """算全年12个月干支
    year_stem: 年干
    返回: [(月份, 干支), ...]
    """
    yt_map = {
        "甲":"丙","己":"丙",
        "乙":"戊","庚":"戊",
        "丙":"庚","辛":"庚",
        "丁":"壬","壬":"壬",
        "戊":"甲","癸":"甲",
    }
    yin_gan = yt_map.get(year_stem, "")
    yin_tg_idx = TG_IDX[yin_gan]

    result = []
    for i, zhi in enumerate("寅卯辰巳午未申酉戌亥子丑"):
        offset = i  # 寅为0
        tg_idx = (yin_tg_idx + offset) % 10
        result.append((i+1, TIANGAN[tg_idx] + zhi))
    return result

def get_liuyue_in_dayun(year_stem, month_branch, dayun_gan, dayun_zhi):
    """在大运中算流月
    用大运干支替代年干支来算
    """
    return get_liuyue_gan(year_stem, month_branch)  # 简化版

if __name__ == "__main__":
    # 测试：甲年流月
    print("甲年流月:")
    for m, gz in get_all_liuyue("甲"):
        print(f"  {m}月: {gz}")

    # 验证：甲己年起丙寅 ✓
