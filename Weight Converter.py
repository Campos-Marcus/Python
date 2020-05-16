def conv(a,b):
    if b == 'l' or 'L':
        final_value = a * 0.45
    elif b == 'K' or 'k':
        final_value = a * 2.2
    else:
        print("Wrong character")

    print(f"final value: {final_value}")


weight = input("weight: ")

measure_unit = input( 'L(bs) or (K)g: ')

conv(float(weight), str(measure_unit))



    
