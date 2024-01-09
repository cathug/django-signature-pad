import base64

from django.core.files.base import ContentFile



def decode_data_uri(data_uri):
    '''
    this helper decodes the uri string similar to the method
    outlined in the signature pad readme file: 
    https://github.com/szimek/signature_pad

    param: data_uri - the data uri string
    returns: a raw file object ready to be saved to blob storage backend
    '''
    content_type, encoded_image = data_uri.split(';base64,')
    decoded_image = base64.urlsafe_b64decode(encoded_image)
    media_type = content_type.split('/')[-1]
    return ContentFile(decoded_image, name=f'signature.{media_type}')