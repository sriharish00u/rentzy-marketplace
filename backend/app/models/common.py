from bson import ObjectId
from pydantic import BaseModel

class PyObjectId(str):
    @classmethod
    def __get_pydantic_core_schema__(cls, source, handler):
        from pydantic_core import core_schema
        return core_schema.no_info_after_validator_function(cls.validate, core_schema.str_schema())

    @classmethod
    def validate(cls, v):
        if isinstance(v, ObjectId):
            return str(v)
        if isinstance(v, str) and ObjectId.is_valid(v):
            return v
        raise ValueError("Invalid ObjectId")


def serialize_doc(doc: dict | None):
    if not doc:
        return doc
    doc = dict(doc)
    if "_id" in doc:
        doc["id"] = str(doc.pop("_id"))
    for k, v in list(doc.items()):
        if isinstance(v, ObjectId):
            doc[k] = str(v)
        elif isinstance(v, list):
            doc[k] = [str(i) if isinstance(i, ObjectId) else serialize_doc(i) if isinstance(i, dict) else i for i in v]
        elif isinstance(v, dict):
            doc[k] = serialize_doc(v)
    return doc
