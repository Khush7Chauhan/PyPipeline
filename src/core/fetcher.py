import asyncio
import aiohttp  # type: ignore[import-not-found]
from pathlib import Path
from src.utils.logger import logger
from src.utils.decorator import time_it

async def download_file(session: aiohttp.ClientSession, url: str, dest_dir: Path, idx: int) -> None:
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            content = await response.read()

            ext = Path(url).suffix or ".txt"
            dest_path = dest_dir / f"downloaded_data_{idx}{ext}"
            dest_path.parent.mkdir(parents=True, exist_ok=True)

            with open(dest_path, "wb") as f:
                f.write(content)
            logger.info(f"Downloaded: {url} -> {dest_path.name}")
    except Exception as e:
        logger.error(f"Failed to download {url}: {e}")

@time_it
async def fetch_all_remote_data(urls: list[str], dest_dir: Path) -> None:
    async with aiohttp.ClientSession() as session:
        tasks = [download_file(session, url, dest_dir, i) for i, url in enumerate(urls)]
        await asyncio.gather(*tasks)