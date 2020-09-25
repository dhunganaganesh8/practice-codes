from nose.tools import *
from app import app

app.config['TESTING'] = True
web = app.test_client()

def test_index():
    rv = web.get('/', follow_redirects=True)
    assert_equal(rv.status_code, 404)

    rk = web.get('/hello', follow_redirects=True)
    assert_equal(rk.status_code, 200)
    assert_in(b"Fill Out This Form", rk.data)

    data = {'name': 'Zed', 'greet': 'Hola'}
    rk = web.post('/hello', follow_redirects=True, data=data)
    assert_in(b"Zed", rk.data)
    assert_in(b"Hola", rk.data)
