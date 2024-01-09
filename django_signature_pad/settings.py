from django.conf import settings



################################################################################
# Signature Pad settings
# for attribute details, please see https://github.com/szimek/signature_pad
################################################################################

SETTING_PREFIX = 'SIGNATURE_PAD'

SIGNATURE_PAD_DOT_SIZE = getattr(
    settings, f'{SETTING_PREFIX}_DOT_SIZE', 0)
SIGNATURE_PAD_MIN_WIDTH = getattr(
    settings, f'{SETTING_PREFIX}_MIN_WIDTH', 0.5)
SIGNATURE_PAD_MAX_WIDTH = getattr(
    settings, f'{SETTING_PREFIX}_MAX_WIDTH', 2.5)
SIGNATURE_PAD_THROTTLE = getattr(
    settings, f'{SETTING_PREFIX}_THROTTLE', 16)
SIGNATURE_PAD_MIN_DISTANCE = getattr(
    settings, f'{SETTING_PREFIX}_MIN_DISTANCE', 5)
SIGNATURE_PAD_BACKGROUND_COLOR = getattr(
    settings, f'{SETTING_PREFIX}_BACKGROUND_COLOR', 'rgba(0, 0, 0, 0)')
SIGNATURE_PAD_PEN_COLOR = getattr(
    settings, f'{SETTING_PREFIX}_PEN_COLOR', 'black')
SIGNATURE_PAD_VELOCITY_FILTER_WEIGHT = getattr(
    settings, f'{SETTING_PREFIX}_VELOCITY_FILTER_WEIGHT', 0.7)
SIGNATURE_PAD_SAVE_BUTTON = getattr(
    settings, f'{SETTING_PREFIX}_SAVE_BUTTON', True)
SIGNATURE_PAD_RESET_BUTTON = getattr(
    settings, f'{SETTING_PREFIX}_RESET_BUTTON', True)


SIGNATURE_PAD_DEFAULT_CONFIG = dict(
    dotSize=SIGNATURE_PAD_DOT_SIZE,
    minWidth=SIGNATURE_PAD_MIN_WIDTH,
    maxWidth=SIGNATURE_PAD_MAX_WIDTH,
    throttle=SIGNATURE_PAD_THROTTLE,
    minDistance=SIGNATURE_PAD_MIN_DISTANCE,
    backgroundColor=SIGNATURE_PAD_BACKGROUND_COLOR,
    penColor=SIGNATURE_PAD_PEN_COLOR,
    velocityFilterWeight=SIGNATURE_PAD_VELOCITY_FILTER_WEIGHT,
    saveButton=SIGNATURE_PAD_SAVE_BUTTON,
    resetButton=SIGNATURE_PAD_RESET_BUTTON,    
)