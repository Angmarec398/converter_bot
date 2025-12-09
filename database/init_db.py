import csv
from pathlib import Path

from sqlalchemy import select, func

from database.models import Base, Motivation
from database.session import engine, SessionLocal


MOTIVATION_CSV = Path("motivation.csv")


async def _import_motivation():
    if not MOTIVATION_CSV.exists():
        return

    rows: list[Motivation] = []
    with MOTIVATION_CSV.open("r", encoding="cp1251") as f:
        reader = csv.reader(f, delimiter=";")
        next(reader, None)  # пропускаем заголовок
        for row in reader:
            if len(row) < 3:
                continue
            raw_id, text, author = row[0].strip(), row[1].strip(), row[2].strip()
            try:
                motivation_id = int(raw_id)
            except ValueError:
                continue

            rows.append(
                Motivation(
                    id=motivation_id,
                    text=text,
                    author=author or None,
                )
            )

    if not rows:
        return

    async with SessionLocal() as session:
        session.add_all(rows)
        await session.commit()


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with SessionLocal() as session:
        count = await session.scalar(select(func.count(Motivation.id)))

    if count == 0:
        await _import_motivation()

