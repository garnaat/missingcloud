import json

def generate_html():
    """
    Just a simple function to generate a chunk of HTML that I can
    paste into my blog entry detailing this same info.  Makes it
    easier to keep things up to date.  Automating this completely
    would be better but that will have to wait till I have time
    to investigate blogger api's.
    """
    fp = open('aws.json')
    data = json.load(fp)
    fp.close()
    
    html = ''
    keys = data['services'].keys()
    keys.sort()
    for service in keys:
        value = data['services'][service]
        html += '<b>%s</b>\n' % service
        html += '  <ul>\n'
        for region in value['regions']:
            html += '    <li>%s: %s</li>\n' % (region['name'],
                                               region['endpoint'])
        html += '  </ul>\n'
    return html
    
