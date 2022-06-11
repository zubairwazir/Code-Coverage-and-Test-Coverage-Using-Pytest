from mock_db import MockDB
from mock import patch
import utils


class TestUtils(MockDB):

    def test_db_write(self):
        with self.mock_db_config:
            self.assertEqual(utils.db_write("""INSERT INTO `test_table` (`id`, `text`, `int`) VALUES
                            ('3', 'test_text_3', 3)"""), True)
            self.assertEqual(utils.db_write("""INSERT INTO `test_table` (`id`, `text`, `int`) VALUES
                            ('1', 'test_text_3', 3)"""), False)
            self.assertEqual(utils.db_write("""DELETE FROM `test_table` WHERE id='1' """), True)
            self.assertEqual(utils.db_write("""DELETE FROM `test_table` WHERE id='4' """), True)

    def test_db_read(self):
        with self.mock_db_config:
            self.assertEqual(utils.db_read("""SELECT * FROM `test_table` where id=1"""), [{'id': '1', 'int': 1,
                                                                                           'text': 'test_text'}])
            response = utils.db_read("""SELECT * FROM `test_table` where id=1""")
            assert response is not None
