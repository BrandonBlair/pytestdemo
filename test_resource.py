def test_can_add_resource(logged_in_session, app_url):
    resource_url = f'{app_url}/v1/resource'

    add_resource_payload = {
        "title": "Elegant API Automation: The Sequel",
        "authorFirst": "Brandon",
        "authorMiddle": "",
        "authorLast": "Blair",
        "edition": "1",
        "isbn10": "9999",
        "isbn13": ""
    }

    add_resource_resp = logged_in_session.post(
        url=resource_url,
        json=add_resource_payload
    )

    resource_data = add_resource_resp.json()
    resource = resource_data.get("resource")
    title = resource.get("title")
    
    expected_title = "Elegant API Automation: The Sequel"
    
    assert title == expected_title

    # {"details":"Elegant API Automation added successfully.","error":"None","resource":{"author":"Brandon Blair","edition":"1","id":1,"isbn10":"5678","isbn13":"","title":"Elegant API Automation"}}
