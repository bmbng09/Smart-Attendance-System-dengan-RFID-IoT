try:
    import usocket as socket
except:
    import socket

import gc

class Response:

    def __init__(self, sock):
        self.raw = sock
        self.encoding = "utf-8"
        self._cached = None

    def close(self):
        if self.raw:
            self.raw.close()
            self.raw = None

    @property
    def content(self):
        if self._cached is None:
            try:
                self._cached = self.raw.read()
            finally:
                self.raw.close()
                self.raw = None
        return self._cached

    @property
    def text(self):
        return str(self.content, self.encoding)

    def json(self):
        import ujson
        return ujson.loads(self.content)


def request(method, url, data=None, json=None, headers={}, stream=None):
    try:
        proto, dummy, host, path = url.split("/", 3)
    except ValueError:
        proto, dummy, host = url.split("/", 2)
        path = ""
    if proto == "http:":
        port = 80
    elif proto == "https:":
        import ussl
        port = 443
    else:
        raise ValueError("Unsupported protocol: " + proto)

    if ":" in host:
        host, port = host.split(":", 1)
        port = int(port)

    ai = socket.getaddrinfo(host, port)
    addr = ai[0][4]
    s = socket.socket()

    try:
        s.connect(addr)
        if proto == "https:":
            s = ussl.wrap_socket(s, server_hostname=host)
        s.write(b"%s /%s HTTP/1.0\r\n" % (method.encode(), path.encode()))
        s.write(b"Host: %s\r\n" % host.encode())

        for k in headers:
            s.write(k.encode())
            s.write(b": ")
            s.write(headers[k].encode())
            s.write(b"\r\n")

        if json is not None:
            import ujson
            data = ujson.dumps(json)
            s.write(b"Content-Type: application/json\r\n")

        if data:
            s.write(b"Content-Length: %d\r\n" % len(data))

        s.write(b"\r\n")

        if data:
            s.write(data if isinstance(data, bytes) else data.encode())

        l = s.readline()
        protover, status, msg = l.split(None, 2)
        status = int(status)

        while True:
            l = s.readline()
            if not l or l == b"\r\n":
                break

        resp = Response(s)
        resp.status_code = status
        return resp

    except Exception as e:
        s.close()
        raise e


def get(url, **kw):
    return request("GET", url, **kw)

def post(url, **kw):
    return request("POST", url, **kw)

def put(url, **kw):
    return request("PUT", url, **kw)

def patch(url, **kw):
    return request("PATCH", url, **kw)

def delete(url, **kw):
    return request("DELETE", url, **kw)

