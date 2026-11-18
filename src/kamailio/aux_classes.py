import redis

class RedisDB:

    def __init__(self, host):
        self.client = redis.Redis(
            host=host,
            port=6379,
            db=0,
            decode_responses=True,
            socket_connect_timeout=1,
            socket_timeout=1
        )

    def set(self, key, value):
        return self.client.set(key, value)

    def get(self, key):
        return self.client.get(key)

    def seti(self, key, value):
        return int(self.client.set(key, value))

    def geti(self, key):
        return int(self.client.get(key))
    
    def delete(self, key):
        return self.client.delete(key)

    def exists(self, key):
        return self.client.exists(key)

    def close(self):
        self.client.close()