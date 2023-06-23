from .base import BaseModel
from .title_description import TitleDescriptionModel


class BaseInfoModel(BaseModel, TitleDescriptionModel):
    """
    Abstact Base info model with uuid pk, title, description, create and update time 
    """
    
    class Meta:
        abstract = True
