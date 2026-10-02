"""重生测试"""
import pytest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src.engine import EquipRebirthSystem, Equipment

class TestRebirth:
    def test_refund_all_materials(self):
        ers = EquipRebirthSystem()
        ers.equipment = {"e1": Equipment("e1","n",50,"epic",10,{"atk":100},["gem1"],True)}
        refund = ers.rebirth("e1")
        assert "gem" in str(refund).lower() or "affix" in str(refund).lower(), "只返还强化材料"

class TestBound:
    def test_bound_preserved(self):
        ers = EquipRebirthSystem()
        ers.equipment = {"e1": Equipment("e1","n",50,"epic",10,{},[],True)}
        ers.rebirth("e1")
        assert ers.equipment["e1"].bound == True, "重生清除绑定"
