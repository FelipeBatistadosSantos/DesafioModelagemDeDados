import sqlite3

def run_queries():
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()

    with open('sql/queries.sql', 'r') as f:
        queries = f.read().strip().split('\n\n')

    for i, query in enumerate(queries):
        query = query.strip()
        if query:
            filename = f"query_results_{i + 1}.txt"

            with open(filename, 'w') as f:
                f.write("Consulta:\n")
                f.write(query + "\n")
                f.write("-" * 30 + "\n")
                try:
                    for row in c.execute(query):
                        f.write(f"{row}\n")
                except sqlite3.Error as e:
                    f.write(f"Erro: {e}\n")
                f.write("\n")

    conn.close()



if __name__ == "__main__":
    run_queries()
