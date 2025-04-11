OSPF = 110
RIP =120
EIGRP = 90
BGP = 20

pregunta = str(input("De que protocolo desea saber la Distancia Administrativa?: "))

if pregunta ==str("OSPF"):
    print("La Distancia Administrativa del protocolo OSPF es "+ str(OSPF))
elif pregunta==str("RIP"):
    print("La Distancia Administrativa del protocolo RIP es "+ str(RIP))
elif pregunta==str("EIGRP") :
    print("La Distancia Administrativa del protocolo EIGRP es "+ str(EIGRP))
elif pregunta==str("BGP"):
    print("La Distancia Administrativa del protocolo BGP es "+ str(BGP))
else:
    print("Por favor escribe un nombre valido para el protocolo \n(por ejemplo OSPF, RIP,EIGRP o BGP)")