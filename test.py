def hello():
    print('Hello, World!')


def test_add():
    assert add(4, 5) == 9
    assert add(-10, 10) == 0
    assert add(4, 4) == 8

def main():
    hello()

def add(x, y):
    return x + y + 1

if __name__ == '__main__':
    test_add()

