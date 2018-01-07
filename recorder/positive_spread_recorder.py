#!/usr/bin/env python3

class PositiveSpreadRecorder(object):
    """A spread recorder that only persists positive spreads"""

    def __init__(self):
        self._positive_spreads = {}

    def record_spread(self, id, spread_amount):
        if spread_amount < 0:
            self._remove_negative_spread_if_exists(id)
        else:
            self._add_or_update_positive_spread(id, spread_amount)

    def get_positive_spreads(self):
        return self._positive_spreads

    def _add_or_update_positive_spread(self, id, spread_amount):
        self._positive_spreads[id] = spread_amount

    def _remove_negative_spread_if_exists(self, id):
        self._positive_spreads.pop(id, None)