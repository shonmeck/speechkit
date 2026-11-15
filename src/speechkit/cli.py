import argparse
from pathlib import Path
import duckdb
from speechkit.config import DB_PATH
from speechkit.loader import load_speeches
from speechkit.store import create_schema, insert_speeches, GROUPINGS, get_stats

def cmd_ingest(args):
    Path(args.db).parent.mkdir(parents=True, exist_ok=True)
    with duckdb.connect(args.db) as con:
        create_schema(con)
        n = insert_speeches(con, load_speeches(args.folder))
        print(n, "speeches loaded")

def cmd_stats(args):
    with duckdb.connect(args.db, read_only=True) as con:
        rows = get_stats(con, by=args.by, start=args.start, end=args.end, country=args.country)
        print(f"{args.by:<10}{'speeches':>10}{'countries':>10}{'words':>12}")
        for key, speeches, countries, words in rows:
            print(f"{key:<10}{speeches:>10}{countries:>10}{words:>12,}")

def main():
    parser = argparse.ArgumentParser(prog="speechkit")
    parser.add_argument("--db", default=DB_PATH, help="Path to the database file")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("stats", help="Count speeches, countries, and words")
    p.add_argument("--by", choices=list(GROUPINGS), default="year")
    p.add_argument("--from", dest="start", type=int)
    p.add_argument("--to", dest="end", type=int)
    p.add_argument("--country")
    p.set_defaults(func=cmd_stats)

    p = sub.add_parser("ingest", help="Move data into DuckDB database")
    p.add_argument("folder")
    p.set_defaults(func=cmd_ingest)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()