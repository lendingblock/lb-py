import enum


class OrderType(enum.Enum):
    limit = 0
    market = 1


class Side(enum.Enum):
    borrow = 0
    lend = 1


class Ccy(enum.Enum):
    BTC = 1
    ETH = 2
    BCH = 3
    XRP = 4
    LTC = 5


class Status(enum.Enum):
    PENDING = 0
    ACCEPTED = 1
    REJECTED = 2
    DELETED = 3
    CANCELLED = 4
    UPDATED = 5
    EXECUTED = 6
    PARTIALLY_EXECUTED = 7


class Error(enum.Enum):
    # order has wrong data
    bad_order = 1
    # Market order is too large for the size of the order book
    large_market_order = 2
