# Tarea 1: Añadir la clase derivada Camion
class Vehiculo():
    def __init__(self, marca, modelo, año):
        self.__marca = marca  # Encapsulamiento
        self.__modelo = modelo  # Encapsulamiento
        self.__año = año  # Encapsulamiento

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_año(self):
        return self.__año

    def set_año(self, año):
        self.__año = año

    # Tarea 4: Método detener
    def detener(self):
        print(f"El vehículo {self.get_marca()} {self.get_modelo()} se está deteniendo.")  # Abstracción

class Auto(Vehiculo):  # Herencia
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)
        self.__puertas = puertas  # Encapsulamiento

    def get_puertas(self):
        return self.__puertas

    def set_puertas(self, puertas):
        self.__puertas = puertas

    def acelerar(self):  # Polimorfismo
        print(f"El auto {self.get_marca()} {self.get_modelo()} está acelerando.")

    def detener(self):  # Polimorfismo
        print(f"El auto {self.get_marca()} {self.get_modelo()} se está deteniendo.")

class Motocicleta(Vehiculo):  # Herencia
    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)
        self.__cilindrada = cilindrada  # Encapsulamiento

    def get_cilindrada(self):
        return self.__cilindrada

    def set_cilindrada(self, cilindrada):
        self.__cilindrada = cilindrada

    def acelerar(self):  # Polimorfismo
        print(f"La motocicleta {self.get_marca()} {self.get_modelo()} con cilindrada de {self.get_cilindrada()}cc está acelerando.")

    def detener(self):  # Polimorfismo
        print(f"La motocicleta {self.get_marca()} {self.get_modelo()} se está deteniendo.")

# Tarea 1: Clase Camion
class Camion(Vehiculo):  # Herencia
    def __init__(self, marca, modelo, año, capacidad_carga):
        super().__init__(marca, modelo, año)
        self.__capacidad_carga = capacidad_carga  # Encapsulamiento

    def get_capacidad_carga(self):
        return self.__capacidad_carga

    def set_capacidad_carga(self, capacidad_carga):
        self.__capacidad_carga = capacidad_carga

    def acelerar(self):  # Polimorfismo
        print(f"El camión {self.get_marca()} {self.get_modelo()} con capacidad de {self.get_capacidad_carga()} toneladas está acelerando.")

    def detener(self):  # Polimorfismo
        print(f"El camión {self.get_marca()} {self.get_modelo()} se está deteniendo.")


# Tarea 2: Modificación del almacenamiento de vehículos en un diccionario
if __name__ == "__main__":
    vehiculos = {
        "Corolla": Auto("Toyota", "Corolla", 2020, 4),
        "MT-07": Motocicleta("Yamaha", "MT-07", 2019, 689),
        "Camioneta": Camion("Lamborghini", "Actros", 2018, 18)
    }

    for modelo, vehiculo in vehiculos.items():
        vehiculo.acelerar()
        vehiculo.detener()

