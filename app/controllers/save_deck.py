from dataclasses import asdict

from app.db.db import DBTiny
from app.models.flashcard_models import FlashCardSrc
from app.settings.settings import dirname_app


def save_deck(deck: dict[str, str | list[int]]) -> None:
    with DBTiny(dirname_app / '.store', 'decks') as db:
        db.create(deck)