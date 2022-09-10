from dataclasses import field
from pydantic import BaseSettings, validator
from typing import Optional
from pydantic.fields import ModelField

class Config(BaseSettings,extra="ignore"):
    fastapi_reload: bool = False
    arxiv_dir = Optional[str] = None
    arxiv_to_me: bool = True
    arxiv_live_off_notify: bool = False
    arxiv_proxy: Optional[str] = None
    arxiv_interval: int = 10
    arxiv_dynamic_interval: int = 0
    arxiv_dynamic_at: bool = False
    arxiv_screenshot_style: str = "mobile"

    @validator("arxiv_interval", "arxiv_dynamic_interval")
    def non_negative(cls, v:int,  field: ModelField):
        if v < 0:
            return field.default
        return v
