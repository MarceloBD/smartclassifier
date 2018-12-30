import aiohttp
import asyncio

class Datamuse():
	def __init__(self):
		return
	
	async def get_synonymous(self, word):
		async with  aiohttp.request('GET', 'http://api.datamuse.com/words?ml='+word) as response:
			html = await response.text()

		return html
		