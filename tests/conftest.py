import asyncio
import os

import pytest
from faker import Faker

from lendingblock.client import Lendingblock

fake = Faker()


@pytest.fixture(scope='session', autouse=True)
def loop():
    """Return an instance of the event loop."""
    # Shared loop makes everything easier. Just don't mess it up.
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    yield loop
    loop.close()


@pytest.fixture(scope='session', autouse=True)
async def lb(loop):
    url = os.environ.get('LENDINGBLOCK_TEST_SERVER_URL')
    cli = Lendingblock(url, token=os.environ.get('LENDINGBLOCK_TEST_TOKEN'))
    user = await cli.execute(
        '/op/users', method='POST', json=dict(
            email=fake.email(),
            username=fake.user_name(),
            password=fake.password()
        )
    )
    token = await cli.execute(
        f'/op/users/{user["id"]}/tokens', method='POST', json={}
    )
    cli.token = token['key']
    yield cli
    await cli.close()


@pytest.fixture
async def org_id(lb):
    org_data = await lb.execute(
        '/organizations',
        'POST',
        json={
            'email': fake.ascii_company_email(),
            'country': 'GB',
        },
    )
    return org_data['id']
