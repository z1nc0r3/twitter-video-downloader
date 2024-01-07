# Assuming all url arguments are standard twitter media url's.

import pytest
from urllib.parse import urlparse


@pytest.mark.unit
def test_domain_valid():
    """Assert the site is equal to twitter.com"""
    url = "https://x.com/realmadriden/status/1743790569866821949?s=20"

    parsed_url = urlparse(url)

    assert parsed_url.hostname == "x.com"
