from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from .censor import censor



def is_modified(original, processed):
	return original.strip() != processed


def out_json(request, in_text):
	censored = censor(in_text)
	return JsonResponse({
		"wasSwearing": is_modified(in_text, censored),
		"censored": censored
	})


def out_plain(request, in_text):
	censored = censor(in_text)
	return HttpResponse(censored, content_type='text/plain')