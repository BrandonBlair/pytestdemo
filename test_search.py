def test_can_receive_search_results(logged_in_session, app_url):
    author_name = "Sagan"
    search_url = f'{app_url}/v1/search?author={author_name}'
    search_resp = logged_in_session.get(url=search_url)
    search_data = search_resp.json()
    results = search_data.get("results")
    resource = results[0]
    title = resource.get("title")

    expected_title = "Cosmos"

    assert title == expected_title
