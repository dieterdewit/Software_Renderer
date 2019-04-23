from KryuGL import *

# Posicion de la Camara
eye = V3(1, 1, 5)
center = V3(0, 0, 0)
displace = V3(0, 1, 0)

# Llama las funciones para la escritura de la imagen .bmp
r = Bitmap(920, 920)
r.glViewPort(1, 1, 919, 919)
r.lookAt(eye, center, displace)

# Lectura de la Textura
fondo = Texture('./Fondo/stars.bmp')
r.framebuffer_fondo(fondo)

# Se elige un shader a utilizar en los modelos siguientes
r.shader = r.tie_shader

# ---------- Cargar los modelos bmp con textura mtl ----------
# Tie-Fighter
r.glLoad(
    './Modelos/tie.obj',
    mtl='./Modelos/tie.mtl',
    translate=(2.25,1.75,0),
    scale=(0.44,0.44,0.44),
    rotate=(0.2,-0.2,0)
    )

r.glClearZbuffer()

r.shader = r.arc_shader

# Arc
r.glLoad(
    './Modelos/arc.obj',
    mtl='./Modelos/arc.mtl',
    translate=(6.3,2.75,0),
    scale=(0.175,0.175,0.175),
    rotate=(-1,3,0.3)
    )

r.glClearZbuffer()

r.shader = r.gouraud

# Tie2
r.glLoad(
    './Modelos/tie2.obj',
    mtl='./Modelos/tie2.mtl',
    translate=(0.5,4,0),
    scale=(0.3,0.3,0.3),
    rotate=(0.5,0.25,0)
    )
    
r.glClearZbuffer()

r.shader = r.gouraud

# X-Wing
r.glLoad(
    './Modelos/x.obj',
    mtl='./Modelos/x.mtl',
    translate=(1.25,0.5,0),
    scale=(0.39,0.39,0.39),
    rotate=(0.2,0,-0.06)
    )
    
r.glClearZbuffer()

r.shader = r.laser_shader

r.glLoad(
    './Modelos/al-bar.obj',
    mtl='./Modelos/al-bar.mtl',
    translate=(-0.45,0,0),
    scale=(1.1,1.1,2.5),
    rotate=(1.5,0.15,0)
    )

r.glClearZbuffer()

r.glLoad(
    './Modelos/al-bar.obj',
    mtl='./Modelos/al-bar.mtl',
    translate=(-0.7,0,0),
    scale=(1.1,1.1,2.5),
    rotate=(1.5,0.15,0)
    )
# ------------------------------------------------------------

# Creacion del Archivo
r.glFinish('StarWars_15146.bmp')
