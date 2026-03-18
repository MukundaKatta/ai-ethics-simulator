"""Tests for EthicsSimulator."""
import pytest
from src.ethicssimulator import EthicsSimulator

def test_init():
    obj = EthicsSimulator()
    stats = obj.get_stats()
    assert stats["total_ops"] == 0

def test_operation():
    obj = EthicsSimulator()
    result = obj.load_scenario(input="test")
    assert result["processed"] is True
    assert result["operation"] == "load_scenario"

def test_multiple_ops():
    obj = EthicsSimulator()
    for m in ['load_scenario', 'present_choice', 'evaluate_decision']:
        getattr(obj, m)(data="test")
    assert obj.get_stats()["total_ops"] == 3

def test_caching():
    obj = EthicsSimulator()
    r1 = obj.load_scenario(key="same")
    r2 = obj.load_scenario(key="same")
    assert r2.get("cached") is True

def test_reset():
    obj = EthicsSimulator()
    obj.load_scenario()
    obj.reset()
    assert obj.get_stats()["total_ops"] == 0

def test_stats():
    obj = EthicsSimulator()
    obj.load_scenario(x=1)
    obj.present_choice(y=2)
    stats = obj.get_stats()
    assert stats["total_ops"] == 2
    assert "ops_by_type" in stats
