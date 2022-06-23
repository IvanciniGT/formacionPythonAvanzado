# Distrubir código python

Version de python que necesito tener
    Si instala mi versión... que pasa si tiene apps que requieren de otra versión...

Dependencias
    Yo uso unas dependencias..
    Estan instaladas en el entorno donde se va a ejecutar mi código?
        Si o no
        Y si están instaladas otras versiones diferentes a las que yo uso???
        Y son incompatibles entre apps

Virtual Environments < MUERTO 
    Esto resuelve parte del problema (tando en distribución, como en desarrollo)

Contenedores < DOCKER *********

---

# Contenedor. Qué es contenedor?

Un contendor es un entorno aislado, donde ejecutar procesos, dentro de un SO Linux®.

Ailado en cuanto a qué?
- Su propio filesystem
- Su propia configuración de RED, su propia IP
- Sus propias variables de entorno
- Limitación de acceso a los recursos HW del host

Los contenedores los creamos desde una imagen de contenedor.

## Qué es una imagen de contenedor?

Es un fichero comprimido (tar) que contiene un programa YA INSTALADO por alguien
y preconfigurado.
Las imágenes de contenedor las conseguimos de un registry de repositorios de 
imagenes de contenedor: docker hub, quay.io


    Office | MariaDB | MySQL
    1º Descargar un instalador MariaDB
    2º Ejecuto el instalador
    3º Configuro el software
    
    c:\archivos de programa\"mariadb" -> ZIP -> Os lo mando 
    ZIP > Misma ruta... os funciona? NO en la mayor parte de los casos.

---


Docker Desktop for Windows  ->  wsl para ejecutar un kernel de Linux donde correr los contendores
                                maquina virtual en hyperV
Docker Desktop for MacOS    ->  monta una mv con otro hipervisor, pero que corre linux

Linux es el kernel de SO más utilizado en el mundo.

Linux no es un SO... es un kernel de SO.
GNU/Linux < Redhat Enterprise Linux, CentOS, Ubuntu, Debian.
Android < Linux

Kernel de Windows : DOS , NT


# Modelo de instalación tradicional:

    App1 + App2 + App3          Problemas: 
    --------------------            - Incompatibilidad SO
            SO                      - Incompatibilidad de dependencias, configuraciones
    --------------------            - App1 se vuelve loca (cpu 100%)
          HIERRO                        App1 muere > App2 y App3 van detras
                                    - App1 potencialmente puede acceder a los ficheros de app2

# Maquinas virtuales:

      App1   | App2 + App3      Problemas: 
    --------------------            - La configuración se hace mucho más compleja:
      SO 1   |   SO 2                       Necesito N sistemas operativos
    --------------------                        A instalar
      MV 1   |   MV 2                           Configurar
    --------------------                        Mantener
        Hipervisor                  - Desperdicio de recursos
    vmware, virtualbox,             - Perdida en rendimiento
    hyperv, kvm, citrix
    --------------------            
            SO                      
    --------------------            
          HIERRO
                                    
# Contenedores:

      App1   | App2 + App3
    --------------------  
      C 1    |   C 2     
    --------------------  
     Gestor Contenedors
       DOCKER, podman
      crio, containerd
    --------------------            
         SO Linux
    --------------------
          HIERRO

Están estandarizados: Hay un estandar OpenContainerInitiative (DOCKER)
Da igual el software que vaya dentro del contenedor:
Todos se operan de la misma forma:
    Arranque
    Parada
    Reinicio
    Ver los logs
    Configurarlo
    
---
Maquina 
    Interfaces de red
        loopback     (virtual) < 127.0.0.1 (localhost) "there is no plce like 127.0.0.1"
        Ethernet (LAN) > NIC (tarjeta de red)
        Wifi           > NIC (wifi)
        docker      Red virtual: 172.17.0.0/16
            host:      172.17.0.1
            contenedor 172.17.0.2

Ubuntu Instalar apps paquetes: apt-get (heredado de debian)
Redhat                         yum




CRM - Web

# Entorno de Producción:
- Alta disponibilidad: Intentar garantizar un tiempo de funcionamiento de la app...
                       Intentar garantizar la no perdida de información 
                            REPLICACION
                                Procesos < CLUSTER
                                Datos
            90%     -> 36 dias al año que puede estar off                       |   €
            99%     -> 3,6 dias al año                                          |   €€
            99,9%   -> 8 horas (incluyendo mantenimientos y actualizaciones)    |   €€€€€
            99,99%  -> Minutos                                                  V   €€€€€€€€€€€€€€
- Escalabilidad: Capacidad de ajustar mi infraestructura a las necesidades puntuales
    
    # Modelo de app 1
        App1:   CUALQUIER APP DEPARTAMENTAL: Guardia civil: perdir uniforme
            dia 1 :            1000 personas
            dia 100 :          980 personas         NO HAY ESCALABILIDAD
            dia 1000 :         1020 personas

    # Modelo de app 2
        App2:   App de un servicio que ofrezco y cada vez tengo mas clientes
            dia 1 :            100   personas   
            dia 100 :          1000  personas       SI NECESITO CRECER
            dia 1000 :         11000 personas
    
    # Modelo de app 3
        App3:   INTERNET esto es el dia de hoy
            dia n :            100     personas   
            dia n+1 :          100000  personas  
            dia n+2 :          200     personas
            dia n+3 :          2000000 personas 
            
    CLUSTER
        Contrato maquinas a un cloud bajo demanda (terraform)
        Y como pongo mi software a funcionar alli dentro
            CONTENEDORES > IMAGEN con todo ya montado 
    
Kubernetes/Openshift
    Gestores de gestores de contenedores


- Seguridad (Todos los entornos)

---
Diseñais una prueba
Haceis el producto
Ejecutais la prueba
---
DNI / ISO 
Coche EUROCAP

Hago una app web, y hago su pantalla de login
Diseño: Voy a ver si curiosamenet mi app tiene una pantalla de login
        Y si me tod un dato ok entro y si no pues no entro
Ejecutamos
---
Sistema/App
La app falla... que ha fallao?
El objetivo no es solo ver si aquello funciona, es si no funciona, identificar el problema.
---
Estáticas
    Calidad de código INDECENTE = MANTENIMIENTO HORRIBLE + POTENCIALES PROBLEMAS
    SonarQube <<<  Hermano mayor que sabe un huevo de python > Code smells > tiempo deuda técnica
Dinámicas
    Funcionales
        Unitarias:          Prueba que comprueba la funcionalidad de una unidad (metodo)
            Código 300 funciones : al menos 300 pruebas unitarias
        Integracion:        Prueba es la comunicación entre dos componentes
        sistema             Pruebo que el sistema cumple con su función
        Aceptacion          Pruebo si hace lo que quiere cliente
    No funcionales
        Estres
        Carga
        UX
        HA

Complejidad cognitiva   Como de dificil es para un ser humano entender el codigo

Complejidad ciclomática     5           
            ---- Determinar el minimo numero de pruebas que tengo que hacer
    Número de caminos distintos que puede tomar el codigo
    
if CONDICION1:
    if CONDICION2: 
        pass
    elif CONDICION3:
        pass
    else:
        pass
else:
    if CONDICION4:
        pass
    else:
        pass

match valor: 
    case 1:  
    case 2:  
    case 3:
    case 4:
        valor/denominador
    case _:
    
Orden de complejidad de un algoritmo <<<< Libros
