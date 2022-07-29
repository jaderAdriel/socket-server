
def __init__(request):
    response = ''
    try:
        url = formatRequest(request)
        html = url_pattern[url]
        html = htmlFilteToString(html)
        contentLength = len(html.encode())
        response = f'HTTP/1.1 200 OK\r\n\
Content-Type: text/html\r\n\
Content-Length: {contentLength}\r\n\
\r\n\
{html}\r\n'

    except:
        response = 'HTTP/1.1 504\r\n'

    return response
    


def formatRequest(request):
    request = request.split('\n')
    for i, colon in enumerate(request):
        request[i] = colon.split(' ')
    return request[0][1]



def htmlFilteToString(path):
    html_as_string = ''
    with open(path, 'r') as file:
        html_as_string = file.read()
    return html_as_string


url_pattern = {
    '/pag-1/' : 'pag-1.html',
    '/pag-2/' : 'pag-2.html',
}

