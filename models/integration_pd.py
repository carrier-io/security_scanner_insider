from typing import Optional, List
from pylon.core.tools import log
from pydantic import BaseModel, validator


class IntegrationModel(BaseModel):
    # save_intermediates_to: Optional[str] = '/data/intermediates/sast'
    timeout: Optional[int] = 0
    tech: str


    @validator('tech')
    def validate_tech(cls, v):
        if v not in ['csharp', 'android', 'ios', 'javascript']:
            raise ValueError("tech value must one of csharp, andoid, ios, javascript")
        return v


    def check_connection(self) -> bool:
        try:
            return True
        except Exception as e:
            log.exception(e)
            return False
