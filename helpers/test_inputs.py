from helpers.inputs import DataReader

class TestAocData():
    def test_from_str(self):
        s = (
            "1a\n"
            "2b\n"
            "3c"
        )
        data = DataReader.from_str(s)
        assert data == ['1a', '2b', '3c']

    def test_from_file(self, tmp_path):
        import os
        p = os.path.join(tmp_path, "test")
        with open(p, 'w') as f:
            f.write(
                "1a\n"
                "2b\n"
                "3c"
            )

        data = DataReader.from_file(p)
        assert data == ['1a', '2b', '3c']

    def test_split_group(self):
        s = (
            "1a\n"
            "\n"
            "\n"
            "2b\n"
            "3c"
        )
        data = DataReader.from_str(s)
        list = DataReader.split(data)
        assert len(list) == 3
        assert list[0] == ['1a']
        assert list[1] == []
        assert list[2] == ['2b', '3c']