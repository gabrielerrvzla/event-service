from pydantic import BaseModel


class MessageSchema(BaseModel):
    id: str
    topic_callback: str
    content: str
