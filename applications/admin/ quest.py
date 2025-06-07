"""Missões, tarefas e progresso"""

class Quest:
    def __init__(self, id, titulo, descricao, xp_recompensa):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.xp_recompensa = xp_recompensa
        self.completada = False

    def completar(self):
        self.completada = True
