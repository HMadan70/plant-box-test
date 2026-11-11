def test_home_page_welcomes_shoppers(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome to Leaf & Pot" in response.text


def test_every_page_has_the_footer(client):
    assert "<footer>" in client.get("/").text
