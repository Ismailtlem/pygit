import hashlib

# from _typeshed import ReadableBuffer


def hash_git_object(data: bytes) -> str:
    oid = hashlib.sha1(data).hexdigest()
    print("oiid", oid)
    with open(f".git/objects/{oid}", "wb") as out:
        out.write(data)
    return oid
