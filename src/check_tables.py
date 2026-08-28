from sqlalchemy import inspect
from src.database import get_engine

engine = get_engine()

inspector = inspect(engine)

tables = inspector.get_table_names()

print("\nTables in database:")
for table in tables:
    print(f" - {table}")

print(f"\nTotal tables: {len(tables)}")