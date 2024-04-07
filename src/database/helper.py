def create_schema_instances(data, schema, attr):
    instances = []
    if data:
        for id in data:
            instance = schema(**{attr: id})
            instances.append(instance)
    return instances
