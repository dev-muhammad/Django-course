from common.models import BaseInfoModel


class Country(BaseInfoModel):
    """
    Country model
    fields:
        - id (uuid)
        - create_time (datetime)
        - update_time (datetime)
        - is_active (bool defaul=True)
        - title
        - description
    """

    class Meta:
        verbose_name= 'Страна'
        verbose_name_plural = 'Страны'
        ordering = ['title']
