# Anki Card Extractor

## Objective

Export the specific notes from Anki programatically. You can specify the conditions and the fields you want to export.

## Setup

1. Create a virtual environment:

```bash
python -m venv venv

# On Windows
.\venv\Scripts\activate

# On Unix/macOS
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with your Anki path:

```
ANKI_PATH=/path/to/your/anki/collection.anki2
```

4. Create a `queries.py` file in the root directory with your queries. A sample file is provided in `sample.queries.py`.

5. Run the extractor:

```bash
python main.py
```

This will generate CSV files containing your Anki cards based on your queries.
