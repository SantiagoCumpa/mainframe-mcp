import aiohttp

from schemas import ApiResponse

class HttpClient:
    @staticmethod
    async def get(
        url: str, 
        json: dict[str, str | int | bool | None]
    ) -> ApiResponse:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, json=json) as response:
                return await response.json()
            
http_client = HttpClient()