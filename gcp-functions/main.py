import functions_framework
import json

@functions_framework.http
def hello_http(request):
    if request.method not in ("GET", "POST"):
        return ("Method Not Allowed", 405, {"Allow": "GET, POST"})

    args = request.args or {}
    name = (args.get("name") or "").strip()
    shout = (args.get("shout") or "").strip().lower() in ("1", "true", "yes", "y")
    fmt = (args.get("format") or "").strip().lower()

    base = "This request is from the GCP function simulation. Real ones coming soon! ⚡"
    if name:
        base = f"{base} Hello, {name}!"
    if shout:
        base = base.upper()

    headers = {"X-Function": "hello_http"}

    if fmt == "json":
        payload = {"message": base, "status": "ok"}
        return (json.dumps(payload), 200, {**headers, "Content-Type": "application/json"})

    return (base, 200, headers)
