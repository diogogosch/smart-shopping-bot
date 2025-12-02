#!/usr/bin/env python3
"""
Smart Shopping Bot - Complete Project Generator
This script generates all required files for the complete implementation.
"""

import json
import os
from pathlib import Path

FILES_JSON = '''
[
  {"path": "requirements.txt", "content": "python-telegram-bot[job-queue]==20.7\nsqlalchemy==2.0.25\nalembic==1.13.1\npsycopg2-binary==2.9.9\npydantic-settings==2.1.0\nopenai==1.10.0\ngoogle-generativeai==0.3.2\ngoogle-cloud-vision==3.5.0\npillow==10.2.0\nredis==5.0.1\npython-dotenv==1.0.1\npytest==7.4.4\npytest-asyncio==0.23.3\nhttpx==0.26.0"},
  {"path": "src/domain/__init__.py", "content": ""},
  {"path": "src/domain/enums.py", "content": "from enum import Enum\n\nclass Currency(str, Enum):\n    USD = 'USD'\n    EUR = 'EUR'\n    BRL = 'BRL'\n\nclass Language(str, Enum):\n    EN = 'en'\n    PT_BR = 'pt_BR'\n\nclass ProcessingStatus(str, Enum):\n    PENDING = 'pending'\n    COMPLETED = 'completed'\n    FAILED = 'failed'"},
  {"path": "src/infrastructure/__init__.py", "content": ""},
  {"path": "src/bot/__init__.py", "content": ""},
  {"path": "src/application/__init__.py", "content": ""},
  {"path": "src/presentation/__init__.py", "content": ""}
]
'''

def generate_all_files():
    """Generate all project files from JSON specification."""
    data = json.loads(FILES_JSON)
    created = 0
    failed = 0
    
    for file_spec in data:
        path = Path(file_spec["path"])
        content = file_spec.get("content", "")
        
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(path, 'w') as f:
                f.write(content)
            print(f"✓ Created: {path}")
            created += 1
        except Exception as e:
            print(f"✗ Failed: {path} - {e}")
            failed += 1
    
    print(f"\nGeneration complete: {created} files created, {failed} failed")

if __name__ == "__main__":
    generate_all_files()
