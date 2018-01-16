from .fee import Fee
from .calculator import Calculator
from state import fee_store


def get_fee(from_currency, to_currency, exchange, amount):
  if from_currency == to_currency:
    return fee_store[from_currency].fastest
  # TODO implement exchange fees
  return 0