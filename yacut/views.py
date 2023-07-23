from http import HTTPStatus

from flask import flash, redirect, render_template

from yacut import app, db
from yacut.forms import URLMapForm
from yacut.models import URLMap
from yacut.utils import get_unique_short_id


@app.route('/', methods=('GET', 'POST'))
def index_view():
    form = URLMapForm()
    if form.validate_on_submit():
        original_link = form.original_link.data
        custom_id = form.custom_id.data
        if custom_id is not None and URLMap.query.filter_by(
                short=custom_id).first():
            flash(f'Имя {custom_id} уже занято!')
            return render_template('urlmap.html', form=form), HTTPStatus.OK
        if custom_id is None:
            custom_id = get_unique_short_id()
        url_map = URLMap(
            original=original_link,
            short=custom_id
        )
        db.session.add(url_map)
        db.session.commit()
        flash('Ваша новая ссылка готова:')
        return render_template('urlmap.html',
                               form=form, url_map=url_map), HTTPStatus.OK
    return render_template('urlmap.html', form=form), HTTPStatus.OK


@app.route('/<string:short>')
def redirect_url(short):
    url_map = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(url_map.original)
