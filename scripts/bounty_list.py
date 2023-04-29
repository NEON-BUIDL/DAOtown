from pathlib import Path
import os
import math
from gltflib import GLTF

# Lê todos os arquivos na pasta "model" e processa os arquivos glb.
model_path = Path(__file__).parent / "../models"
files = [f for f in os.listdir(model_path) if f.endswith('.glb')]
num_triangles_list = []
num_drawcalls_list = []
file_data = []

for file in files:
    file_path = model_path / file
    gltf = GLTF.load_glb(file_path)
    scene_index = gltf.model.scene
    scene = gltf.model.scenes[scene_index]

    num_triangles = 0
    num_drawcalls = 0

    for node_index in scene.nodes:
        node = gltf.model.nodes[node_index]
        if node.mesh is not None:
            mesh = gltf.model.meshes[node.mesh]
            mesh_primitives = mesh.primitives if mesh is not None else []
            num_drawcalls += len(mesh_primitives)

            for primitive in mesh_primitives:
                if 'POSITION' in primitive.attributes.__dict__:
                    num_triangles += gltf.model.accessors[primitive.attributes.POSITION].count // 3

    num_triangles_list.append(num_triangles)
    num_drawcalls_list.append(num_drawcalls)
    file_data.append((file, num_triangles, num_drawcalls))

# Calcula a média e o desvio padrão do número de triângulos e drawcalls.
mean_triangles = sum(num_triangles_list) / len(num_triangles_list)
std_dev_triangles = math.sqrt(sum([(x - mean_triangles) ** 2 for x in num_triangles_list]) / len(num_triangles_list))
mean_drawcalls = sum(num_drawcalls_list) / len(num_drawcalls_list)
std_dev_drawcalls = math.sqrt(sum([(x - mean_drawcalls) ** 2 for x in num_drawcalls_list]) / len(num_drawcalls_list))

# Define os limites aceitáveis para o número de triângulos e drawcalls.
MAX_TRIANGLES = mean_triangles + std_dev_triangles
MAX_DRAWCALLS = mean_drawcalls + std_dev_drawcalls

# Cria uma lista dos arquivos aptos para bounty.
bounty_list = []

for file, num_triangles, num_drawcalls in file_data:
    if num_triangles > MAX_TRIANGLES or num_drawcalls > MAX_DRAWCALLS:
        bounty_list.append(file)

# Imprime a lista dos arquivos aptos para bounty.
print("Arquivos aptos para bounty:")
for file in bounty_list:
    print(file)
