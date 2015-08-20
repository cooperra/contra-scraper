from pymongo import MongoClient
import index
import source
import urllib

client = MongoClient()

db = client['contra-scraper']

def compare_index(new_index_data):
    def deep_eq(a, b):
        # this ignoring is no longer necessary because _id will never be present
        #
        # ignore _id because we don't care about it
        # we compare copies, first removing _id from both
        a_copy, b_copy = a.copy(), b.copy()
        try:
            del a_copy["_id"]
        except KeyError:
            pass
        try:
            del b_copy["_id"]
        except KeyError:
            pass
        return a_copy == b_copy
    def join_by_key(key_name, index_a, index_b):
        # The thing to remember is that index_a and b are 
        # more like lists of sources than actual indexes
        def index_by_key(index):
            new_ind = {}
            for source in index:
                new_ind[source[key_name]] = source
            return new_ind
        ind_a = index_by_key(index_a)
        ind_b = index_by_key(index_b)
        joined = {}
        for key in set(ind_a):
            if key in ind_b:
                joined[key] = (ind_a.pop(key), ind_b.pop(key))
        # both, a only, b only
        return (joined, ind_a, ind_b)
    
    stored_index_data = ( s["index"] for s in db.sources.find({}, ["index"]) )
    (joined, new, deleted) = join_by_key("code", new_index_data, stored_index_data)
    new_or_changed = new.values()
    deleted = deleted.values()
    
    # add all modified items to new_or_changed set
    for code in joined:
        if not deep_eq(joined[code][0], joined[code][1]):
            new_or_changed.add(joined[code][0])
    
    return (new_or_changed, deleted)

DOWNLOAD_DIR = "downloads"
BASE_URL = "http://www.ibiblio.org/contradance/index/"
INDEX_URL = "index.html"

def _download_file(url, dest_dir, dest_name):
    if dest_dir==None:
        dest_dir = DOWNLOAD_DIR
    dest_path = dest_dir+"/"+dest_name
    urllib.request.urlretrieve(url, dest_path)
    return dest_path

def download_index(dest_dir=None, dest_name="index.html"):
    return _download_file(BASE_URL+INDEX_URL, det_dir, dest_name)

def download_source(source_index_entry, dest_dir=None, dest_name=None):
    if dest_name==None:
        dest_name = "source_"+ source_index_entry["code"]+".txt"
    if dest_dir==None:
        dest_dir = DOWNLOAD_DIR+"/"+"sources"
    source_url = urllib.request.urljoin(BASE_URL, source_index_entry["code_link"], allow_fragments=False)
    return _download_file(source_url, dest_dir, dest_name)

def sync_index(from_file=None):
    if from_file==None:
        from_file = download_index()
    
    index_file = open(from_file, 'r', encoding="Latin-1")
    index_data = index.load(index_file)
    
    changed_or_new_sources, deleted_sources = compare_index(index_data)

    for s in changed_or_new_sources:
        sync_source(s)

    # index is saved in sync_sources;
    # no need to explicitly save here
    
    # delete removed sources
    # TODO backup also?
    if len(deleted_sources) > 0:
        bulkOp = db.sources.initialize_unordered_bulk_op()
        for s in deleted_sources:
            bulkOp.find({"index.code": deleted_source["code"]}).remove()
            #bulkOp.find({"_id": deleted_source["_id"]}).remove()
        bulk_result = bulkOp.execute()
        print(bulk_result)

def sync_source(source_index_data, use_cached=True):
    if use_cached:
        filename = "samples/source/"+source_index_data["code"]+".txt"
    else:
        filename = download_source(source_index_data)
    #source_detail_file = open(filename, 'r')
    source_detail_data = source.load_file(filename)
    for d in source_detail_data['dances']:
        sync_dance(source_detail_data, d)
    query_result = db.sources.update({"index.code": source_index_data["code"]},
                                     {"index": source_index_data,
                                      "detail": source_detail_data},
                                     upsert=True)
    print(source_index_data["code"], query_result)

def sync_dance(source_detail_data, dance):
    pass

def test():
    sync_index(from_file="samples/index/Michael Dyck's Contradance Index_ Sources.html")

test()

for a in db.sources.find():
    print(a["index"]["code"])


