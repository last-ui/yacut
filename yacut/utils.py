import random
import string

from settings import DEFAULT_SHORT_URL_LENGTH
from yacut.models import URLMap


def get_unique_short_id(unique_length=DEFAULT_SHORT_URL_LENGTH):
    while True:
        short_url = ''.join(
            [random.choice(string.ascii_letters + string.digits)
                    for _ in range(unique_length)]
        )
        if not URLMap.query.filter_by(short=short_url).first():
            return short_url
