# core/gestion_solicitudes.py

# Aquí se implementará la lógica para gestionar las solicitudes de material.

# from .modelos_datos import Solicitud, Item
# from ..database import queries

class GestionSolicitudes:
    def __init__(self):
        # Inicialización, si es necesaria
        pass

    def crear_nueva_solicitud(self, id_tecnico: int, detalles_items: list):
        # Lógica para crear una nueva solicitud
        # Esto implicaría validar los datos, posiblemente verificar stock,
        # y luego llamar a queries.crear_solicitud(...)
        print(f"Creando nueva solicitud para técnico {id_tecnico} con items: {detalles_items}")
        # Ejemplo:
        # nueva_solicitud = Solicitud(id_solicitud=None, id_tecnico=id_tecnico, ...)
        # queries.crear_solicitud(nueva_solicitud, detalles_items)
        pass

    def aprobar_solicitud(self, id_solicitud: int):
        # Lógica para aprobar una solicitud y actualizar el stock
        print(f"Aprobando solicitud {id_solicitud}")
        # solicitud = queries.obtener_solicitud_por_id(id_solicitud)
        # if solicitud:
        #   for item_solicitado in solicitud.items:
        #       gestion_stock.actualizar_cantidad_item(item_solicitado.id_item, -item_solicitado.cantidad_solicitada)
        #   queries.actualizar_estado_solicitud(id_solicitud, "Aprobada")
        pass