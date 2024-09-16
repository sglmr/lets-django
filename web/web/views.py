import logging

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request: HttpRequest) -> HttpResponse:
    """Homepage view for the website"""

    return render(request, "index.html")
