from anki.collection import Collection
import os
from dotenv import load_dotenv
from typing import List, Dict
import csv
from pathlib import Path

def get_notes_with_fields(col: Collection, search_query: str, fields: List[str] | None = None, limit=None, order=False) -> List[Dict[str, str]]:
    """
    Get notes matching the search query and return specified fields.
    
    Args:
        col: Anki collection object
        search_query: Anki search query string
        fields: List of field names to retrieve. If None, returns all fields.
        limit: Maximum number of results to return
        order: Whether to order the results
    
    Returns:
        List of dictionaries, each containing the requested fields
        Example: [{'Korean': '안녕', 'English': 'hello'}, {...}]
    """
    results = []
    card_ids = col.find_cards(search_query, order)
    
    # Apply limit if specified
    if limit is not None:
        card_ids = card_ids[:limit]
    
    for card_id in card_ids:
        card = col.get_card(card_id)
        note = card.note()
        
        # Create a dictionary for this note's fields
        note_fields = {}
        
        # If no fields specified, get all fields
        fields_to_get = fields if fields is not None else note.keys()
        
        for field in fields_to_get:
            try:
                note_fields[field] = note[field]
            except KeyError:
                note_fields[field] = None  # or '' if you prefer empty string
        
        results.append(note_fields)
    
    return results

def convert_notes_to_csv(notes: List[Dict[str, str]], output_file: str):
    with open(output_file, "w") as f:
        writer = csv.writer(f)
        writer.writerow(notes[0].keys())
        for note in notes:
            writer.writerow(note.values())

def export_anki_queries(col, queries_list, output_dir="output"):
    """
    Export Anki cards based on queries to CSV files in the specified output directory.
    
    Args:
        col: Anki collection object
        queries_list: List of Query objects containing search parameters
        output_dir: Directory to save CSV files (default: "output")
    """
    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    for query in queries_list:
        # Get notes based on query parameters
        notes = get_notes_with_fields(
            col,
            query["query_string"],
            query["fields"],
            query.get("limit"),
            query.get("order", False)
        )
        
        # Save to CSV in output directory
        output_path = os.path.join(output_dir, query["output_file"])
        with open(output_path, "w", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(query["fields"])  # Write header
            for note in notes:
                writer.writerow([note[field] for field in query["fields"]])
        print(f"Exported {len(notes)} notes to {output_path}")

if __name__ == "__main__":
    load_dotenv()
    col = Collection(os.getenv("ANKI_PATH"))
    
    # Load queries from queries.py
    from queries import queries
    
    # Export all queries to CSV files
    export_anki_queries(col, queries)