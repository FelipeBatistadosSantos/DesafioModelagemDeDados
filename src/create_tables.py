import sqlite3

def create_tables():
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()
    
    with open('sql/schema.sql', 'r') as f:
        schema = f.read()
    
    c.executescript(schema)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
