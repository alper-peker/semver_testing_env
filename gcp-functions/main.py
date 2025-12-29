import functions_framework

@functions_framework.http
def hello_http(request):
    if request.method not in ("GET", "POST"):
        return ("Method Not Allowed", 405, {"Allow": "GET, POST"})

    body = "This request is from the GCP function simulation. Real ones coming soon! ⚡"
    return (body, 200, {"X-Function": "hello_http"})
