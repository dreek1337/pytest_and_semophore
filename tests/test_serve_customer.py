import pytest
import pytest_asyncio
from main import serve_customer


@pytest_asyncio.fixture
async def make_result(
        cashiers_number: int,
        customers: list[int]
) -> int:
    res = await serve_customer(cashiers_number, customers)

    return res


@pytest.mark.parametrize('cashiers_number, customers, res', [
    (3, [0, 0, 0, 5], 5),
    (3, [0, 0, 0, 4], 4),
    (3, [1, 1, 1, 7], 8),
    (3, [0, 0, 0, 5, 4, 3], 5),
    (2, [1, 1, 2, 9], 10),
    (10, [1, 1, 2, 4], 4)
])
def test_good_result(
        cashiers_number: int,
        customers: list[int],
        res: int,
        make_result: int
) -> None:

    assert make_result == res


@pytest.mark.parametrize('cashiers_number, customers, res', [
    (3, [0, 0, 0, 5], 2),
    (3, [0, 0, 0, 4], 3),
    (3, [1, 1, 1, 7], 9),
    (3, [0, 0, 0, 5, 4, 3], 6),
    (2, [1, 1, 2, 9], 11),
    (10, [1, 1, 2, 4], 5)
])
def test_bad_result(
        cashiers_number: int,
        customers: list[int],
        res: int,
        make_result: int
) -> None:

    assert make_result != res
