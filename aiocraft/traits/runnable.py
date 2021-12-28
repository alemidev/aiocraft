import asyncio
import logging

from typing import Optional
from signal import signal, SIGINT, SIGTERM, SIGABRT

class Runnable:
	_is_running : bool
	_stop_task : Optional[asyncio.Task]

	def __init__(self):
		self._is_running = False
		self._stop_task = None

	async def start(self):
		self._is_running = True

	async def stop(self, force:bool=False):
		self._is_running = False

	def run(self):
		logging.info("Starting process")

		def signal_handler(signum, __):
			if signum == SIGINT:
				if self._stop_task:
					self._stop_task.cancel()
					logging.info("Received SIGINT, terminating")
				else:
					logging.info("Received SIGINT, stopping gracefully...")
				self._stop_task = asyncio.get_event_loop().create_task(self.stop(force=self._stop_task is not None))

		signal(SIGINT, signal_handler)

		loop = asyncio.get_event_loop()

		async def main():
			await self.start()
			while self._is_running:
				await asyncio.sleep(1)

		loop.run_until_complete(main())

		logging.info("Process finished")

