import urllib, json

brands = [
    {
        'name': 'Stop & Shop',
        'id': '423801622'
    },
    {
        'name': 'Giant Food Stores',
        'id': '491014869'
    },
    {
        'name': 'Giant Landover',
        'id': '423806284'
    },
    {
        'name': 'MARTINS',
        'id': '490731809'
    }
]

for brand in brands:
    print brand['name']
    print '------------------------'
    url = "https://itunes.apple.com/us/rss/customerreviews/id=" + brand['id'] + "/json"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    ratings = {}
    versions = []
    
    for entry in data['feed']['entry']:
     if entry.has_key('im:rating'):
            version = entry['im:version']['label']
            versions.append(version)
            rating = {
                'rating': entry['im:rating']['label'],
                'title': entry['title']['label'],
                'content': entry['content']['label'],
                'id': entry['id']['label']
            }
            if ratings.has_key(version):
             ratings[version].append(rating)
            else:
                ratings[version] = [ rating ]

    versions = list(set(versions))
    for version in versions:
        print 'Version: ' + version
        print 'Number of reviews: ' + str(len(ratings[version]))
        average = sum(float(r['rating']) for r in ratings[version]) / len(ratings[version])
        print 'Average: ' + str(average)
        print ''
