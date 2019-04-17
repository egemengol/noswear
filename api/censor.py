import requests

from urllib.parse import urljoin, urlencode

from django.conf import settings


def censor(text, api_endpoint=settings.SWEAR_API_URL, out_type="plain"):
	if text == "":
		return ""

	assert type(text) == str
	assert out_type == "plain" or out_type == "json"

	url = urljoin(api_endpoint, out_type) + "?" + urlencode({'text': text})

	resp = requests.get(url)
	return resp.text
