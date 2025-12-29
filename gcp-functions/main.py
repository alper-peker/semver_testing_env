import functions_framework
import json

@functions_framework.http
def hello_http(request):
    if request.method not in ("GET", "POST"):
        return ("Method Not Allowed", 405, {"Allow": "GET, POST"})

    args = request.args or {}
    name = (args.get("name") or "").strip()
    fmt = (args.get("format") or "").strip().lower()

    base = "This request is from the GCP function simulation. Real ones coming soon! ⚡"
    if name:
        base = f"{base} Hello, {name}!"

    headers = {"X-Function": "hello_http"}

    payload = {"message": base, "status": "ok"}

    if fmt == "text":
        return (base, 200, {**headers, "Content-Type": "text/plain; charset=utf-8"})

    return (json.dumps(payload), 200, {**headers, "Content-Type": "application/json"})
