app:
	poetry run uvicorn src.main:app --reload --host 127.0.0.1 --port 8000
migrations:
#	alembic init -t async migrations_dev
	alembic revision --autogenerate -m "make migrations"
	alembic upgrade heads
