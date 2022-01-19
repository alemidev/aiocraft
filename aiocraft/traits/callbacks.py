import asyncio
import uuid
import logging

from inspect import isclass
from typing import Dict, List, Set, Any, Callable, Type

class CallbacksHolder:

	_callbacks : Dict[Any, List[Callable]]
	_tasks : Dict[uuid.UUID, asyncio.Event]

	_logger : logging.Logger

	def __init__(self):
		super().__init__()
		self._callbacks = {}
		self._tasks = {}

	def callback_keys(self, filter:Type = None) -> Set[Any]:
		return set(x for x in self._callbacks.keys() if not filter or (isclass(x) and issubclass(x, filter)))

	def register(self, key:Any, callback:Callable):
		if key not in self._callbacks:
			self._callbacks[key] = []
		self._callbacks[key].append(callback)
		return callback

	def trigger(self, key:Any) -> List[Callable]:
		if key not in self._callbacks:
			return []
		return self._callbacks[key]

	def _wrap(self, cb:Callable, uid:uuid.UUID) -> Callable:
		async def wrapper(*args):
			try:
				ret = await cb(*args)
			except Exception:
				logging.exception("Exception processing callback")
				ret = None
			self._tasks[uid].set()
			self._tasks.pop(uid)
			return ret
		return wrapper

	def run_callbacks(self, key:Any, *args) -> None:
		for cb in self.trigger(key):
			task_id = uuid.uuid4()
			self._tasks[task_id] = asyncio.Event()

			asyncio.get_event_loop().create_task(self._wrap(cb, task_id)(*args))

	async def join_callbacks(self):
		await asyncio.gather(*list(t.wait() for t in self._tasks.values()))
		self._tasks.clear()

