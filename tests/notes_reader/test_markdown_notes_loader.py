from io import StringIO
import os
import pytest
from unittest.mock import patch, MagicMock
from app.notes_reader.notes_loader import MarkdownNotesLoader


@pytest.fixture(scope="session")
def folder_dir() -> str:
    return 'obsidian_vault'


@pytest.fixture(scope="session")
def note_docker():
    return """
    # Docker

    Multiline Content
    Multiline Content

    #docker #pytest #python
    """


@pytest.fixture(scope="session")
def file_md(note_docker):
    return StringIO(note_docker)


def test_tags_are_normalized():
    tags = ["python", "#pytest", "#python", "Python", "  docker"]

    nl = MarkdownNotesLoader('.', tags)

    assert nl.tags == {"#python", "#pytest", "#docker"}


def test_find_tags_in_multiline_note(note_docker):
    nl = MarkdownNotesLoader('.', [])
    found_tags = nl.find_tags(note_docker)
    assert found_tags == {"#docker", "#pytest", "#python"}


def test_check_tags_from_note_with_tags():
    nl = MarkdownNotesLoader('.', ["python", "pytest"])
    assert nl.check_tags({"#pytest", "#docker"})


def test_check_tags_from_note_without_matching_tags():
    nl = MarkdownNotesLoader('.', ["python", "pytest"])
    assert not nl.check_tags({"#unit_tests", "#docker"})


# Testowanie funkcji load
@patch("os.listdir")
@patch("app.notes_reader.notes_loader.MarkdownNotesLoader.__load_file")
def test_load_notes(mock_load_file, mock_listdir, folder_dir, note_docker):
    # Mockowanie listy plików
    mock_listdir.return_value = ["docker_note.md"]
    mock_load_file.return_value = note_docker

    nl = MarkdownNotesLoader(folder_dir, ["python", "docker"])

    notes = nl.load()

    assert len(notes) == 1
    assert notes[0].title == "docker_note"
    assert "#docker" in notes[0].tags
    assert "#python" in notes[0].tags


# Testowanie metody __get_file_list
@patch("os.listdir")
def test_get_file_list(mock_listdir, folder_dir):
    mock_listdir.return_value = ["docker_note.md", "test_note.md"]

    nl = MarkdownNotesLoader(folder_dir, ["python", "docker"])

    file_list = nl._MarkdownNotesLoader__get_file_list()

    assert "docker_note.md" in file_list
    assert "test_note.md" in file_list
