
import requests
from database import db
from cv_app.faqs.models import FaQuestion

"""All Tests
This file is where every one of the tests that I wrote myself are stored.
"""

expected_urls = [("/", "Elijah Ruffin Portfolio"), ("/home", "Elijah Ruffin Portfolio"),
                 ("/faqs", "FAQs"), ("/projects", "Portfolio Projects"), ("/contact", "Contact Me"),
                 ("/experience", "Work Experience"), ("/bio", "About Me"), ("/resume", "Resume")]


# Dynamically checking each title element value by accessing a views data directly.
# I'll have to standardize when I use the words route and url.
def test_check_titles(client, urls):
    expected_titles = {"/": "Elijah Ruffin Portfolio", "/home": "Elijah Ruffin Portfolio", "/faqs": "FAQs",
                       "/projects": "Portfolio Projects", "/contact": "Contact Me", "/experience": "Work Experience",
                       "/bio": "About Me", "/resume": "Resume"}

    for url_rule in urls:
        if "GET" in url_rule.methods and not url_rule.rule.startswith('/static') and '<' not in url_rule.rule:
            response = client.get(url_rule.rule)

            current_route = url_rule.rule
            expected = expected_titles.get(current_route)

            print(f"Result: {current_route} Expected: {expected}")

            try:
                assert expected.encode('utf-8') in response.data
                print(f"{current_route} title is correct!")
            except AttributeError as ae:
                print(f"{current_route} not in expected_titles.")
                print("Attribute error. The get function could not find the name of a url to the match current "
                      "url taken from app.url_map's url list.")
                print(f"Check that the route function is spelled correctly or add the function to expected_routes.")


# Meta Tag Presence
def test_meta_tag(client, urls):
    for url_rule in urls:
        response = client.get(url_rule.rule)
        try:
            assert f'<meta name="viewport" content="width=device-width, initial-scale=1">'.encode(
                'utf-8') in response.data
            print(f"{url_rule} title has a meta tag!")

        except AttributeError as ae:
            print(f"{url_rule} does not have a meta tag.")


# Confirm a FAQs records can be added successfully.
def test_check_faqs_test_fixture(client, app):
    with app.app_context():
        faq_record = FaQuestion(source_file="test/file/path", question="Test Question", answer="Test Answer")
        db.session.add(faq_record)
        db.session.commit()

        records = FaQuestion.query.first()
        # print(records)

    assert records is not None


def check_url(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.RequestException:
        return False


# This test will take a long time because each get request is made synchronously.
# aiohttp and import asyncio make this very easy.
# Add a way to scan the entire site for hyperlinks.
# Could use reg ex for a link pattern in the pages response data.
def test_hyperlinks_status():
    urls = [
        "https://aws.amazon.com/certification/certified-cloud-practitioner/",
        "https://werkzeug.palletsprojects.com/en/2.3.x/",
        "https://flask.palletsprojects.com/en/3.0.x/",
        "https://www.atlassian.com/agile",
        "https://www.atlassian.com/software/jira/guides/getting-started/introduction#what-is-jira-software",
        "https://www.debian.org/doc/",
        "https://github.com/ruffineli77",
        "https://github.com/ruffineli77/ArchetypeApp",
        "https://github.com/ruffineli77/PortfolioPortal",
        "https://github.com/ruffineli77/InstagramClone",
        "https://github.com/ruffineli77/DonationWebsite",
        "https://github.com/ruffineli77/AdobeExpressClone",
        "https://github.com/ruffineli77/WildlifeCamera.git",
    ]
    for url in urls:
        assert check_url(url), f"URL {url} is not accessible"


# print("Testing that each page has a title element.\n")
# print("Testing that each page has a meta tag for responsiveness.\n")
# print("Testing that a database record can be added successfully.\n")
# print("Testing that links used in the bio page still work.\n")
