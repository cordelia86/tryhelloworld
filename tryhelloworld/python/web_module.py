def get_web(url):
    import urllib.request as request

    response = request.urlopen(url)
    data = response.read()
    decoded = data.decode('utf-8')
    return decoded


url = input('Enter any url: ')
content = get_web(url)
print(content)
