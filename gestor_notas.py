# gestor/gestor_notas.py
import csv, json

class GestorNotas:
    """Clase para gestionar notas de estudiantes"""

    def __init__(self, ruta_csv=None, ruta_txt=None, ruta_json=None):
        self.ruta_csv = ruta_csv
        self.ruta_txt = ruta_txt
        self.ruta_json = ruta_json
        self.datos = []
        self.config = {}
        self.lineas_txt = []

    def cargar_csv(self):
        """Carga datos desde un archivo CSV"""
        if not self.ruta_csv:
            raise ValueError("Debe proporcionar ruta_csv")
        with open(self.ruta_csv, encoding="utf-8") as f:
            self.datos = list(csv.DictReader(f))

    def cargar_txt(self):
        """Carga líneas desde archivo de texto"""
        if not self.ruta_txt:
            raise ValueError("Debe proporcionar ruta_txt")
        with open(self.ruta_txt, encoding="utf-8") as f:
            self.lineas_txt = [l.strip() for l in f]

    def cargar_json(self):
        """Carga configuración desde archivo JSON"""
        if not self.ruta_json:
            raise ValueError("Debe proporcionar ruta_json")
        with open(self.ruta_json, encoding="utf-8") as f:
            self.config = json.load(f)

    def filtrar_aprobados(self, minimo=6.0):
        """Devuelve lista de estudiantes con nota >= mínimo"""
        aprob = []
        for est in self.datos:
            try:
                if float(est["nota"]) >= minimo:
                    aprob.append(est)
            except:
                pass
        return aprob

    def promedio_general(self):
        """Promedio de todas las notas del CSV"""
        notas=[]
        for est in self.datos:
            try:
                notas.append(float(est["nota"]))
            except:
                pass
        return sum(notas)/len(notas) if notas else 0.0

    def resumen(self):
        """Devuelve resumen general del módulo"""
        return {
            "total_estudiantes": len(self.datos),
            "promedio_general": self.promedio_general(),
            "config": self.config
        }
