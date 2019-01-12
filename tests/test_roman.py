from codekata.roman import dec_to_roman

def test_dec_to_roman():
    assert dec_to_roman(1) == 'I'
    assert dec_to_roman(2) == 'II'
    assert dec_to_roman(3) == 'III'
    assert dec_to_roman(4) == 'IV'
    assert dec_to_roman(5) == 'V'
    assert dec_to_roman(6) == 'VI'
    assert dec_to_roman(7) == 'VII'
    assert dec_to_roman(8) == 'VIII'
    assert dec_to_roman(9) == 'IX'
    assert dec_to_roman(10) == 'X'
    assert dec_to_roman(11) == 'XI'
    assert dec_to_roman(12) == 'XII'
    assert dec_to_roman(13) == 'XIII'
    assert dec_to_roman(14) == 'XIV'
    assert dec_to_roman(15) == 'XV'
    assert dec_to_roman(16) == 'XVI'

    assert dec_to_roman(20) == 'XX'
    assert dec_to_roman(20) == 'XX'
    assert dec_to_roman(20) == 'XX'

    assert dec_to_roman(50) == 'L'
    assert dec_to_roman(100) == 'C'

    assert dec_to_roman(120) == 'CXX'
