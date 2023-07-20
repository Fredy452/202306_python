import modulos


gato = modulos.Mascota("Michifuz", "Normal", "no come", 10, 10)

ninja = modulos.Ninja("Naruto", "No se", gato, "purina", "purina")

ninja.alimentar("pescado")
print(ninja)
gato.mostrar_macota()