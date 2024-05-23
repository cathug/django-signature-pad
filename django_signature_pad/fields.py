import base64

from django.core.exceptions import ValidationError
from django.db.models import Field
from django.utils.translation import gettext_lazy as _
from django_signature_pad.forms import SignatureField as SignatureFormField


def decode_data_uri(data_url):
    '''
    this helper decodes the uri string similar to the method
    outlined in the signature pad readme file: 
    https://github.com/szimek/signature_pad

    param: data_url - the data url string
    returns: a decoded byte string, MIME string tuple
    '''
    content_type, encoded_image = data_url.split(';base64,')
    decoded_image = base64.urlsafe_b64decode(encoded_image)
    media_type = content_type.split('/')[-1]

    return decoded_image, media_type


def encode_image(image, media_type='data:image/png'):
    '''
    The reverse of decode_data_uri().  Encodes the image to base64 data_uri
    string

    params: image - image (byte)
            media_type - one of 'data:image/png', 'data:image/svg', or 
                'data:image/jpeg' (str)
    returns: data url string, or None otherwise
    '''
    mime = ['png', 'svg', 'jpeg']
    if media_type in [f'data:image/{m}' for m in mime]:
        encoded_image = base64.urlsafe_b64encode(image)
        return f'{media_type};base64,{encoded_image}'

    return None


class SignatureField(Field):
    '''
    A field that captures the signature from a canvas
    '''
    description = 'A field that captures the signature from a canvas'


    def get_internal_type(self):
        '''
        database storage type
        '''
        return 'TextField'


    # def from_db_value(self, value, expression, connection):
    #     '''
    #     converts the data from the database to a data stream object
    #     '''
    #     if value is None:
    #         return value
    #     return decode_data_uri(value)


    def to_python(self, value):
        '''
        deserializes the value 
        '''
        if isinstance(value, str) or value is None:
            return value
        try:
            return str(value)
        except TypeError:
            raise ValidationError(_(f'{value} cannot be cast as a string.') )


    # def get_prep_value(self, value):
    #     '''
    #     converts python object back to database query value
    #     '''
    #     value =  super().get_prep_value(value)
    #     if value is None:
    #         return value
    #     try:
    #         return encode_image(value)
    #     except TypeError:
    #         raise ValidationError(_(f'{value} cannot be converted back to a database query value.') )
   

    def formfield(self, **kwargs):
        '''
        Specify a signature form field for a model field
        '''
        return super().formfield(
            **{
                'form_class': SignatureFormField,
                **kwargs,
            }
        )
