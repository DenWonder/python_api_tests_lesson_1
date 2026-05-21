from typing import Literal
import dotenv
import pydantic
import pydantic_settings

class Config(pydantic_settings.BaseSettings):
    context: Literal['local', 'test', 'stage'] = 'local'
    base_url: str = ''

dotenv.load_dotenv()

config = Config(dotenv.find_dotenv(f'.env.{Config().context}'))