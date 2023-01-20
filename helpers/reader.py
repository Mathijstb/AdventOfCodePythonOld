class DataReader:

    @staticmethod
    def from_str(s):
        return s.split('\n')

    @staticmethod
    def from_file(f_in):
        with open(f_in, 'r') as f:
            return [l.strip('\n') for l in f.readlines()]

    @staticmethod
    def split(data, sep=''):
        groups = []
        currentGroup = []
        for x in data:
            if x == sep:
                groups.append(currentGroup)
                currentGroup = []
            else:
                currentGroup.append(x)
        groups.append(currentGroup)

        return groups
