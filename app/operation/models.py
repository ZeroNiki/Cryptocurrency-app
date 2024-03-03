from sqlalchemy import Table, String, Integer, Column, MetaData

metadata = MetaData()

crypto_data = Table(
    "cr_data",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("symbol", String, nullable=False),
)
