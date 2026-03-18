"""Tests for AiEthicsSimulator."""
from src.core import AiEthicsSimulator
def test_init(): assert AiEthicsSimulator().get_stats()["ops"] == 0
def test_op(): c = AiEthicsSimulator(); c.analyze(x=1); assert c.get_stats()["ops"] == 1
def test_multi(): c = AiEthicsSimulator(); [c.analyze() for _ in range(5)]; assert c.get_stats()["ops"] == 5
def test_reset(): c = AiEthicsSimulator(); c.analyze(); c.reset(); assert c.get_stats()["ops"] == 0
def test_service_name(): c = AiEthicsSimulator(); r = c.analyze(); assert r["service"] == "ai-ethics-simulator"
