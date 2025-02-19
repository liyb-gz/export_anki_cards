from typing import TypedDict, List, Optional

class Query(TypedDict):
    query_string: str
    fields: List[str]
    output_file: str
    limit: Optional[int]
    order: Optional[str]

queries: List[Query] = [
    # Get vocabulary cards that are currently in "learn" status
    # Fields: Front = vocabulary word, Back = definition/translation
    # Output file: vocabulary_learning.csv
    {
        "query_string": 'deck:"Language Vocabulary" is:learn',
        "fields": ["Front", "Back"], 
        "output_file": "vocabulary_learning.csv"
    },

    # Get grammar example sentences that are currently in "learn" status
    # Fields: Sentence = example sentence, Translation = English translation
    # Output file: grammar_learning.csv
    {
        "query_string": 'deck:"Language Grammar" is:learn',
        "fields": ["Sentence", "Translation"],
        "output_file": "grammar_learning.csv"
    },

    # Get vocabulary cards that have been learned, the card status is "review"
    # Fields: Front = vocabulary word, Back = definition/translation
    # Output file: vocabulary_learned.csv
    {
        "query_string": 'deck:"Language Vocabulary" is:review',
        "fields": ["Front", "Back"],
        "output_file": "vocabulary_learned.csv"
    },

    # Get grammar sentences that have been learned, the card status is "review"
    # Fields: Sentence = example sentence, Translation = English translation
    # Output file: grammar_learned.csv
    {
        "query_string": 'deck:"Language Grammar" is:review',
        "fields": ["Sentence", "Translation"], 
        "output_file": "grammar_learned.csv"
    },

    # Get the next 50 new vocabulary cards to learn, ordered by due date
    # Fields: Front = vocabulary word, Back = definition/translation
    # Output file: vocabulary_new.csv
    {
        "query_string": 'deck:"Language Vocabulary" is:new',
        "fields": ["Front", "Back"],
        "output_file": "vocabulary_new.csv",
        "limit": 50,
        "order": "c.due asc"
    },

    # Get the next 50 new grammar sentences to learn from the card type "Grammar",
    # ordered by due date
    # Fields: Sentence = example sentence, Translation = English translation
    # Output file: grammar_new.csv
    {
        "query_string": 'deck:"Language Grammar" is:new card:grammar',
        "fields": ["Sentence", "Translation"],
        "output_file": "grammar_new.csv",
        "limit": 50,
        "order": "c.due asc"
    }
]
