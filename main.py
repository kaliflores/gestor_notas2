from gestor.gestor_notas import GestorNotas

def main():
    gestor = GestorNotas(
        ruta_csv="data/alumnos.csv",
        ruta_txt="data/notas.txt",
        ruta_json="data/config.json"
    )

    gestor.cargar_csv()
    gestor.cargar_txt()
    gestor.cargar_json()

    print("=== Resumen General ===")
    print(gestor.resumen())

    print("\n=== Aprobados ===")
    for a in gestor.filtrar_aprobados():
        print(a)

    print("\n=== TXT ===")
    for l in gestor.lineas_txt:
        print(" -", l)

if __name__ == "__main__":
    main()
