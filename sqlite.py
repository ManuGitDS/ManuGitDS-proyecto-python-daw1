import sqlite3

conn = sqlite3.connect("salines.db")
cursor = conn.cursor()

# Actualizar el primer apellido del alumno con id 1
cursor.execute(
    "UPDATE profesores SET primer_apellido = ?, segundo_apellido = ? WHERE id_profesor = ?",
    ("Fillol", "Rodriguez", 19)
)

conn.commit()
conn.close()

print("Actualización completada.")
