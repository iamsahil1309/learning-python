# mixing pydantic and typing 
from pydantic import BaseModel
from typing import List, Dict, Optional

class cart(BaseModel):
    user_id : int
    items : List[str]
    quantities : Dict[str, int]

class BlogPost(BaseModel):
    title : str
    comment : str
    image_url : Optional[str] = None         #this is optional and default value is none when some blog post use images or not so we use optional