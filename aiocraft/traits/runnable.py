import asyncio
import logging

from signal import signal, SIGINT, SIGTERM, SIGABRT

class Runnable:

	async def start(self):
		raise NotImplementedError

	async def stop(self, force:bool=False):
		raise NotImplementedError

	async def _stop_wrapper(self):
		done, pending = await asyncio.wait(self.stop(), FORCE_QUIT.wait(), return_when=asyncio.FIRST_COMPLETED)
		if FORCE_QUIT.is_set(): # means previous stop() didn't finish and user sent another SIGINT
			await self.stop(force=True)

	def run(self):
		global DONE
		global FORCE_QUIT

		logging.info("Starting process")

		DONE = asyncio.Event()
		FORCE_QUIT = asyncio.Event()
		
		def signal_handler(signum, __):
			global DONE
			global FORCE_QUIT
			if signum == SIGINT:
				if DONE.is_set():
					logging.info("Received SIGINT, terminating")
					FORCE_QUIT.set()
				else:
					logging.info("Received SIGINT, stopping gracefully...")
					DONE.set()

		signal(SIGINT, signal_handler)

		loop = asyncio.get_event_loop()

		async def main():
			await self.start()
			await DONE.wait()
			await self._stop_wrapper()

		loop.run_until_complete(main())

		logging.info("Process finished")

