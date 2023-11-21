import torch

def check_device():
    '''
    Cette fonction ne prend pas d'argument.
    Cette fonction renvoie 2 éléments :
    1. Si CUDA est disponible sur la machine. 
    2. liste des GPU actifs.
    '''
    
    # Afficher si CUDA est disponible
    cuda_dispo = print(f"CUDA disponible : {torch.cuda.is_available()}")

    # Afficher le nom du GPU actif
    gpu_actif = print(f"GPU actif : {torch.cuda.get_device_name(0)}")

    return cuda_dispo, gpu_actif

check_device()