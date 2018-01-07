#!/usr/bin/env python3

import sqlite3
import time

class Store(object):

    def __init__(self):
        self._db = sqlite3.connect('elefund.db')
        self._db.execute('''CREATE TABLE IF NOT EXISTS spread_history( \
          strategy_id TEXT,
          timestamp INTEGER,
          spread_amount REAL)''')

    def record(self, strategy_id, spread_amount):
        insert_data = (strategy_id, time.time(), spread_amount)
        self._db.execute('''INSERT INTO spread_history(strategy_id, timestamp, spread_amount)
                         VALUES (?, ?, ?)
                         ''', insert_data)
