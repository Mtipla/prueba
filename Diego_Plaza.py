import funciones as fn

while True:
    fn.menu_p()
    opcion=fn.validar_numero(1,4,"una opcion: ","OPCION INVALIDA")
    if opcion==1:
        fn.grabar()
    elif opcion==2:
        fn.buscar_m()
    elif opcion==3:
        fn.retirasre()
    else:
        print("Graias por venir, vuelva pronto")
        break
 