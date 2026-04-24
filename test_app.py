from app import tambah, kurang, kali

def test_tambah():
    assert tambah(2, 3) == 5

def test_kurang():
    assert kurang(5, 3) == 2

def test_kali():
    assert kali(3, 4) == 12