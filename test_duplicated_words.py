from duplicated_words import check_duplicates
def test():
    assert check_duplicates("foo") == True 
    assert check_duplicates("car") == False 
    assert check_duplicates("ala ma kota") == True
    assert check_duplicates("ma ala kota") == True
    assert check_duplicates("kota ma ala") == True
    assert check_duplicates("kota ma al") == False