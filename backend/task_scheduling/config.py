

def load_config(file_path='config.txt'):
    config = {}

    try:
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()

                if not line or line.startswith("#"):
                    continue  

                if ':' in line:
                    key, value = line.split(":", 1)
                    config[key.strip()] = int(value.strip())

    except FileNotFoundError:
        raise RuntimeError(f"Arquivo de configuração '{file_path}' não encontrado.")

    return config
