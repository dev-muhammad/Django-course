from .uuid import UUIDmodel
from .create_update_time import CreateUpdatetimeModel
from .is_active import IsActiveModel

class BaseModel(UUIDmodel, IsActiveModel, CreateUpdatetimeModel):
    """
    Abstact Base model with uuid pk and create and update time
    """

    class Meta:
        abstract = True
