def init(screen_size=(800, 600)):

    global w, h, card_w, card_h, n, ncards, path, suits, hidden_card_filename, xoffset, yoffset, ALPHAMAP

    ALPHAMAP = {
    'A':('TTT',[0,0,0]),
    'B':('TTM',[0,0,1]),
    'C':('TTB',[0,0,2]),
    'D':('TMT',[0,1,0]),
    'E':('TMM',[0,1,1]),
    'F':('TMB',[0,1,2]),
    'G':('TBT',[0,2,0]),
    'H':('TBM',[0,2,1]),
    'I':('TBB',[0,2,2]),
    'J':('MTT',[1,0,0]),
    'K':('MTM',[1,0,1]),
    'L':('MTB',[1,0,2]),
    'M':('MMT',[1,1,0]),
    'N':('MMM',[1,1,1]),
    'O':('MMB',[1,1,2]),
    'P':('MBT',[1,2,0]),
    'Q':('MBM',[1,2,1]),
    'R':('MBB',[1,2,2]),
    'S':('BTT',[2,0,0]),
    'T':('BTM',[2,0,1]),
    'U':('BTB',[2,0,2]),
    'V':('BMT',[2,1,0]),
    'W':('BMM',[2,1,1]),
    'X':('BMB',[2,1,2]),
    'Y':('BBT',[2,2,0]),
    'Z':('BBM',[2,2,1])
    }

    if screen_size == (640, 480):
        w = 640
        h = 480
        card_w = 43
        card_h = 64 
        path = "images/640x480/"
        hidden_card_filename = 'images/640x480/hidden.gif'
        suits = ['c', 'd', 'h', 's']
        n = 13
        ncards = 4*n
        xoffset = 123
        yoffset =  24        
        
    elif screen_size == (800, 600):
        w = 800
        h = 600
        card_w = 57
        card_h = 85
        path = "images/800x600/"
        hidden_card_filename = 'images/800x600/hidden.gif'
        suits = ['c', 'd', 'h', 's']
        n = 13
        ncards = 4*n
        xoffset = 123
        yoffset =  24

    elif screen_size == (1024, 768):
        w = 1024 
        h = 768
        card_w = 79
        card_h = 123
        path = "images/1024x768/"
        hidden_card_filename = 'images/1024x768/hidden.gif'
        suits = ['c', 'd', 'h', 's']
        n = 13
        ncards = 4*n
        xoffset = 123
        yoffset = 154
        
    elif screen_size == (1344, 768):
        w = 1344 
        h = 768
        card_w = 79
        card_h = 123
        path = "images/1344x768/"
        hidden_card_filename = 'images/1344x768/hidden.gif'
        suits = ['c', 'd', 'h', 's']
        n = 13
        ncards = 4*n
        xoffset = 123
        yoffset = -34        
