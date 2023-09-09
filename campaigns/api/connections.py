import redis


def get_redis_connection():
    """Creates a connection to a
    Redis database"""
    conn = redis.Redis('redis', 1)
    try:
        conn.ping()
    except:
        return False
    else:
        return conn
