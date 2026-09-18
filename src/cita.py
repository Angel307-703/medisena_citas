class CitaMedica:
    def __init__(self, id_cita: str, paciente: str, especialidad: str, fecha: str, costo_consulta: float, es_urgencia: bool):
        self.id_cita = id_cita
        self.paciente = paciente
        self.especialidad = especialidad
        self.fecha = fecha
        self.costo_consulta = costo_consulta
        self.es_urgencia = es_urgencia

    def calcular_costo_final(self) -> float:
        """Aplica un descuento del 15% si la cita no es de urgencia (Cita Programada)."""
        if not self.es_urgencia:
            return self.costo_consulta * 0.85
        return self.costo_consulta

    def a_diccionario(self) -> dict:
        """Serializa la instancia a un diccionario con llaves en snake_case."""
        return {
            "id_cita": self.id_cita,
            "paciente": self.paciente,
            "especialidad": self.especialidad,
            "fecha": self.fecha,
            "costo_consulta": self.costo_consulta,
            "es_urgencia": self.es_urgencia,
            "costo_final": self.calcular_costo_final()
        }