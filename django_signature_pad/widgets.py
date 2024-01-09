import json
from django.forms import Media
from django.forms.widgets import HiddenInput
from django.template import loader
from django.template.loader import render_to_string
from django.templatetags.static import StaticNode
from django.utils.html import html_safe, json_script
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from signature_pad.settings import SIGNATURE_PAD_DEFAULT_CONFIG

@html_safe
class SignaturePadJSPath:
    '''
    Custom asset path for Signature Pad JS, with the defer attribute specified
    '''
    def __str__(self):
        path = StaticNode.handle_simple('signature_pad.js')
        return f'<script src="{path}" defer></script>'

# ------------------------------------------------------------------------------

@html_safe
class SignaturePadJSOptionsPath:
    '''
    Custom asset path for passing json options to Signature Pad
    '''
    def __init__(self, options):
        self.options = options
        del options['saveButton']
        del options['resetButton']

    def __str__(self):
        return json_script(self.options, 'signature_pad_options')

# ------------------------------------------------------------------------------

class SignatureWidget(HiddenInput):
    '''
    Custom Signature Widget 
    '''
    default_error_messages = {
        'invalid': _('No signature was added.'),
    }

    template_name = 'django_signature_pad/wagtail_widget.html'
    is_hidden = False


    def __init__(self, attrs=None, options=None):
        '''
        init function
        with additional signature pad options arg 

        params: attrs - html attributes for the widget (dict), or none if using
                    default settings
                options - signature pad options (dict), or None if using default
                    settings
        '''
        super().__init__(attrs)
        self.options = options or {}


    @property
    def media(self):
        '''
        dynamic media definition
        '''
        options = self.build_signature_pad_attrs()
        return Media(
            css = { 'all': ['signature_pad.css',], },
            js = [SignaturePadJSPath(), SignaturePadJSOptionsPath(options)],
        )


    def build_signature_pad_attrs(self):
        '''
        build the signature pad attribute dictionary, which will be passed to
        the signature pad options
        '''
        attrs = SIGNATURE_PAD_DEFAULT_CONFIG.copy()
        attrs.update(self.options)
        return attrs


    def build_signature_pad_id(self, name):
        '''
        build HTML id for signature pad canvas.
        '''
        return f'signature_pad_{name}'


    def get_context(self, name, value, attrs):
        '''
        returns the context for the templates
        '''
        context = super().get_context(name, value, attrs)
        signature_pad_id = self.build_signature_pad_id(name)
        options = self.build_signature_pad_attrs()
        context['signature_pad_widget'] = {}
        context['signature_pad_widget']['signature_pad_id'] = signature_pad_id
        context['signature_pad_widget']['options'] = options

        return context

# ------------------------------------------------------------------------------

# class WagtailAdminSignatureWidget(SignatureWidget):
#     '''
#     A signature widget for the wagtail admin interface
#     '''
#     template_name = 'django_signature_pad/wagtail_widget.html'