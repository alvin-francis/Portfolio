def cooling_cap():
    
    again= True
    
    while again==True:
        
        hp_val=''
        btu_val=''
        tr_val = ''
        kw_val= ''
        unit1=''

        while unit1 not in ["hp","btuh","tr","kw"]:
            unit1=input("Choose unit(hp,btuh,tr,kw): ")
            if unit1 not in ["hp","btuh","tr","kw"]:
                print("not recognized")
    
        if unit1=="hp":
            
            hp_val=float(input("convert hp to btu/hr, tr and kW: "))
            btu_val=9500*hp_val
            tr_val =0.8*hp_val
            kw_val=2.49*hp_val
            print(f'{hp_val} HP is equal to {btu_val} BTU/hr')
            print(f'{hp_val} HP is equal to {tr_val} TR')
            print(f'{hp_val} HP is equal to {kw_val} kW')
    
        elif unit1=="btuh":
            btu_val=float(input("convert btu/hr to hp, tr and kW: "))
            hp_val = btu_val/9500
            tr_val = btu_val*0.8/9500
            kw_val = btu_val*2.49/9500
            print(f'{btu_val} BTU/hr is equal to {hp_val} HP')
            print(f'{btu_val} BTU/hr is equal to {tr_val} TR')
            print(f'{btu_val} BTU/hr is equal to {kw_val} kW')
        
        elif unit1=="tr":
            tr_val =float(input("convert tr to hp, btu/hr and kW: "))
            hp_val = tr_val/0.8
            btu_val = tr_val*9500/0.8
            kw_val = tr_val*2.49/0.8
            print(f'{tr_val} TR is equal to {hp_val} HP')
            print(f'{tr_val} TR is equal to {btu_val} BTU/hr')
            print(f'{tr_val} TR is equal to {kw_val} kW')
            
        else:
            kw_val = float(input("convert kw to hp, btu/hr and tr: "))
            hp_val = kw_val*2.49
            btu_val= kw_val*9500/2.49
            tr_val = kw_val*0.8/2.49
            print(f'{kw_val} kW is equal to {hp_val} HP')
            print(f'{kw_val} kW is equal to {btu_val} BTU/hr')
            print(f'{kw_val} kW is equal to {tr_val} TR')
            
        replay=input("convert more?(y/n): ").upper()
        if replay=="Y":
            again=True
        else:
            again=False
            
cooling_cap()
