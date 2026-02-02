#######################################################
#             AUTO-TRIEUR DE DOSSIER                  #
#      Projet Open Source - Le_Pigeon_Baladeur V1.0   #
#######################################################

from pathlib import Path

# 1. CONFIGURATION DES EXTENSIONS
extensions_images = [".jpg", ".jpeg", ".png", ".gif", ".svg", ".raw", ".webp", ".avif", ".heic", ".heif", ".tiff", ".psd", ".ai", ".eps", ".bmp", ".ico"]
extensions_videos = [".mp4", ".mov", ".mkv", ".webm", ".flv", ".avi", ".wmv", ".avchd", ".mxf"]
extensions_documents = [".docx", ".odt", ".rtf", ".txt", ".xlsx", ".ods", ".csv", ".pptx", ".odp", ".pdf"]
extensions_musiques = [".mp3", ".wav", ".flac", ".m4a", ".aac"]
extensions_archives = [".rar", ".zip", ".7z", ".tar", ".gz", ".bz2", ".xz", ".sit", ".sitx", ".cab", ".iso"]
extensions_executables = [".exe", ".msi", ".bat", ".ps1", ".app", ".dmg", ".pkg", ".apk", ".deb", ".sh"]
extensions_script = [".py", ".js", ".php", ".jar", ".css", ".html", ".c", ".cpp", ".java", ".cs", ".rb", ".swift", ".json", ".xml", ".yaml", ".yml", ".sql", ".md", ".gitignore", ".log"]

# 2. DÉFINITION DU CHEMIN (Dynamique pour tout utilisateur Linux)
# Path.home() trouve automatiquement /home/utilisateur/
chemin_a_trier = Path.home() / "Téléchargements"

#######################################################
#                  FONCTION DE TRI                    #
#######################################################

def ranger_fichier(fichier, nom_dossier):
    """Crée le dossier si besoin, gère les doublons et déplace le fichier."""

    # Création du dossier de destination dans le répertoire courant
    dossier_dest = chemin_a_trier / nom_dossier
    dossier_dest.mkdir(exist_ok=True)

    # Définition de la destination initiale
    destination = dossier_dest / fichier.name

    # GESTION DES DOUBLONS
    # Si le fichier existe déjà, ajoute (1), (2), etc.
    compteur = 1
    while destination.exists():
        nouveau_nom = f"{fichier.stem}({compteur}){fichier.suffix}"
        destination = dossier_dest / nouveau_nom
        compteur += 1

    # Déplacement du fichier
    fichier.rename(destination)
    print(f"✅ {fichier.name} -> {nom_dossier}/")

#######################################################
#                BOUCLE PRINCIPALE                    #
#######################################################

def main():
    print(f"🚀 Démarrage du tri dans : {chemin_a_trier}")

    if not chemin_a_trier.exists():
        print("❌ Erreur : Le dossier spécifié n'existe pas.")
        return

    # Parcourt chaque élément du dossier
    for fichier in chemin_a_trier.iterdir():
        if fichier.is_file():
            extension = fichier.suffix.lower()

            # Vérification des catégories
            if extension in extensions_images:
                ranger_fichier(fichier, "Images")
            elif extension in extensions_videos:
                ranger_fichier(fichier, "Videos")
            elif extension in extensions_documents:
                ranger_fichier(fichier, "Documents")
            elif extension in extensions_musiques:
                ranger_fichier(fichier, "Musique")
            elif extension in extensions_archives:
                ranger_fichier(fichier, "Archives")
            elif extension in extensions_executables:
                ranger_fichier(fichier, "Executables")
            elif extension in extensions_script:
                ranger_fichier(fichier, "Script-Dev")

    print("✨ Tri terminé !")

if __name__ == "__main__":
    main()
