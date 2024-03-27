from Mesa import MesaDeJogo

ms = MesaDeJogo(2)

print("Saco: \n", ms.pocket)
print("Mesa de fabricas: \n", ms.factory_board)
print("Chao de fabrica: \n", ms.factory_floor)

ms.manufacture_board()

print("Saco: \n", ms.pocket)
print("Mesa de fabricas: \n", ms.factory_board)
print("Chao de fabrica: \n", ms.factory_floor)

print("pegado >>> ",ms.pick_ceramic(0, 3))
print("Saco: \n", ms.pocket)
print("Mesa de fabricas: \n", ms.factory_board)
print("Chao de fabrica: \n", ms.factory_floor)