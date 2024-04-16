import os

def get_secret(name):
    """
    Fonction pour récupérer une variable d'environnement sensible à partir des secrets GitHub.
    
    Args:
        name (str): Nom de la variable d'environnement à récupérer.
        
    Returns:
        str: Valeur de la variable d'environnement.
    """
    if name in os.environ:
        return os.environ[name]
    else:
        raise ValueError(f"Variable d'environnement '{name}' non trouvée.")

def main():
    # Exemple d'utilisation pour récupérer une variable d'environnement sécurisée
    api_key = get_secret("API_KEY")
    print("API Key:", api_key)

if __name__ == "__main__":
    main()
