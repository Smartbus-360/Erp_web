import requests
from django.shortcuts import redirect

FASTAPI_BASE_URL = "https://erp.backend.smartbus360.com"

def api_request(request, method, path, **kwargs):
    auth = request.session.get("auth")

    if not auth or not auth.get("access_token"):
        raise PermissionError("Not logged in")

    headers = kwargs.pop("headers", {})
    headers["Authorization"] = f"Bearer {auth['access_token']}"

    response = requests.request(
        method,
        f"{FASTAPI_BASE_URL}{path}",
        headers=headers,
        timeout=10,
        **kwargs
    )

    if response.status_code == 401:
        request.session.flush()
        raise PermissionError("Session expired")

    return response
