def test_can_reach_search_with_logged_in_session(logged_in_session):
    search_resp = logged_in_session.get(url="http://127.0.0.1:5000/search")
    assert "Search for a book!" in search_resp.text
