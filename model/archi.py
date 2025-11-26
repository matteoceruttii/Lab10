from dataclasses import dataclass

# classe che gestisce gli archi tra Hub
@dataclass
class Archi:
    id_hub_origine: int
    id_hub_destinazione: int
    valore_totale: float
    n_spedizioni: int

    def __eq__(self, other):
        return isinstance(other, Archi) and self.id_hub_origine == other.id_hub_origine

    def __str__(self):
        return f'{self.id_hub_origine} {self.id_hub_destinazione} - {self.valore_totale}'

    def get_valore_medio(self):
        return self.valore_totale / self.n_spedizioni if self.n_spedizioni > 0 else 0