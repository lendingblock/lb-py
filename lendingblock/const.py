import enum


Tenors = frozenset(('1d', '1w', '2w', '1m'))


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
    LND = 6


class TradableCcy(enum.Enum):
    BTC = 1
    ETH = 2
    BCH = 3
    LTC = 5


class OrderAction(enum.Enum):
    ADD = 1
    REJECT = 2
    DELETE = 3
    CANCEL = 4
    # UPDATE = 5
    EXECUTION = 6
    PARTIAL_EXECUTION = 7


class OrderStatus(enum.Enum):
    PENDING = 0
    ADDED = 1
    REJECTED = 2
    DELETED = 3
    CANCELLED = 4
    # UPDATED = 5
    EXECUTED = 6
    PARTIALLY_EXECUTED = 7


class OrderError(enum.Enum):
    # order has wrong data
    bad_order = 1
    # Market order is too large for the size of the order book
    large_market_order = 2
    # Order is too small
    small_order = 3
    # Order is too big
    large_order = 4
    # Order is not a multiple of step (tick size)
    order_step = 5
    # Order was flagged as a wash trade
    wash_trade = 6
    # Limit order crosses too far into the other side of the book
    deep_limit_order = 7
