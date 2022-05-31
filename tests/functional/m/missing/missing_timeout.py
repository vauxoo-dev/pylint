# pylint: disable=consider-using-with,import-error,missing-module-docstring,reimported
import http.client
import smtplib
import smtplib as smtplib_r
import urllib
from http.client import (
    HTTPConnection,
    HTTPConnection as HTTPConnection_r,
    HTTPSConnection,
    HTTPSConnection as HTTPSConnection_r,
)
from smtplib import SMTP, SMTP as SMTP_r
from urllib.request import urlopen, urlopen as urlopen_r

import requests
import serial
import serial as serial_r
import suds.client
from requests import (
    delete,
    delete as delete_r,
    get,
    get as get_r,
    head,
    head as head_r,
    options,
    options as options_r,
    patch,
    patch as patch_r,
    post,
    post as post_r,
    put,
    put as put_r,
    request,
    request as request_r,
)
from serial import Serial, Serial as Serial_r
from suds.client import Client, Client as Client_r

# requests without timeout
requests.delete("http://localhost")  # [missing-timeout]
requests.get("http://localhost")  # [missing-timeout]
requests.head("http://localhost")  # [missing-timeout]
requests.options("http://localhost")  # [missing-timeout]
requests.patch("http://localhost")  # [missing-timeout]
requests.post("http://localhost")  # [missing-timeout]
requests.put("http://localhost")  # [missing-timeout]
requests.request("call", "http://localhost")  # [missing-timeout]

delete_r("http://localhost")  # [missing-timeout]
get_r("http://localhost")  # [missing-timeout]
head_r("http://localhost")  # [missing-timeout]
options_r("http://localhost")  # [missing-timeout]
patch_r("http://localhost")  # [missing-timeout]
post_r("http://localhost")  # [missing-timeout]
put_r("http://localhost")  # [missing-timeout]
request_r("call", "http://localhost")  # [missing-timeout]

delete("http://localhost")  # [missing-timeout]
get("http://localhost")  # [missing-timeout]
head("http://localhost")  # [missing-timeout]
options("http://localhost")  # [missing-timeout]
patch("http://localhost")  # [missing-timeout]
post("http://localhost")  # [missing-timeout]
put("http://localhost")  # [missing-timeout]
request("call", "http://localhost")  # [missing-timeout]

# requests valid cases
requests.delete("http://localhost", timeout=10)
requests.get("http://localhost", timeout=10)
requests.head("http://localhost", timeout=10)
requests.options("http://localhost", timeout=10)
requests.patch("http://localhost", timeout=10)
requests.post("http://localhost", timeout=10)
requests.put("http://localhost", timeout=10)
requests.request("call", "http://localhost", timeout=10)

delete_r("http://localhost", timeout=10)
get_r("http://localhost", timeout=10)
head_r("http://localhost", timeout=10)
options_r("http://localhost", timeout=10)
patch_r("http://localhost", timeout=10)
post_r("http://localhost", timeout=10)
put_r("http://localhost", timeout=10)
request_r("call", "http://localhost", timeout=10)

delete("http://localhost", timeout=10)
get("http://localhost", timeout=10)
head("http://localhost", timeout=10)
options("http://localhost", timeout=10)
patch("http://localhost", timeout=10)
post("http://localhost", timeout=10)
put("http://localhost", timeout=10)
request("call", "http://localhost", timeout=10)

# urllib without timeout
urllib.request.urlopen("http://localhost")  # [missing-timeout]
urlopen("http://localhost")  # [missing-timeout]
urlopen_r("http://localhost")  # [missing-timeout]

# urllib valid cases
urllib.request.urlopen("http://localhost", timeout=10)
urlopen("http://localhost", timeout=10)
urlopen_r("http://localhost", timeout=10)

# suds without timeout
suds.client.Client("http://localhost")  # [missing-timeout]
Client("http://localhost")  # [missing-timeout]
Client_r("http://localhost")  # [missing-timeout]

# suds valid cases
suds.client.Client("http://localhost", timeout=10)
Client("http://localhost", timeout=10)
Client_r("http://localhost", timeout=10)

# http.client without timeout
http.client.HTTPConnection("http://localhost")  # [missing-timeout]
http.client.HTTPSConnection("http://localhost")  # [missing-timeout]
HTTPConnection("http://localhost")  # [missing-timeout]
HTTPSConnection("http://localhost")  # [missing-timeout]
HTTPConnection_r("http://localhost")  # [missing-timeout]
HTTPSConnection_r("http://localhost")  # [missing-timeout]

# http.client valid cases
http.client.HTTPConnection("http://localhost", timeout=10)
http.client.HTTPSConnection("http://localhost", timeout=10)
HTTPConnection("http://localhost", timeout=10)
HTTPSConnection("http://localhost", timeout=10)
HTTPConnection_r("http://localhost", timeout=10)
HTTPSConnection_r("http://localhost", timeout=10)

# smtplib without timeout
smtplib.SMTP("http://localhost")  # [missing-timeout]
smtplib_r.SMTP("http://localhost")  # [missing-timeout]
SMTP("http://localhost")  # [missing-timeout]
SMTP_r("http://localhost")  # [missing-timeout]

# smtplib valid cases
smtplib.SMTP("http://localhost", timeout=10)
smtplib_r.SMTP("http://localhost", timeout=10)
SMTP("http://localhost", timeout=10)
SMTP_r("http://localhost", timeout=10)

# Serial without timeout
serial.Serial("/dev/ttyS1")  # [missing-timeout]
serial_r.Serial("/dev/ttyS1")  # [missing-timeout]
Serial("/dev/ttyS1")  # [missing-timeout]
Serial_r("/dev/ttyS1")  # [missing-timeout]

# serial valid cases
serial.Serial("/dev/ttyS1", timeout=10)
serial_r.Serial("/dev/ttyS1", timeout=10)
Serial("/dev/ttyS1", timeout=10)
Serial_r("/dev/ttyS1", timeout=10)
