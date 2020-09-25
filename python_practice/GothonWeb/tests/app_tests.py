from nose.tools import *
from app import *

app.config['TESTING'] = True
web = app.test_client()

def test_session():
    with web:
        rv = web.get('/')
        assert_equal(session['room_name'], 'central_corridor')

def test_get_post():
    with web:
        rv = web.get('/game', follow_redirects=True)
        room = planisphere.load_room(session['room_name'])
        assert_equal(rv.status_code, 200)
        assert room.name.encode() in rv.data

        data = {'action': 'shoot!'}
        rv = web.post('/game', follow_redirects=True, data=data)
        assert_in(b'death', rv.data)
        assert_in(b'Play Again', rv.data)

        data = {'action': 'tell a joke'}
        rv = web.post('/game', follow_redirects=True, data=data)
        room = planisphere.load_room(session['room_name'])
        assert_in(room.name.encode(), rv.data)
