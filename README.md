# Le Pigeon Baladeur - Auto-Trieur de Dossier_V2

![Python Version](https://img.shields.io/badge/Python_3.10%2B-blue?style=for-the-badge\&logo=python\&logoColor=white)
![Platform](https://img.shields.io/badge/Windows_|_macOS_|_Linux-lightgrey?style=for-the-badge)
![License](https://img.shields.io/badge/Licence_MIT-green?style=for-the-badge)


---

## ✨ Aperçu

Marre de voir votre dossier **Téléchargements** devenir un chaos total ?<br>
**Le Pigeon Baladeur V2** est un utilitaire Python avec interface graphique qui trie automatiquement vos fichiers selon leur type.

💡 Simple, rapide, sans dépendances externes.

---

## Interface

<p align="center">
  <kbd>
    <img src="https://github.com/lepigeonbaladeur/Auto-Trieur-de-Dossier/blob/main/Screenshot.png" alt="Auto-Trieur-de-Dossier Screenshot" width="850">
  </kbd>
</p>


---

## 🛠️ Fonctionnalités

* 🎨 Interface graphique (Tkinter)
* 🔍 Mode simulation (preview avant tri)
* ✅ Sélection manuelle des fichiers à déplacer
* 📦 Zéro dépendance externe
* 🔁 Gestion intelligente des conflits de noms
* 🧾 Logs détaillés + rapport automatique

---

## Installation & Utilisation

### ▶️ Lancer le script

```bash
git clone https://github.com/lepigeonbaladeur/Auto-Trieur-de-Dossier.git
cd Auto-Trieur-de-Dossier
python le_pigeon_baladeur_v2.py
```

---

### ⚙️ Version exécutable (sans Python)

#### 1. Installer PyInstaller

```bash
pip install pyinstaller
```

#### 2. Compiler

```bash
python -m PyInstaller --onefile --windowed le_pigeon_baladeur_v2.py
```

#### 3. Résultat

```
dist/
```

---

## 🗂️ Types de fichiers gérés

| Catégorie      | Extensions                         |
| -------------- | ---------------------------------- |
| 🖼️ Images     | jpg, png, webp, svg, psd, ai       |
| 🎬 Vidéos      | mp4, mkv, avi, mov, webm           |
| 📄 Documents   | pdf, docx, xlsx, csv, txt          |
| 🎵 Musique     | mp3, wav, flac, ogg                |
| 📦 Archives    | zip, rar, 7z, tar, iso             |
| ⚙️ Exécutables | exe, msi, deb, app, sh             |
| 💻 Dev         | py, js, cpp, json, sql, html, yaml |
| 📁 Autres      | polices, 3D, eBooks, images disque |

> Les fichiers inconnus sont classés automatiquement dans `Autres/`.

---

##  Concepts techniques utilisés

* `pathlib` → gestion de fichiers
* `tkinter` → interface graphique
* `threading` → fluidité UI
* structures de données (dict)

## 👨‍🎓 Contexte

Projet personnel réalisé dans le cadre de ma préparation au **BUT Informatique**.

---

## 📜 Licence

Licence MIT — libre d'utilisation, modification et distribution.

---

---

> [!NOTE]
> **Garantie** : Ce projet est fourni "tel quel", sans garantie d'aucune sorte.
> **Responsabilité** : L'auteur décline toute responsabilité en cas de bug ou de perte de données. L'utilisateur assume l'entière responsabilité de son utilisation et de ses modifications.

---
## ☕ Support

Si ce projet t'aide :

⭐ Laisse une étoile
🐛 Ouvre une issue
💡 Propose des idées

---

**Développé avec logique, café et un peu de chaos maîtrisé.**


