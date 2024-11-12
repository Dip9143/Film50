# It's just mock test function
from unittest.mock import patch, MagicMock
import project

def test_rec_film():
    with patch("project.input_option", return_value=1), \
         patch("project.toprated") as mock_toprated:

        pass

def test_search_film():
    with patch("project.input", return_value="Inception"), \
         patch("project.requests.get") as mock_get:
        pass

def test_clear_watch():
    with patch("builtins.open", new_callable=MagicMock) as mock_open:
        project.clear_watch()
        pass

def test_clear_not():
    with patch("builtins.open", new_callable=MagicMock) as mock_open:
        project.clear_not()
        pass
