from fastmcp import FastMCP

from typing import Optional
from data_types import McpResponse

from client import http_client

from dotenv import load_dotenv
import os

load_dotenv()
MAINFRAME_API = os.getenv("MAINFRAME_API")

mcp = FastMCP("My MCP Server")

@mcp.tool(
    name="GetMember",
    description="Retrieve a member from the mainframe.",
)
async def get_member(member: str , library: str, output_path: Optional[str]) -> McpResponse:
    """
    Fetch a member from the mainframe and save it to the specified output path.
    """
    url = f"{MAINFRAME_API}/get-member"
    
    response =await http_client.get(
        url, 
        json={
            "member": member,
            "library": library,
            "outputPath": output_path
        }
    )
    
    return McpResponse(
        success=response.get("success"),
        message=response.get("message"),
    )

@mcp.tool(
    name="GetDataset",
    description="Get a dataset from the mainframe.",
)
async def get_dataset(dataset_name: str, output_path: Optional[str]) -> McpResponse:
    """
    List members in a specified library on the mainframe and save the list to the specified output path.
    """
    url = f"{MAINFRAME_API}/get-dataset"
    
    response = await http_client.get(
        url, 
        json={
            "datasetName": dataset_name,
            "outputPath": output_path
        }
    )
    
    return McpResponse(
        success=response.get("success"),
        message=response.get("message"),
    )

if __name__ == "__main__":
    mcp.run()