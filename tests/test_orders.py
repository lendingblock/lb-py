import pytest

from lendingblock.const import Side, OrderType, Ccy


@pytest.fixture
async def wallets_org_id(lb, org_id):
    for ccy in Ccy.BTC.name, Ccy.ETH.name, Ccy.LND.name:
        await lb.execute(
            f'organizations/{org_id}/wallets',
            'POST',
            json={
                'address': f'{org_id}{ccy}',
                'currency': ccy,
            }
        )
    return org_id


@pytest.fixture
async def order_id(lb, wallets_org_id):
    order_data = {
        'org_id': wallets_org_id,
        'type': OrderType.limit.name,
        'side': Side.lend.name,
        'tenor': '1d',
        'amount': 10.0,
        'currency': Ccy.BTC.name,
        'price': 2.0,
    }
    order = await lb.execute('orders', 'POST', json=order_data)
    return order['id']


async def test_create(lb, wallets_org_id):
    order_data = {
        'org_id': wallets_org_id,
        'type': OrderType.limit.name,
        'side': Side.lend.name,
        'tenor': '1d',
        'amount': 10.0,
        'currency': Ccy.BTC.name,
        'price': 2.0,
    }
    resp = await lb.orders.create(order_data)
    assert 'id' in resp


async def test_get(lb, order_id):
    resp = await lb.orders.get(order_id)
    assert resp['id'] == order_id


async def test_get_list(lb, order_id):
    resp = await lb.orders.get_list()
    assert order_id in [order['id'] for order in resp]


async def test_delete(lb, order_id):
    await lb.orders.delete(order_id)
    all_orders = await lb.execute('orders')
    assert order_id not in all_orders
