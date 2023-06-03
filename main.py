import asyncio

from temporalio.client import Client
from temporalio.worker import Worker

from loyalty_workflow import LoyaltyProgram


async def main():
    # Start client
    client = await Client.connect("localhost:7233")

    # Run a worker for the workflow
    worker = Worker(
        client,
        task_queue="loyalty-program-task-queue",
        workflows=[LoyaltyProgram],
    )
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
