1. add new version `alembic revision -m "init db"` in where the `alembic.ini` storage
2. goto latest version `alembic upgrade head`
3. `alembic downgrade -1`
4. `alembic upgrade +1`
