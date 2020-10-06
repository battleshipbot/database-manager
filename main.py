"""
Created by Epic at 10/6/20
"""

from cache import CacheElement
from bridge.bridge import BridgeClient
from asyncio import sleep

client = BridgeClient("database_manager", paths=["database/fetch", "database/dispatch", "database/ping"])

tasks_in_queue = 0


async def status_report():
    while True:
        metrics = {
            "tasks_in_queue": tasks_in_queue
        }
        await client.dispatch("DATABASE_STATS", metrics, path="metrics/register")
        await sleep(60)
