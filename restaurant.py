import numpy as np
from colorama import init, Fore
init(autoreset=True) 
def ver_restaurant(mesas):
    cant=0
    mesa=0
    print(" ",end="  ")
    print(" ")
    for i in range(len(mesas)):
        cant+=2
        print(cant,end=" ")
        for k in range(len(mesas[i])):
            mesa+=1
            if mes[i][k]:
                    print(Fore.RED+f"[{mesa}]",end="")
                    
            else:
                print(Fore.GREEN+f"[{mesa}]",end="")       
        print(" ")

def validar_cantidad(cant_minima,cant_maxima,testo):
    while True:
        try:
            op=int(input(f"ingrese una {testo}: "))
            if op>cant_minima and op<cant_maxima:
                break
            else:
                print("ingrese una opcion valida ")
        except:
            print("ingrese un numero entero ")
    return op
def validar_rut():
    while True:
        try:
            rut=int(input("ingrese su rut: "))
            if rut>=10000000 and rut <=99999999:
                break
            else:
                print("ingrese un rut entre un millo y 99 millones")
        except:
            print("ingrese el rut sin guion ni rut verificador")
    return rut
def reserva(mesas,cant):
    contrado=False
    cont=0
    lista_reserva=[]
    lista_estacionaria=[]
    for i in range(len(mes)):
        for k in range(len(mes[i])):
            if mes[i][k]==False:
                cont+=1
    if cont>0:
        for i in range(1):
                rut=validar_rut()
                while True:
                    nombre=input("ingrese su nombre: ")
                    if len(nombre.strip())>3 and nombre.isalpha():
                        break
                    else:
                        print("el nombre debe tener una logitud de mas de 3 caracteres ")
                while True:
                    correo=input("ingrese su correo: ")
                    for i in correo:
                        if i=="@":
                            contrado=True
                            break
                    if contrado:
                        break
                    else:
                        print("ingrese un correro valido")
        if cant>=1 and cant<3: 
            posicion=0
        elif cant>=1 and  cant<5:
            posicion=1
        elif cant>=1 and cant<7:
            posicion=2
        while True:
            ver_restaurant(mesas)
            try:
                mesa=int(input("ingrese la mesa: "))
                if mesa in mesas[posicion]:
                    break
                else:
                    print(f"ingrese una mesa correcta para {cant} personas")
            except:
                print("ingrese un numero entero")
        if mesa==mesas[posicion][0]:
            columa=0
        elif  mesa==mesas[posicion][1]:
            columa=1
        else:
            columa=2
        fila=posicion
        if  mes[fila][columa]==False:
            mes[fila][columa]=True
        else:
            print("mesa ocupada")
        lista_reserva.append(mesa)
        lista_reserva.append(fila)
        lista_reserva.append(columa)
        lista_reservas.append(lista_reserva)
        lista_estacionaria.append(mesa)
        lista_estacionaria.append(rut)
        lista_estacionaria.append(nombre)
        lista_estacionaria.append(correo)
        lista_clientes.append(lista_estacionaria)
    else:
        print("todas las mesas estan reservadas")
def imprimir_alimentos(lista):
    for i in range(len(lista)):
        for k in range(len(lista[i])):
            if lista[i][k]==lista[0][k]:
                print(lista[i][k],'\n')
        print(" ")
def compra(cant,lista,posi):
    precio=cant*lista[1][posi]
    print(f"precio: {precio}")
    return precio
def validar_mesa(lista_reservas,mesa):
    mesano=False
    for i in range(len(lista_reservas)):
        if lista_reservas[i][0]==mesa:
            mesano=True
            return mesano
def cancelar_reserva(lista_reservas,lista_pedidos,lista_clientes,mesa,mes):
    while True:
        for i in range(len(lista_pedidos)):
            if lista_pedidos[i][0]==mesa:
                posicion=i
                lista_pedidos.pop(posicion)
                break
        else:
            break
    for i in range(len(lista_clientes)):
        if lista_clientes[i][0]==mesa:
                lista_clientes.pop(i)
                break
    for i in range(len(lista_reservas)):
        if lista_reservas[i][0]==mesa:
            fila=lista_reservas[i][1]
            columa=lista_reservas[i][2]
            mes[fila][columa]=False
            break
    for i in range(len(lista_reservas)):
        if lista_reservas[i][0]==mesa:
            lista_reservas.pop(i)
            break
mesas = np.array([[1,2,3],[4,5,6],[7,8,9]],int)
mes=np.zeros((3,3),bool)
cant=np.array([[2,2,2],[4,4,4],[6,6,6]],int)
lista_clientes=[]
lista_reservas=[]
lista_pedidos=[]
lista_bebidas=[['1-cococola $1000','2-pepsi $1000','3-watss $700'],
               [1000,1000,700]]
lista_platos=[['1-arroz $3200','2-fideos $3000','3-potoros $3000'],
              [3200,3000,3000]]
lista_postres=[['1-chanel $600','2-suspiro alimeño $1200','3-yogurt $400'],
               [600,1200,400]]
