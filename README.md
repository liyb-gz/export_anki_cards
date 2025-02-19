# Anki Card Extractor

## Objective

Export the learning, learned and about to learn cards from Anki, and fill them in a prompt, and send it to a LLM. Ask the LLM to generate a passage that is suitable for your current language level.

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

4. Run the extractor:

```bash
python main.py
```

This will generate CSV files containing your Anki cards based on your queries.
