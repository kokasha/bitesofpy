#url = 'https://www.amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/?keywords=war+of+art'
def generate_affiliation_link(url):
    url = url.split('/')
    url = [x for x in url if x not in '']
    return 'http:' + '//' + 'www.amazon.com' + '/' + url[3] + '/' + url[4] + '/' + '?tag=pyb0f-20'

# generate_affiliation_link(url)