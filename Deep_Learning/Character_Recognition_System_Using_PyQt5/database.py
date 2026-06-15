import sqlite3
import os

DB_DIR = "database"
DB_PATH = os.path.join(DB_DIR, "predictions.db")

def init_db():
    """Initializes the database and creates the history table if it doesn't exist."""
    if not os.path.exists(DB_DIR):
        os.makedirs(DB_DIR)
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            character TEXT,
            confidence REAL
        )
    ''')
    conn.commit()
    conn.close()

def log_prediction(character, confidence):
    """Logs a new prediction result into the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO history (character, confidence)
        VALUES (?, ?)
    ''', (character, float(confidence)))
    conn.commit()
    conn.close()