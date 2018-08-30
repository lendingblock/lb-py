import uuid


async def test_get_list(lb):
    resp = await lb.loans.get_list()
    assert isinstance(resp, list)


async def test_get_wrong_id(lb):
    no_such_loan = uuid.uuid4().hex
    resp = await lb.loans.get(no_such_loan)
    assert isinstance(resp, dict)
