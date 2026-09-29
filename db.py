# db.py
import sqlite3
from pathlib import Path

DB_PATH = Path("telemedicine.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS cases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_name TEXT,
        age INTEGER,
        notes TEXT,
        filename TEXT,
        prediction TEXT,
        score REAL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    conn.commit()
    conn.close()

def insert_case(patient_name, age, notes, filename, prediction, score):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
    INSERT INTO cases (patient_name, age, notes, filename, prediction, score)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (patient_name, age, notes, filename, prediction, float(score)))
    conn.commit()
    conn.close()

def list_cases(limit=100):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT id, patient_name, age, notes, filename, prediction, score, timestamp FROM cases ORDER BY timestamp DESC LIMIT ?', (limit,))
    rows = c.fetchall()
    conn.close()
    return rows

