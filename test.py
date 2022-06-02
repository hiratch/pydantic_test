from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []

    def __init__(self, id: int, name: str, signup_ts: Optional[datetime], friends: List[int]):
        super().__init__(id=id, name=name, signup_ts=signup_ts, friends=friends)
        self.id = id
        self.signup_ts = signup_ts
        self.friends = friends

external_data = {
    'id': 123,
    'name': 'Takashi',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, 3]
}

user = User(**external_data)
print(user.id)
print(repr(user.signup_ts))
print(user.friends)
print(user.dict())

