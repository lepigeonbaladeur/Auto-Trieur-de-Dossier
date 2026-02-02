# ✨ Auto-Trieur de Dossier (Python) ✨

![Python Version](https://img.shields.io/badge/Python_3.10%2B-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Platform](https://img.shields.io/badge/Linux_Compatible-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![License](https://img.shields.io/badge/Licence_MIT-3DDC84?style=for-the-badge&logo=open-source-initiative&logoColor=white)

---

## 🗂️ Adieu le Désordre, Bonjour l'Organisation Automatisée !

**Fatigué de voir votre dossier "Téléchargements" se transformer en champ de bataille numérique ?** Cet **Auto-Trieur de Dossier** est la solution pour un espace de travail Linux impeccable. Développé avec passion en Python, il transforme le chaos en ordre structuré en un clin d'œil.

## 🌟 Points Forts du Projet

-   **⚡ Performance & Simplicité** : Un script Python léger et efficace.
-   **🎯 Tri Intelligent Multi-Catégories** : Reconnaissance et classement automatique dans des dossiers spécifiques (Photos , Vidéos , Docs , Musique , Archives , et bien plus !).
-   **🛡️ Gestion Anti-Perte de Données** : Fini les écrasements ! Les fichiers existants sont intelligemment renommés (ex: `rapport(1).pdf`).
-   **🌍 Compatibilité Universelle Linux** : Conçu pour s'adapter à n'importe quel utilisateur, n'importe où sur Linux grâce à `Path.home()`.
-   **🧱 Code** : Facile à comprendre, à modifier et à étendre.

## 🚀 Mise en Route (C'est Facile !)

### Prérequis
Assurez-vous d'avoir [Python 3.10 ou supérieur](https://www.python.org/downloads/) installé sur votre système Linux.

### 📥 Option 1 : Lancez le script directement

1.  Clonez ce dépôt pour obtenir le code :
    ```bash
    git clone https://github.com/lepigeonbaladeur/Auto-Trieur-de-Dossier.git
    cd Auto-Trieur-de-Dossier
    ```
2.  Exécutez l'outil :
    ```bash
    python3 trieur.py
    ```

### 📦 Option 2 : Créez une application autonome (Exécutable)

Pour une utilisation sans Python préinstallé, transformez-le en binaire !

1.  Installez `PyInstaller` (si ce n'est pas déjà fait) :
    ```bash
    pip install pyinstaller
    ```
2.  Générez le fichier exécutable :
    ```bash
    python3 -m PyInstaller --onefile trieur.py
    ```
3.  Vous trouverez votre application prête à l'emploi dans le dossier `dist/`.

## 🗃️ Votre Dossier, Mieux Organisé !

Voici un aperçu des catégories que cet outil prend en charge :

| Dossier de Destination | Types de Fichiers | Exemples d'Extensions |
| :-------------------- | :---------------- | :-------------------- |
| **Images** 📸         | Photos, graphiques | `.jpg`, `.png`, `.gif`, `.svg`, `.webp`, `.psd` |
| **Videos** 🎬         | Films, clips, tutoriels | `.mp4`, `.mov`, `.mkv`, `.avi`, `.wmv` |
| **Documents** 📄      | Rapports, PDFs, Tableurs | `.pdf`, `.docx`, `.txt`, `.xlsx`, `.csv`, `.pptx` |
| **Musique** 🎶        | Pistes audio | `.mp3`, `.wav`, `.flac`, `.m4a` |
| **Archives** 🗜️       | Fichiers compressés | `.zip`, `.rar`, `.7z`, `.tar`, `.iso` |
| **Script-Dev** 💻     | Code source, scripts | `.py`, `.js`, `.html`, `.cpp`, `.sql`, `.json` |
| **Executables** ⚙️    | Programmes installables | `.exe`, `.dmg`, `.deb`, `.sh`, `.apk` |

## 👨‍🎓 Mon Parcours & Motivation (Futur BUT Informatique)

Ce projet est une étape clé dans ma préparation pour le **BUT Informatique**. Il démontre ma passion pour le développement, ma capacité à concrétiser des idées et mon engagement envers la philosophie Open Source. J'aspire à approfondir ces compétences et à contribuer activement au monde du logiciel.

---

## 📜 Licence

Ce projet est distribué sous la [Licence MIT](LICENSE). N'hésitez pas à explorer, modifier et partager !

---
*Développé avec ❤️ et logique en Python.*
