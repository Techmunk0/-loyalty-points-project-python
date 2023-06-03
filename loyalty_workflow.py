import asyncio

from temporalio import workflow


@workflow.defn
class LoyaltyProgram:
    def __init__(self) -> None:
        self._pending_points: asyncio.Queue[int] = asyncio.Queue()
        self._total_points: int = 0
        self._exit: bool = False

    @workflow.run
    async def run(self) -> int:
        while True:
            await workflow.wait_condition(
                lambda: not self._pending_points.empty() or self._exit
            )

            while not self._pending_points.empty():
                point = await self._pending_points.get()
                self._total_points += point

            if self._exit:
                return self._total_points

    @workflow.signal
    async def add_to_points(self, point: int) -> None:
        await self._pending_points.put(point)

    @workflow.signal
    async def remove_from_points(self, point: int) -> None:
        await self._pending_points.put(-point)

    @workflow.signal
    def exit(self) -> None:
        self._exit = True

    @workflow.query
    def loyalty_details(self) -> int:
        return self._total_points
