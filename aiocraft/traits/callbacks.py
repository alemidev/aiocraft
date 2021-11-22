import asyncio
from uuid import uuid4

from typing import Dict, List, Any, Callable

class CallbacksHolder:

	_callbacks : Dict[Any, List[Callable]]
	_tasks : Dict[str, asyncio.Event]

	def __init__(self):
		super().__init__()
		self._callbacks = {}
		self._tasks = {}

	def register(self, key:Any, callback:Callable):
		if key not in self._callbacks:
			self._callbacks[key] = []
		self._callbacks[key].append(callback)

	def trigger(self, key:Any) -> List[Callable]:
		if key not in self._callbacks:
			return []
		return self._callbacks[key]

	def run_callbacks(self, key:Any, *args) -> None:
		for cb in self.trigger(key):
			task_id = str(uuid4())
			self._tasks[task_id] = asyncio.Event()

			async def wrapper(*args):
				await cb(*args)
				self._tasks[task_id].set()
				self._tasks.pop(task_id)

			asyncio.get_event_loop().create_task(wrapper(*args))

	async def join_callbacks(self):
		await asyncio.gather(*list(t.wait() for t in self._tasks.values()))
		self._tasks.clear()

