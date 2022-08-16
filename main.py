from src.domain.models.players import Player

from src.infrastructure.postgres.orm import start_mappers
from src.infrastructure.repository import PostgresPlayerRepository
from src.infrastructure.postgres.engines import engine_factory

def main():
    in_memory = engine_factory('in_memory')
    start_mappers(in_memory)
    repo = PostgresPlayerRepository(in_memory)

    player = Player(id="1234", name="valken")
    repo.add(player)

    by_id = repo.get_by_id(id="1234")
    by_name = repo.get_by_name(name="valken")


if __name__ == "__main__":
    main()