from app.db.init import init_db
from app.ingestion.consumer import consume_events


def main() -> None:
    init_db()
    consume_events()


if __name__ == "__main__":
    main()
