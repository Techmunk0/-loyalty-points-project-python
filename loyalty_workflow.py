import asyncio
from datetime import timedelta

from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    from activity import Email, send_email


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
                if self._total_points % 1000 == 0:
                    await workflow.execute_activity(
                        send_email,
                        Email(
                            to=f"{workflow.info().workflow_id}",
                            subject="Congratulations!",
                            body="You have earned a free coffee!",
                        ),
                        start_to_close_timeout=timedelta(seconds=10),
                    ),
                    workflow.upsert_search_attributes({"points": [self._total_points]})

            if workflow.info().get_current_history_length() >= 2000:
                workflow.continue_as_new()

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
