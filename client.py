import socket
UDP_IP= "10.160.108.93"
UDP_PORT= 5050
data=""
OK=("En ligne")
import marshal
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

BN=[['*','A','B','C','D','E',"F","G","H","I","J"],['0','-','-','-','-','-','-','-','-','-','-'],['1','-','-','-','-','-','-','-','-','-','-'],['2','-','-','-','-','-','-','-','-','-','-'],
    ['3','-','-','-','-','-','-','-','-','-','-'],['4','-','-','-','-','-','-','-','-','-','-'],['5','-','-','-','-','-','-','-','-','-','-'],['6','-','-','-','-','-','-','-','-','-','-'],
    ['7','-','-','-','-','-','-','-','-','-','-'],['8','-','-','-','-','-','-','-','-','-','-'],['9','-','-','-','-','-','-','-','-','-','-']]     #Creation du tableau de jeu


def Afficher():
    tab=""
    for i in range(11):
        tab= "| "
        for j in range(11):
            tab +=BN[i][j]
            tab += " | "
        print(tab)
def Bateau():
    sens=""
    

print("Recherche du serveur...")
#Afficher()
sock.sendto(OK.encode(),(UDP_IP, UDP_PORT))
data = sock.recvfrom(1024)

if (data != ""):
    print("Serveur en ligne")
    print("IP:...",UDP_IP)
    print("*** Lancement de la partie ***\n")
while True:
        MESSAGE=input("Entre la position:")
        sock.sendto(MESSAGE.encode(),(UDP_IP, UDP_PORT))
        data, addr = sock.recvfrom(1024)
        BN=marshal.loads(data)
        Afficher()
