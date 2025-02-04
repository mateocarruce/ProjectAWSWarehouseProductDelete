from pydantic import BaseModel
from typing import Optional

class ProductDeleteSchema(BaseModel):
    id_producto: int
