# Mainframe MCP Server

A Model Context Protocol (MCP) server that provides tools for interacting with mainframe systems. This server enables AI assistants to retrieve members and datasets from mainframe environments through a standardized API.

## Features

- **Get Member**: Retrieve specific members from mainframe libraries
- **Get Dataset**: Fetch datasets from the mainframe system

## Installation

> [!IMPORTANT]
> You have to run mainframe api project before using this MCP server.
> See [Mainframe API](https://github.com/SantiagoCumpa/mainframe-api.git) for  configuration.

1. Clone this repository:
```bash
git clone <repository-url>
cd mainframe-mcp
```

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your `.env` file with the required environment variables.
```bash
# Create a .env file with your mainframe API endpoint
MAINFRAME_API=https://your-mainframe-api-endpoint.com
```

## Configuration

### MCP Client Configuration

Add the server configuration to your MCP client configuration file:

```json
{
  "servers": {
    "<mcp-name>": {
      "type": "stdio",
      "command": "/path/to/bin/fastmcp",
      "args": [
        "run", 
        "/path/to/mainframe-mcp/main.py"
      ]
    }
  }
}
```

| Configuration                    | Description                        |
|----------------------------------|------------------------------------|
| `/path/to/mainframe-mcp/main.py` | Path to your `main.py`             |
| `/path/to/bin/fastmcp`           | Path to your `fastmcp` executable  |

## Usage

### Available Tools

#### GetMember

Retrieve a specific member from a mainframe library.

**Parameters:**
- `member` (string): Name of the member to retrieve
- `library` (string): Library containing the member
- `output_path` (string, optional): Path where the member should be saved

#### GetDataset

Fetch a dataset from the mainframe system.

**Parameters:**
- `dataset_name` (string): Name of the dataset to retrieve
- `output_path` (string, optional): Path where the dataset should be saved

## Project Structure
```
mainframe-mcp/
├── main.py              # MCP server implementation
├── client.py            # HTTP client for API communication
├── data_types.py        # Pydantic models for data validation
├── requirements.txt     # Python dependencies
├── mcp.example.json     # Example MCP configuration
├── instructions.md      # Mainframe structure documentation
└── README.md           # This file
```