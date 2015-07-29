import index
import source
import os
import urllib

indexfile = open("samples/index/Michael Dyck's Contradance Index_ Sources.html", encoding="Latin-1")
index_baseurl = "http://www.ibiblio.org/contradance/index/"

indexdata = index.load(indexfile)

set_to_download = set()

for row in indexdata:
    code_url = urllib.request.urljoin(index_baseurl, row['code_link'], allow_fragments=False)
    first_entered = row['date first entered']
    last_revised = row['date last revised']
    set_to_download.add(code_url)

for url in set_to_download:
    filename = os.path.basename(urllib.request.urlparse(url).path)
    urllib.request.urlretrieve(url, "samples/source/"+filename)
    
