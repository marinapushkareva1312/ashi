import os
import json
from datetime import datetime

def test_journal_saves():
    # Test that save_entry creates a journal file
    from app import save_entry
    save_entry("test text", "test analysis")
    assert os.path.exists("journal.json"), "journal.json was not created"
    print("✓ test_journal_saves passed")

def test_journal_has_date():
    # Test that entry contains date
    with open("journal.json", "r") as f:
        data = json.load(f)
    last_entry = data[-1]
    assert "date" in last_entry, "No date in entry"
    print("✓ test_journal_has_date passed")

def test_journal_has_text():
    # Test that entry contains text
    with open("journal.json", "r") as f:
        data = json.load(f)
    last_entry = data[-1]
    assert "said" in last_entry, "No text in entry"
    print("✓ test_journal_has_text passed")

def test_journal_not_empty():
    # Test that journal has at least one entry
    with open("journal.json", "r") as f:
        data = json.load(f)
    assert len(data) > 0, "Journal is empty"
    print("✓ test_journal_not_empty passed")

def test_entry_has_analysis():
    # Test that entry contains analysis
    with open("journal.json", "r") as f:
        data = json.load(f)
    last_entry = data[-1]
    assert "analysis" in last_entry, "No analysis in entry"
    print("✓ test_entry_has_analysis passed")

def test_date_format():
    # Test that date is in correct format
    with open("journal.json", "r") as f:
        data = json.load(f)
    last_entry = data[-1]
    date_str = last_entry["date"]
    datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    print("✓ test_date_format passed")    

if __name__ == "__main__":
    test_journal_saves()
    test_journal_has_date()
    test_journal_has_text()
    test_journal_not_empty()
    test_entry_has_analysis()
    test_date_format()
    print("\nAll tests passed! ✓")