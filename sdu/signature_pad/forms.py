from django.forms import Field
from django.core import validators
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from signature_pad.helpers import decode_data_uri
from signature_pad.widgets import SignatureWidget


class SignatureField(Field):
    '''
    A field that stores signatures from Signature Pad
    '''
    widget = SignatureWidget()

    # def from_db_value(self, value, expression, connection):
    #     '''
    #     converts the data from the database to a data stream object
    #     '''
    #     if value is None:
    #         return value
    #     return decode_data_uri(value)


    # def to_python(self, value):
    #     '''
    #     the deserialization logic
    #     '''
       
    #     if value is validators.EMPTY_VALUES:
    #         return None

    #     try:
    #         return decode_data_uri(value)
    #     except ValueError:
    #         raise ValidationError(_('Invalid data uri string.') )