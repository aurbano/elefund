#!/usr/bin/env python3

from .positive_spread_recorder import PositiveSpreadRecorder
from unittest.mock import MagicMock

def test_whenNewSpreadAddedThenSpreadReturned():
    recorder = PositiveSpreadRecorder(MagicMock())

    recorder.record_spread('ABC', 123)

    assert recorder.get_positive_spreads() == {'ABC': 123}

def test_whenSpreadUpdatedWithPositiveValueThenUpdatedSpreadReturned():
    recorder = PositiveSpreadRecorder(MagicMock())

    recorder.record_spread('ABC', 123)
    recorder.record_spread('ABC', 224)

    assert recorder.get_positive_spreads() == {'ABC': 224}

def test_whenSpreadUpdatedWithNegativeValueThenSpreadRemoved():
    recorder = PositiveSpreadRecorder(MagicMock())

    recorder.record_spread('ABC', 123)
    recorder.record_spread('ABC', -1)

    assert recorder.get_positive_spreads() == {}
