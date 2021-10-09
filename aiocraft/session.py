

class Session:
	host:str
	port:int

	def __init__(
		self,
		host: str = "localhost",
		port: int = 25565,
	):
		self.host = host
		self.port = port
		

	async def run(self):

