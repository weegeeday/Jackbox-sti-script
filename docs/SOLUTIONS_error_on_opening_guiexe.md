import pathlib
from typing import Any, Dict, List, Optional

# --- Function illustrating fix for FileNotFoundError (Line 144 Context) ---
def load_resource(file_path: str) -> Optional[Any]:
    """Safely loads a resource, handling path resolution failures."""
    resolved_path = pathlib.Path(file_path).resolve()

    if not resolved_path.exists():
        # Instead of failing and allowing the program to crash later, 
        # we log and return None or an empty safe object.
        print(f"WARNING: Resource file not found at {resolved_path}. Using default stub.")
        return {"status": "stub", "data": []}

    try:
        with open(resolved_path, 'r') as f:
            # Assuming resource loading needs to handle specific format (e.g., JSON/YAML)
            return f.read() 
    except Exception as e:
        print(f"ERROR reading file {file_path}: {e}")
        return None

# --- Function illustrating fix for KeyError (Line 242 Context) ---
def process_data_metrics(raw_data: Dict[str, Any]) -> Optional[int]:
    """Retrieves data metrics safely using .get() to prevent KeyError."""
    KEY = '4'
    
    # Instead of raw_data['4'], use .get() with a default value (e.g., 0)
    value = raw_data.get(KEY)

    if isinstance(value, int):
        return value
    else:
        print(f"WARNING: Expected key '{KEY}' to be an integer, received {type(value).__name__}. Defaulting to 0.")
        return 0

# --- Function illustrating fix for IndexError (Line 261 Context) ---
def safe_list_access(data_list: List[Any], index: int, default_val: Any = None) -> Optional[Any]:
    """Accesses list elements with boundary checking to prevent IndexError."""
    if 0 <= index < len(data_list):
        return data_list[index]
    else:
        print(f"WARNING: Attempted to access index {index} on list of size {len(data_list)}. Returning default value.")
        return default_val
