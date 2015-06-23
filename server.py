#!/usr/bin/env python3

import os
import sys
import http.server
import socketserver


def start_server(directory, port=8080):
    CWD = os.getcwd()
    os.chdir(directory)

    ReqHandler = http.server.SimpleHTTPRequestHandler
    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.TCPServer(("", port), ReqHandler)

    print('Serving at http://localhost:' + str(port))
    try:
        httpd.serve_forever()
    except (KeyboardInterrupt, SystemExit):
        print('Server shutting down ...')
        httpd.shutdown()
        os.chdir(CWD)
        sys.exit()
