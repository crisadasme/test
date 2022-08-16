from contextlib import contextmanager

from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker


@contextmanager
def session_scope(engine: Engine):
    """Provide a transactional scope around a series of operations."""

    session = sessionmaker(bind=engine, expire_on_commit=False)()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
