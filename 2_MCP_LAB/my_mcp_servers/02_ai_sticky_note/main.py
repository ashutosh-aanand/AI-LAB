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


# Read all notes
@mcp.tool()
def read_notes() -> str:
    """
    Read and return all notes from the notes file.

    Returns:
        str: all notes as a single string separated by line breaks.
        If no notes exits, a default message is returned.
    """
    ensure_file()

    with open(NOTES_FILE, "r") as f:
        notes = f.read().strip()
    return notes or "No notes yet."


# Return last or latest note added
@mcp.resource("notes://latest")
def get_latest_note() -> str:
    """
    Read and return the latest or last note

    Returns:
        str: the latest or last note as a string
        If no notes exits, a default message is returned.
    """
    
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        notes_lines = f.readlines()
        latest_note = notes_lines[-1].strip() if notes_lines else "No notes"
    return latest_note


# Generate a notes summarisation prompt
@mcp.prompt()
def notes_summary_prompt() -> str:
    """
    Generate a prompt asking the AI to summarise all current notes

    Returns:
        str: A prompt string that includes all notes and asks for a summary.
            If no notes exits, a message will be shown indicating that.
    """

    ensure_file()
    with open(NOTES_FILE, "r") as f:
        notes = f.read().strip()
    if not notes:
        return "There are no notes yet."
    
    return f"Summarise the notes : {notes}"

