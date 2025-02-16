import logging.config

from app.logging_setup import setup_logging

logger = logging.getLogger(__name__)

# _dirname = Path(__file__)


def main() -> None:
    setup_logging()

    # notes_loader = MarkdownNotesLoader(os.path.join("..", 'obsidian_vault'), {"python", "docker", "pytest"})
    # notes = notes_loader.load()
    #
    # clientAI = CardGen(model="gpt-4o-mini")
    #
    # cards = []
    #
    # for note in notes:
    #     logger.info(f"Processing note: ")
    #     flashcards = clientAI.create_card_json(note.content)
    #     cards.append(flashcards.choices[0].message.content)

    # print(cards)


if __name__ == "__main__":
    main()
