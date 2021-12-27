import pytest
from unittest.mock import patch
import app

tests_for_doc_owner = [
    ["11-2", "Геннадий Покемонов"],
    ['56', None],
    ['', None],
    [None, None]
]
tests_for_doc_shelf = [
    ['10006', '2'],
    ['56', None],
    ['', None],
    [None, None]
]
tests_for_delete_doc = [
    ['10006', ('10006', True)],
    ['56', None],
    ['', None],
    [None, None]
]
tests_for_add_new_doc = [
    [('123456', 'passport', 'ФИО', '1'), '1', 'Новый документ'],
    [
        ("11-2", "invoice", "Геннадий Покемонов", '4'),
        None,
        'Добавление документа с существующим номером'
    ]
]


class TestSecretary:
    @pytest.mark.parametrize('user_doc_number, expected', tests_for_doc_owner)
    @patch('builtins.input')
    def test_get_doc_owner_name(self, mock_input, user_doc_number, expected):
        mock_input.return_value = user_doc_number
        assert app.get_doc_owner_name() == expected

    @pytest.mark.parametrize('user_doc_number, expected', tests_for_doc_shelf)
    @patch('builtins.input')
    def test_get_doc_shelf(self, mock_input, user_doc_number, expected):
        mock_input.return_value = user_doc_number
        assert app.get_doc_shelf() == expected

    @pytest.mark.parametrize('user_doc_number, expected', tests_for_delete_doc)
    @patch('builtins.input')
    def test_delete_doc(self, mock_input, user_doc_number, expected):
        mock_input.return_value = user_doc_number
        assert app.delete_doc() == expected

    @pytest.mark.parametrize('test_inputs, expected, description',
                             tests_for_add_new_doc)
    @patch('builtins.input')
    def test_add_new_doc(self, mock_input,
                         test_inputs, expected, description):
        mock_input.side_effect = test_inputs
        assert app.add_new_doc() == expected, description
