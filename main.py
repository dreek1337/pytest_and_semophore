import asyncio
import time


async def check_time(
        customer_time: int,
        semaphore: asyncio.Semaphore
) -> float:
    """
    Вычисление с помощью слипов и определения времени
    :param customer_time:
    :param semaphore:
    :return: Время когда завершилось выполнение обслуживания
    """
    async with semaphore:
        await asyncio.sleep(customer_time)

        return time.time()


async def serve_customer(
        cashiers_number: int,
        customers: list[int]
) -> int:
    """
    Вычисление максимального времени обслуживания всех клиентов в очереди
    :param cashiers_number:
    :param customers:
    :return: Максимальное время обслуживания всех клиентов
    """
    sem = asyncio.Semaphore(cashiers_number)
    start_time = time.time()

    res = await asyncio.gather(*[check_time(i, sem) for i in customers])

    return int(max(res) - start_time)


if __name__ == '__main__':
    asyncio.run(serve_customer(2, [2, 3, 4, 5, 6, 7, 1, 2]))
