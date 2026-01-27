# mixing pydantic and typing 
from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id : int
    items : List[str]
    quantities : Dict[str, int]

class BlogPost(BaseModel):
    title : str
    comment : str
    image_url : Optional[str] = None         #this is optional and default value is none when some blog post use images or not so we use optional

cart_data = {
    "user_id" : 1234,
    "items" : ["laptop", "mouse", "keyboard"],
    "quantities" : {"laptop" : 1, "mouse" : 2, "keyboard" : 3}
}

cart  = Cart(**cart_data)