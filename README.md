# Django Signature Pad

Django Signature Pad adds signature capability to Django web apps.
It is a wrapper for the `signature_pad` Javascript library, which allows
users to draw signatures on HTML5 canvases.  Associated widgets plus model and
form fields are defined to make `signature_pad` play nice with Django.

It is heavily influenced by a similar package `django-jsignature` which uses
the jQuery library `jSignature` to handle signatures on the frontend.

The latest source code for [`signature_pad`](https://github.com/szimek/signature_pad)


## Requirements

The following packages must be installed before installing this app:

+ `Node` >= v.18 LTS
+ `signature_pad` == v. 4.1.7
+ `npm` >= v.9.2.0
+ `Django` ~= 4.2 (not tested on other versions)



## Quick start

1. Add `django-signature-pad` to your `INSTALLED_APPS` setting,
    i.e. `settings.py` file:

```python
    INSTALLED_APPS = [
        ...,
        'django_signature_pad',
    ]

```


2. For models requiring a signature field,

```python
    from django.db import models
    from django_signature_pad.fields import SignatureField
    ...

    class Foo(models.Model):
        signature = SignatureField()

```


3. For forms requiring a signature field,

```python
    from django import forms
    from django_signature_pad.fields import SignatureField
    ...

    class Foo(forms.Form):
        signature = SignatureField()

```


4. `signature_pad` customization:

Each signature pad widget will be initialized with the default settings - see
the `Options` section in the [`signature_pad` docs](https://github.com/szimek/signature_pad).
To initialize the widget with a different global setting, add the following
settings to your Django `settings.py`:

```python
    # add these variables accordingly
    SIGNATURE_PAD_DOT_SIZE = ...
    SIGNATURE_MIN_WIDTH = ...
    SIGNATURE_PAD_MAX_WIDTH = ...
    SIGNATURE_PAD_THROTTLE = ...
    SIGNATURE_PAD_MIN_DISTANCE = ...
    SIGNATURE_PAD_BACKGROUND_COLOR = ...
    SIGNATURE_PAD_PEN_COLOR = ...
    SIGNATURE_PAD_VELOCITY_FILTER_WEIGHT = ...
```

5. TODO

+ Add test cases
+ Wagtail integration


## License

WTFPL.  For code that does not belong to me, please refer to the licensing
docs from the respective authors.

