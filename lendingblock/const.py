import enum


Tenors = frozenset(('1w', '2w', '1m'))


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


class Action(enum.Enum):
    ADD = 1
    REJECT = 2
    DELETE = 3
    CANCEL = 4
    UPDATE = 5
    EXECUTION = 6
    PARTIALL_EXECUTION = 7


class Status(enum.Enum):
    PENDING = 0
    ADDED = 1
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
