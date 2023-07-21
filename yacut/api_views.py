import re
from http import HTTPStatus

from flask import jsonify, request

from yacut import app, db
from yacut.error_handlers import InvalidAPIUsage
from yacut.models import URLMap
from yacut.utils import get_unique_short_id


@app.route('/api/id/', methods=('POST',))
def create_id():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    url = data.get('url')
    if not url:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    short_id = data.get('custom_id')
    if short_id and URLMap.query.filter_by(short=short_id).first():
        raise InvalidAPIUsage(f'Имя "{short_id}" уже занято.')
    elif short_id and not re.match(r'^[A-Za-z0-9]{0,16}$', short_id):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    if not short_id:
        short_id = get_unique_short_id()
    url_map = URLMap(
        original=url,
        short=short_id
    )
    db.session.add(url_map)
    db.session.commit()
    return (jsonify({'url': url_map.original,
                     'short_link': f'{request.host_url}{short_id}'}),
            HTTPStatus.CREATED)


@app.route('/api/id/<string:short_id>/', methods=('GET',))
def get_url(short_id):
    url_map = URLMap.query.filter_by(short=short_id).first()
    if url_map:
        return jsonify({'url': url_map.original}), HTTPStatus.OK
    raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
