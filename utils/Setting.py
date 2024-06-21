import logging
import sys
if sys.version_info[:2] <(3,0):
    from pydantic import BaseSettings,BaseModel
else:
    from pydantic_settings import BaseSettings,BaseModel



logger = logging.getLogger(__name__)


class DatabasePayload(BaseModel):
    parent:str
    
    
class Setting(BaseSettings):
    NOTION_DATABASE_ENDPOINT_URL:str  = "https://api.notion.com/v1/pages"
    NOTION_DATABASE_PAYLOAD: dict = {}
    
