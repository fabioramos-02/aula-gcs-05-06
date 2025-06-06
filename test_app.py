from app import soma

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0
    assert soma(100, 200) == 300
    assert soma(-5, -5) == -10

if __name__ == "__main__":
    test_soma()
    print("Todos os testes passaram!")