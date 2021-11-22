import asyncio
import logging

class Runnable:

	async def start(self):
		raise NotImplementedError

	async def stop(self, force:bool=False):
		raise NotImplementedError

	def run(self):
		loop = asyncio.get_event_loop()

		logging.info("Starting")

		loop.run_until_complete(self.start())

		async def idle():
			never = asyncio.Event()
			logging.info("Idling")
			await never.wait()

		try:
			loop.run_until_complete(idle())
		except KeyboardInterrupt:
			logging.info("Received SIGINT, stopping...")
			try:
				loop.run_until_complete(self.stop())
			except KeyboardInterrupt:
				logging.info("Received SIGINT, stopping for real")
				loop.run_until_complete(self.stop(force=True))

		logging.info("Done")

