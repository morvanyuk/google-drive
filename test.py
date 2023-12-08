import unittest
from main import push_file, create_metadata

class FileTest(unittest.TestCase):


    def test_file_pushing_jpeg(self):
        metadata = create_metadata('', 'jpeg', 'image/jpeg')
        push_file('images/1.jpeg', metadata=metadata)
        
    def test_file_pushing_png(self):
        metadata = create_metadata('', 'png', 'image/png')
        push_file('images/2.png', metadata=metadata)

    def test_file_pushing_jpg(self):
        metadata = create_metadata('', 'jpg', 'image/jpg')
        push_file('images/3.jpg', metadata=metadata)

if __name__ == '__main__':
    unittest.main()