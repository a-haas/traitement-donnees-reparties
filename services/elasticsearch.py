from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from elasticsearch.helpers import scan


# idefix = index
IDEFIX = "tdr"
TIMEOUT=30


def config_es():
    # connect to elasticsearch
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    # create the idefix in the db and ignore it if already exists
    es.indices.create(index=IDEFIX, ignore=400)
    return es


def reset_index():
    es = config_es()
    es.indices.delete(index=IDEFIX, ignore=[400, 404])


def create(doc_type, body):
    es = config_es()
    return es.index(index=IDEFIX, doc_type=doc_type, body=body)


def bulk_insert(doc_type, ljsons):
    es = config_es()

    # tmp yield function for bulk (l is the list of jsons)
    def f(l):
        i = 1
        for j in l:
            data = {'_op_type': 'create',
                    '_index': IDEFIX,
                    '_type': doc_type,
                    '_id': i,
                    '_source': j}
            i += 1
            yield (data)
    return bulk(es, f(ljsons))


def search(doc_type, body):
    es = config_es()
    result = es.search(index=IDEFIX, doc_type=doc_type, body=body, request_timeout=TIMEOUT)
    if result.get('hits') is not None and result['hits'].get('hits') is not None:
        return result['hits']['hits']
    else:
        return {}


def delete_by_id(doc_type, id):
    es = config_es()
    es.delete(index=IDEFIX, doc_type=doc_type, id=id, request_timeout=30)


def delete_by_query(doc_type, query):
    es = config_es()
    es.delete_by_query(index=IDEFIX, doc_type=doc_type, body={"query": query}, request_timeout=30)


def count(doc_type, query):
    es = config_es()
    c = es.count(index=IDEFIX, doc_type=doc_type, body={"query": query})
    # now we can do searches.
    print("Ok. I've got an index of {0} documents. Let's do some searches...".format(c['count']))
    return c


def retrieve_all(doc_type, query):
    es = config_es()
    res = scan(
        es,
        query={"query": query},
        index=IDEFIX,
        doc_type=doc_type
    )
    res = list(res)
    return res


def optimise():
    es = config_es()
    es.indices.forcemerge()