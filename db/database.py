import sqlite3
from pathlib import Path

DB_NAME = 'db.sqlite3'
TABLE_NAME = 'card_flags'

ROOT_DIR = Path(__file__).parent
DB_FILE = ROOT_DIR / DB_NAME


def connect():
    return sqlite3.connect(DB_FILE)

def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bandeira TEXT NOT NULL,
            prefixos TEXT NOT NULL,
            comprimentos TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def populate_table():
    data = [
        ('Visa', '4', '13, 16, 19'),
        ('MasterCard', '51-55, 2221-2720', '16'),
        ('American Express', '34, 37', '15'),
        ('Discover', '6011, 622126-622925, 644-649, 65', '16'),
        ('Diners Club', '300-305, 36, 38', '14, 16, 19'),
        ('JCB', '3528-3589', '16'),
        ('Hipercard', '38, 6062', '13, 16, 19'),
        ('Elo', '4011, 4312, 4387, 4576, 6277, 6362', '16'),
        ('Aura', '50', '16'),
        ('Sodexo', '606282', '13, 16'),
        ('Enroute', '2014, 2149', '15'),
        ('Voyager', '8699', '15'),
        ('Visa Electron', '4026, 4175, 4508, 4844, 4913, 4917', '13-19')
    ]
    
    conn = connect()
    cursor = conn.cursor()
    cursor.executemany(f'''
        INSERT INTO {TABLE_NAME} (bandeira, prefixos, comprimentos)
        VALUES (?, ?, ?)
    ''', data)
    conn.commit()
    conn.close()

def fetch_card_flags_from_db():
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT bandeira, prefixos, comprimentos FROM {TABLE_NAME}")
    rows = cursor.fetchall()
    
    card_flags = {}
    for row in rows:
        bandeira, prefixos, comprimentos = row
        card_flags[bandeira] = {
            "prefixes": prefixos,
            "lengths": comprimentos.replace(" ", "")
        }
    
    conn.close()
    return card_flags

def insert_card_flag(bandeira, prefixos, comprimentos):
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute(f'''
        INSERT INTO {TABLE_NAME} (bandeira, prefixos, comprimentos)
        VALUES (?, ?, ?)
    ''', (bandeira, prefixos, comprimentos))
    
    conn.commit()
    card_id = cursor.lastrowid
    conn.close()
    
    return card_id

#gere uma função para limpar toda a tabela existente
def clear_table():
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute(f"DELETE FROM {TABLE_NAME}")
    conn.commit()
    conn.close()

def update_card_flag(bandeira, prefixos, comprimentos):
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute(f'''
        UPDATE {TABLE_NAME}
        SET prefixos = ?, comprimentos = ?
        WHERE bandeira = ?
    ''', (prefixos, comprimentos, bandeira))
    
    conn.commit()
    conn.close()



if __name__ == "__main__":
    clear_table()
    populate_table()