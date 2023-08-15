from typing import Optional

from teleapi.core.orm.validators.exceptions import ValidationError
from teleapi.core.orm.models import Model
from teleapi.core.orm.models.generics.fields import (
    StringModelField,
    BooleanModelField
)


class InlineKeyboardButtonModel(Model):
    text: str = StringModelField()
    url: Optional[str] = StringModelField(is_required=False)
    callback_data: Optional[str] = StringModelField(is_required=False)
    switch_inline_query: Optional[str] = StringModelField(is_required=False)
    switch_inline_query_current_chat: Optional[str] = StringModelField(is_required=False)
    pay: Optional[bool] = BooleanModelField(is_required=False)

    # web_app
    # login_url
    # switch_inline_query_chosen_chat
    # callback_game

    def __init__(self, **kwargs) -> None:
        if not any((
                kwargs.get('text'),
                kwargs.get('url'),
                kwargs.get('callback_data'),
                kwargs.get('switch_inline_query'),
                kwargs.get('switch_inline_query_current_chat'),
                kwargs.get('pay'),
                kwargs.get('web_app'),
                kwargs.get('login_url'),
                kwargs.get('switch_inline_query_chosen_chat'),
                kwargs.get('callback_game')
        )):
            raise ValidationError("You must define one of optional arguments to use this")

        super().__init__(**kwargs)
