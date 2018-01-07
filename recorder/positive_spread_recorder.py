#!/usr/bin/env python3

class PositiveSpreadRecorder(object):
    """A spread recorder that only persists positive spreads"""

    def __init__(self, history_store):
        self._positive_spreads = {}
        self._history_store = history_store

    def record_spread(self, strategy_id, spread_amount):
        self._history_store.record(strategy_id, spread_amount)
        if spread_amount < 0:
            self._remove_negative_spread_if_exists(strategy_id)
        else:
            self._add_or_update_positive_spread(strategy_id, spread_amount)

    def get_positive_spreads(self):
        return self._positive_spreads

    def _add_or_update_positive_spread(self, strategy_id, spread_amount):
        self._positive_spreads[strategy_id] = spread_amount

    def _remove_negative_spread_if_exists(self, strategy_id):
        self._positive_spreads.pop(strategy_id, None)

