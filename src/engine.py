"""装备重生 - 带8个bug"""
from dataclasses import dataclass, field

@dataclass
class Equipment:
    eid: str
    name: str
    level: int
    quality: str
    enhance_level: int
    affixes: dict
    gems: list
    bound: bool

class EquipRebirthSystem:
    def __init__(self):
        self.equipment: dict[str, Equipment] = {}
        self.last_rebirth = {}

    def rebirth(self, eid):
        eq = self.equipment[eid]
        # bug1: 只返还强化材料
        refund = {"enhance_stone": eq.enhance_level * 10}
        # bug2: 直接清零不是降到1级
        eq.level = 0
        eq.enhance_level = 0
        # bug3: 属性随机重新生成
        eq.affixes = {"new_stat": 100}
        # bug8: 清除绑定
        eq.bound = False
        return refund

    def get_cooldown(self, eid):
        # bug4: 无冷却
        return 0

    def batch_rebirth(self, eids):
        # bug5: 只返还第一件
        return self.rebirth(eids[0])

    def preview(self, eid):
        # bug6: 只显示返还材料不显示重生后属性
        eq = self.equipment[eid]
        return {"refund": {"enhance_stone": eq.enhance_level * 10}}

    def get_cost(self, eid):
        # bug7: 固定消耗
        return 100
