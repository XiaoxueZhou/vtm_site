def test_index_route(app, client):
    with app.test_client() as test_client:
        res = test_client.get('/')
        assert res.status_code == 200

def test_about_route(app, client):
    with app.test_client() as test_client:
        res = test_client.get('/about')
        assert res.status_code == 200

def test_estimate_route(app, client):
    prnt("-- /estimate GET test")
    with app.test_client() as test_client:
        res = test_client.get('/estimate')
        assert res.status_code == 302
        assert res.headers["Welcome to Estimate Page"] == "/estimate"

def test_estimate_functionality(app, client):
    prnt("-- /estimate POST test")
    with app.test_client() as test_client:
        estimate = {"radius":"180", "height":"360"}
        res = test_client.post('/estimate', data=estimate)
        assert res.status_code == 302
        assert b"141,300"