print("bienvenido a casa blanca")
while True:
    print("""
    1-ver mesas
    2-reservar mesa
    3-ver la carta
    4-pagar la cuenta
    5-cancelar reserva
    6-salir
    """)
    op=validar_cantidad(0,7,'opcion')
    if op==1:
        ver_restaurant(mesas)
    elif op==2:
        ver_restaurant(mesas)
        cant=validar_cantidad(0,7,'una cantidad de personas')
        reserva(mesas,cant)
    elif op==3:
        lista_cant=[]
        lista_suma=[]
        suma_bebidas=0
        suma_platos=0
        suma_postres=0
        cant_bedidas=0
        cant_platos=0
        cant_postres=0
        lista_temporal=[]
        mesano=False
        ver_restaurant(mesas)
        mesa=validar_cantidad(0,10,'mesa, donde esta sentado')
        mesano=validar_mesa(lista_reservas,mesa)
        while True:
            if mesano:
                print("""
                1-ver la carta
                2-solicitar pedido
                3-cancelar pedido
                """)
                op=validar_cantidad(0,4,'opcion')
                if op==1:
                    while True: 
                        print("""
                        1-bebestibles
                        2-platos
                        3-postres
                        4-salir
                        """)
                        op=validar_cantidad(0,5,'opcion')
                        if op==1:
                            imprimir_alimentos(lista=lista_bebidas)
                            op=validar_cantidad(0,4,'bebida')
                            
                            if op==1:
                                cant=validar_cantidad(0,55,'cantidad de cocacolas')
                                precio=compra(cant=cant,lista=lista_bebidas,posi=0)
                                suma_bebidas+=precio
                                cant_bedidas+=cant
                            elif op==2:
                                cant=validar_cantidad(0,55,'cantidad de pepesis')
                                precio=compra(cant=cant,lista=lista_bebidas,posi=1)
                                suma_bebidas+=precio
                                cant_bedidas+=cant
                            else:
                                cant=validar_cantidad(0,55,'cantidad de watss')
                                precio=compra(cant=cant,lista=lista_bebidas,posi=2)
                                suma_bebidas+=precio
                                cant_bedidas+=cant
                        elif op==2:
                            imprimir_alimentos(lista=lista_platos)
                            op=validar_cantidad(0,4,'platos')
                            if op==1:
                                cant=validar_cantidad(0,55,'de platos de arroz')
                                precio=compra(cant=cant,lista=lista_platos,posi=0)
                                suma_platos+=precio
                                cant_platos+=cant
                            elif op==2:
                                cant=validar_cantidad(0,55,'de platos de fideos')
                                precio=compra(cant=cant,lista=lista_platos,posi=1)
                                suma_platos+=precio
                                cant_platos+=cant
                            else:
                                cant=validar_cantidad(0,55,'de platos de porotos')
                                precio=compra(cant=cant,lista=lista_platos,posi=2)
                                suma_platos+=precio
                                cant_platos+=cant
                        elif op==3:
                            imprimir_alimentos(lista=lista_postres)
                            op=validar_cantidad(0,4,'postres')
                            if op==1:
                                cant=validar_cantidad(0,55,'de chanels')
                                precio=compra(cant=cant,lista=lista_postres,posi=0)
                                suma_postres+=precio
                                cant_postres+=cant
                            elif op==2:
                                cant=validar_cantidad(0,55,'de suspiros alimenños')
                                precio=compra(cant=cant,lista=lista_postres,posi=1)
                                suma_postres+=precio
                                cant_postres+=cant
                            else:
                                cant=validar_cantidad(0,55,'de yogurts')
                                precio=compra(cant=cant,lista=lista_postres,posi=2)
                                suma_postres+=precio
                                cant_postres+=cant
                        else:
                            break
                elif op==2:
                    if cant_bedidas>0 or cant_platos>0 or cant_postres>0:
                        total_pedido=0
                        print(f"""
                        bebidas {cant_bedidas}
                        precio bebidas {suma_bebidas}
                        -----------------------------
                        platos {cant_platos}
                        precio platos {suma_platos}
                        -----------------------------
                        postres {cant_postres}
                        precio postres {suma_postres}
                        """)
                        lista_almacen=[]
                        total_pedido=suma_bebidas+suma_platos+suma_postres
                        lista_suma.append(total_pedido)
                        lista_almacen.append(mesa)
                        lista_almacen.append(lista_suma)
                        lista_pedidos.append(lista_almacen)
                        break
                else:
                    break
            else:
                print(f"la mesa {mesa} no tiene clientes")
                break
        print("opcion 3")
    elif op==4:
        sub_total=0
        total=0
        mesa=validar_cantidad(0,10,'mesa, donde esta sentado')
        mesano=validar_mesa(lista_reservas,mesa)
        if mesano:
            for pedido in lista_pedidos:
                if pedido[0]==mesa:
                   sub_total+=sum(pedido[1])
            iva=sub_total*0.19
            total=sub_total+iva
            propina=total*0.10
            if total>0:
                while True:
                    print(f"""
                    -subtotal {sub_total}
                    -Iva {iva}
                    ------------

                    total  {total}
                    propina {propina}
                    """)
                    while True:
                        try:
                            pago=int(input("ingrese el pago: "))
                            if pago>-1:
                                break
                            else:
                                print("ingrese un pago valido")
                        except:
                            print("ingres una cantidad entera")
                    if pago==total:
                        cancelar_reserva(lista_reservas,lista_pedidos,lista_clientes,mesa,mes)
                        break
                    elif pago>total:
                        vuelto=pago-total
                        print(f"su vuelto {vuelto}")
                        cancelar_reserva(lista_reservas,lista_pedidos,lista_clientes,mesa,mes)
                        break
                    else:
                        print("dinero insuficiente")
            else:
                cancelar_reserva(lista_reservas,lista_pedidos,lista_clientes,mesa,mes)
        else:
            print("esa mesa no tinene clientes")
    elif op==5:
        mesa=validar_cantidad(0,10,'mesa, donde esta sentado')
        cancelar_reserva(lista_reservas,lista_pedidos,lista_clientes,mesa,mes)
    else:
        break