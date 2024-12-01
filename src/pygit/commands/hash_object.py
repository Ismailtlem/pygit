import hashlib

from _typeshed import ReadableBuffer


def hash_git_object(data: ReadableBuffer) -> str:
    oid = hashlib.sha1(data).hexdigest()
    with open(f".git/objects/{oid}", "wb") as out:
        out.write(data)
    return oid
