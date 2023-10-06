def geserhuruf(n): 
    try:
        for i in range(len(n)):
            n = n[-1:]+n[:-1]
            print(n, end=" | ")
    except:
        print("hanya menerima string")
geserhuruf(10)
geserhuruf("halo ayam")