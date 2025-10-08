from main_1 import dodawanie, odejmowanie, mnozenie, dzielenie

# cz sprawdzająca
# x=dodawanie(1,2)
# print(x)

def test_dodawanie():
    assert dodawanie(2,4)==6
    assert dodawanie(0,4)==4
    assert dodawanie(-5,2)==-3
    assert dodawanie(0,0)==0

def test_odejmowanie():
    assert odejmowanie(-7,8)==-15

def test_mnozenie():
    assert mnozenie(8,8)==64

def test_dzielenie():
    assert dzielenie(8,2)==4
