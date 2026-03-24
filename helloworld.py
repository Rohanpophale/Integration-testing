def add(a, b):
    return a + b


def main():
    a = 2
    b = 2
    expected = 5
    result = add(a, b)

    if result == expected:
        print(True)
        return 0

    print(False)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
