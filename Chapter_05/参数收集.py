def test(x,y,z=3,*books,**score):
    print(x,y,z)
    print(books)
    print(score)

test(1,2,4,"Android","IOS",语文=123,数学=100)