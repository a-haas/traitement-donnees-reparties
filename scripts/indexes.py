from services import elasticsearch


def create():
    elasticsearch.config_es()


def reset():
    elasticsearch.reset_index()


def optimise():
    elasticsearch.optimise()