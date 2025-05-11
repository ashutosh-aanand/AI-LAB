from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("NotesMan") # naming my notes manager mcp server

# store notes in a txt file
NOTES_FILE = os.path.join(os.path.dirname(__file__), "notes.txt")

def ensure_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            f.write("")

# Add a new note
@mcp.tool()
def add_note(note: str) -> str:
    
    """
    Append a new note to the notes file
    args:
        note (str): the note to be added.
    return:
        str: confirmation message indicating that the note was saved.
    """

    ensure_file()
    
    with open(NOTES_FILE, "a") as f:
        f.write(note + "\n")
    
    return "note saved successfully !"

@mcp.tool()
def read_notes() -> str:
    return ""

@mcp.resource("notes://latest")
def get_latest_note() -> str:
    return ""

@mcp.prompt()
def note_summary_prompt() -> str:
    return ""
