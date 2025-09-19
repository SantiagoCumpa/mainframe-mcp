from pydantic import BaseModel

class ApiResponse(BaseModel):
    success: bool
    type: str
    message: str
    exitCode: int
    
    def get(self, key: str):    
        return getattr(self, f"{key}")
    
class McpResponse(BaseModel):
    success: bool
    message: str
        
    def get(self, key: str):
        return getattr(self, f"{key}")
