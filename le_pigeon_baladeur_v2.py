#!/usr/bin/env python3
"""
#######################################################
#             AUTO-TRIEUR DE DOSSIER                  #
#      Projet Open Source - Le_Pigeon_Baladeur V2.0   #
#              Interface Tkinter                       #
#######################################################
Double-cliquer pour lancer. Aucune dépendance externe.
Compatible Linux / macOS / Windows.
"""

import threading
import tkinter as tk
from datetime import datetime
from pathlib import Path
from tkinter import filedialog, messagebox, ttk

# ===========================================================
#  CATALOGUE DES EXTENSIONS
# ===========================================================
CATEGORIES: dict[str, list[str]] = {
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif", ".svg", ".raw", ".webp",
        ".avif", ".heic", ".heif", ".tiff", ".tif", ".psd", ".ai",
        ".eps", ".bmp", ".ico", ".xcf", ".indd", ".sketch", ".fig",
    ],
    "Videos": [
        ".mp4", ".mov", ".mkv", ".webm", ".flv", ".avi", ".wmv",
        ".avchd", ".mxf", ".m4v", ".3gp", ".3g2", ".ogv", ".ts",
        ".vob", ".divx", ".rm", ".rmvb",
    ],
    "Documents": [
        ".docx", ".doc", ".odt", ".rtf", ".txt", ".pages",
        ".xlsx", ".xls", ".ods", ".csv", ".tsv",
        ".pptx", ".ppt", ".odp", ".key", ".pdf",
    ],
    "Musique": [
        ".mp3", ".wav", ".flac", ".m4a", ".aac", ".ogg", ".wma",
        ".aiff", ".aif", ".opus", ".mid", ".midi", ".ape", ".wv",
    ],
    "Archives": [
        ".rar", ".zip", ".7z", ".tar", ".gz", ".bz2", ".xz",
        ".sit", ".sitx", ".cab", ".iso", ".img", ".tgz", ".z",
    ],
    "Executables": [
        ".exe", ".msi", ".bat", ".cmd", ".ps1", ".app", ".pkg",
        ".apk", ".deb", ".rpm", ".sh", ".run", ".bin", ".out",
        ".appimage", ".snap",
    ],
    "Script-Dev": [
        ".py", ".js", ".ts", ".jsx", ".tsx", ".mjs", ".cjs",
        ".php", ".rb", ".go", ".rs", ".swift", ".kt",
        ".java", ".cs", ".cpp", ".c", ".h", ".hpp",
        ".r", ".lua", ".pl", ".scala", ".dart",
        ".html", ".htm", ".css", ".scss", ".sass", ".less",
        ".vue", ".svelte",
        ".json", ".jsonc", ".xml", ".yaml", ".yml",
        ".toml", ".ini", ".cfg", ".conf", ".env",
        ".sql", ".db", ".sqlite",
        ".md", ".mdx", ".rst",
        ".gitignore", ".gitattributes", ".editorconfig",
        ".log", ".lock", ".jar", ".wasm",
    ],
    "Polices":      [".ttf", ".otf", ".woff", ".woff2", ".eot"],
    "3D-CAO":       [".stl", ".obj", ".fbx", ".blend", ".dae", ".3ds", ".gltf", ".glb", ".step", ".stp"],
    "eBooks":       [".epub", ".mobi", ".azw", ".azw3", ".fb2"],
    "Images-Disque":[".vhd", ".vmdk", ".vdi", ".qcow2"],
}

EMOJI_CAT = {
    "Images": "🖼️", "Videos": "🎬", "Documents": "📄",
    "Musique": "🎵", "Archives": "📦", "Executables": "⚙️",
    "Script-Dev": "💻", "Polices": "🔤", "3D-CAO": "🧊",
    "eBooks": "📚", "Images-Disque": "💾",
}

# ===========================================================
#  COULEURS (dark industrial)
# ===========================================================
C = {
    "bg":      "#0f1117",
    "panel":   "#1a1d27",
    "border":  "#2a2d3a",
    "accent":  "#00d4aa",
    "accent2": "#ff6b35",
    "text":    "#e8eaf0",
    "muted":   "#6b7080",
    "success": "#4caf7d",
    "warning": "#f0a500",
    "error":   "#e05555",
    "row_a":   "#1a1d27",
    "row_b":   "#161820",
}

# ===========================================================
#  LOGIQUE MÉTIER
# ===========================================================
def build_index(catalogue):
    idx = {}
    for dossier, exts in catalogue.items():
        for ext in exts:
            idx[ext.lower()] = dossier
    return idx

EXT_INDEX = build_index(CATEGORIES)


def destination_unique(dossier_dest: Path, stem: str, suffix: str) -> Path:
    dest = dossier_dest / f"{stem}{suffix}"
    n = 1
    while dest.exists():
        dest = dossier_dest / f"{stem}({n}){suffix}"
        n += 1
    return dest


def simuler(dossier: Path) -> list[dict]:
    resultats = []
    for fichier in sorted(dossier.iterdir()):
        if not fichier.is_file():
            continue
        if fichier.name.startswith("tri_log_"):
            continue
        ext = fichier.suffix.lower()
        cat = EXT_INDEX.get(ext)
        nom_dossier = cat if cat else f"Autres/{ext.lstrip('.') or 'sans-extension'}"
        resultats.append({
            "fichier": fichier,
            "nom": fichier.name,
            "ext": ext or "(aucune)",
            "categorie": nom_dossier,
            "connu": cat is not None,
            "selected": True,
        })
    return resultats


def executer(actions: list[dict], dossier: Path) -> list[str]:
    log = []
    stats: dict[str, int] = {}
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log.append(f"{'─'*52}")
    log.append(f"  AUTO-TRIEUR OpenSource   —  {ts}")
    log.append(f"  Dossier : {dossier}")
    log.append(f"{'─'*52}")

    for action in actions:
        if not action.get("selected", True):
            log.append(f"  ⏭  Ignoré       {action['nom']}")
            continue
        fichier: Path = action["fichier"]
        if not fichier.exists():
            log.append(f"  ⚠  Introuvable  {action['nom']}")
            continue
        dest_dir = dossier / action["categorie"]
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = destination_unique(dest_dir, fichier.stem, fichier.suffix)
        fichier.rename(dest)
        cat = action["categorie"]
        stats[cat] = stats.get(cat, 0) + 1
        log.append(f"  ✅  {fichier.name}  →  {cat}/")

    log.append(f"{'─'*52}")
    log.append(f"  ✨ Terminé — {sum(stats.values())} fichier(s) déplacé(s)")
    for cat, nb in sorted(stats.items(), key=lambda x: -x[1]):
        log.append(f"     {cat:<26} {nb:>3} fichier(s)")

    log_path = dossier / f"tri_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    log_path.write_text("\n".join(log), encoding="utf-8")
    log.append(f"{'─'*52}")
    log.append(f"  📄 Log sauvegardé : {log_path.name}")
    return log


# ===========================================================
#  APPLICATION
# ===========================================================
class PigeonApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AUTO-TRIEUR OpenSource ")
        self.configure(bg=C["bg"])
        self.minsize(820, 560)
        self.geometry("980x680")
        self._centre()

        self._dossier: Path | None = None
        self._actions: list[dict] = []
        self._vars: list[tk.BooleanVar] = []

        self._build()

    def _centre(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth()  - 980) // 2
        y = (self.winfo_screenheight() - 680) // 2
        self.geometry(f"980x680+{x}+{y}")

    # ── BUILD ───────────────────────────────────────────────
    def _build(self):
        # Header
        hdr = tk.Frame(self, bg=C["bg"], pady=16)
        hdr.pack(fill="x", padx=24)
        tk.Label(hdr, text="AUTO-TRIEUR OpenSource",
                 bg=C["bg"], fg=C["accent"],
                 font=("Courier New", 20, "bold")).pack(side="left")
        tk.Label(hdr, text=" V2.0",
                 bg=C["bg"], fg=C["muted"],
                 font=("Courier New", 10)).pack(side="left", pady=(6, 0))

        tk.Frame(self, bg=C["border"], height=1).pack(fill="x", padx=24)

        # Barre dossier
        bar = tk.Frame(self, bg=C["panel"], pady=10, padx=16)
        bar.pack(fill="x", padx=24, pady=(12, 0))

        tk.Label(bar, text="Dossier :", bg=C["panel"], fg=C["muted"],
                 font=("Courier New", 9)).pack(side="left")

        self._lbl_chemin = tk.Label(bar, text="  (aucun sélectionné)",
                                    bg=C["panel"], fg=C["text"],
                                    font=("Courier New", 9), anchor="w")
        self._lbl_chemin.pack(side="left", fill="x", expand=True, padx=6)

        self._btn_sim = self._mk_btn(bar, "▶ Simuler",
                                     self._lancer_simulation,
                                     side="right", padx=(0, 8),
                                     state="disabled")
        self._mk_btn(bar, "📂 Parcourir", self._choisir_dossier, side="right")

        # Notebook
        style = ttk.Style(self)
        style.theme_use("default")
        style.configure("P.TNotebook", background=C["bg"], borderwidth=0)
        style.configure("P.TNotebook.Tab", background=C["border"],
                         foreground=C["muted"], padding=(14, 6),
                         font=("Courier New", 9, "bold"))
        style.map("P.TNotebook.Tab",
                  background=[("selected", C["panel"])],
                  foreground=[("selected", C["accent"])])

        self._nb = ttk.Notebook(self, style="P.TNotebook")
        self._nb.pack(fill="both", expand=True, padx=24, pady=10)

        self._f_sim = tk.Frame(self._nb, bg=C["bg"])
        self._nb.add(self._f_sim, text="  Simulation  ")
        self._build_sim_tab()

        self._f_rap = tk.Frame(self._nb, bg=C["bg"])
        self._nb.add(self._f_rap, text="  Rapport  ")
        self._build_rap_tab()

        # Footer
        ftr = tk.Frame(self, bg=C["bg"], pady=10)
        ftr.pack(fill="x", padx=24)

        self._lbl_status = tk.Label(ftr,
            text="Sélectionne un dossier pour commencer.",
            bg=C["bg"], fg=C["muted"], font=("Courier New", 9), anchor="w")
        self._lbl_status.pack(side="left", fill="x", expand=True)

        self._btn_exec = self._mk_btn(ftr, "🚀 Confirmer & Trier",
                                      self._executer, side="right",
                                      color=C["accent2"], state="disabled")

    def _build_sim_tab(self):
        ctrl = tk.Frame(self._f_sim, bg=C["bg"])
        ctrl.pack(fill="x", padx=4, pady=(8, 4))

        for txt, cmd, hover in [
            ("✔ Tout cocher",   self._tout_cocher,   C["accent"]),
            ("✘ Tout décocher", self._tout_decocher, C["error"]),
        ]:
            tk.Button(ctrl, text=txt, command=cmd,
                      bg=C["border"], fg=C["text"], relief="flat",
                      font=("Courier New", 8), cursor="hand2",
                      activebackground=hover, activeforeground=C["bg"],
                      padx=8, pady=3).pack(side="left", padx=4)

        self._lbl_count = tk.Label(ctrl, text="",
                                   bg=C["bg"], fg=C["muted"],
                                   font=("Courier New", 8))
        self._lbl_count.pack(side="right", padx=8)

        # Canvas scrollable
        cont = tk.Frame(self._f_sim, bg=C["bg"])
        cont.pack(fill="both", expand=True, padx=4, pady=4)

        self._canvas = tk.Canvas(cont, bg=C["bg"], highlightthickness=0)
        sb = ttk.Scrollbar(cont, orient="vertical",
                            command=self._canvas.yview)
        self._canvas.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y")
        self._canvas.pack(side="left", fill="both", expand=True)

        self._inner = tk.Frame(self._canvas, bg=C["bg"])
        self._cwin = self._canvas.create_window(
            (0, 0), window=self._inner, anchor="nw")
        self._inner.bind("<Configure>",
                         lambda _: self._canvas.configure(
                             scrollregion=self._canvas.bbox("all")))
        self._canvas.bind("<Configure>",
                          lambda e: self._canvas.itemconfig(
                              self._cwin, width=e.width))
        for seq in ("<MouseWheel>", "<Button-4>", "<Button-5>"):
            self._canvas.bind_all(seq, self._scroll)

    def _build_rap_tab(self):
        self._txt = tk.Text(self._f_rap, bg=C["panel"], fg=C["text"],
                            font=("Courier New", 9), relief="flat",
                            padx=14, pady=10, state="disabled", wrap="none")
        sb = ttk.Scrollbar(self._f_rap, command=self._txt.yview)
        self._txt.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y", pady=8)
        self._txt.pack(fill="both", expand=True, padx=(8, 0), pady=8)
        self._txt.tag_config("ok",   foreground=C["success"])
        self._txt.tag_config("skip", foreground=C["muted"])
        self._txt.tag_config("head", foreground=C["accent"],
                              font=("Courier New", 9, "bold"))
        self._txt.tag_config("warn", foreground=C["warning"])

    # ── HELPERS ─────────────────────────────────────────────
    def _mk_btn(self, parent, text, cmd, side="left",
                padx=(0, 0), color=None, state="normal"):
        b = tk.Button(parent, text=text, command=cmd,
                      bg=color or C["accent"], fg=C["bg"],
                      relief="flat", font=("Courier New", 9, "bold"),
                      cursor="hand2", state=state,
                      activebackground=C["text"], activeforeground=C["bg"],
                      padx=12, pady=5)
        b.pack(side=side, padx=padx)
        return b

    def _status(self, msg, color=None):
        self._lbl_status.config(text=msg, fg=color or C["muted"])

    def _scroll(self, event):
        if event.num == 4 or event.delta > 0:
            self._canvas.yview_scroll(-1, "units")
        else:
            self._canvas.yview_scroll(1, "units")

    # ── ACTIONS ─────────────────────────────────────────────
    def _choisir_dossier(self):
        candidates = [Path.home() / "Téléchargements", Path.home() / "Downloads"]
        initial = next((str(p) for p in candidates if p.exists()), str(Path.home()))
        chemin = filedialog.askdirectory(title="Dossier à trier", initialdir=initial)
        if chemin:
            self._dossier = Path(chemin)
            self._lbl_chemin.config(text=f"  {self._dossier}")
            self._btn_sim.config(state="normal")
            self._status("Dossier sélectionné — clique sur ▶ Simuler")

    def _lancer_simulation(self):
        if not self._dossier:
            return
        self._status("Analyse…", C["warning"])
        self._btn_sim.config(state="disabled")
        threading.Thread(target=lambda: self.after(
            0, lambda: self._afficher_simulation(simuler(self._dossier))
        ), daemon=True).start()

    def _afficher_simulation(self, actions: list[dict]):
        self._actions = actions
        self._vars.clear()

        for w in self._inner.winfo_children():
            w.destroy()

        if not actions:
            tk.Label(self._inner,
                     text="Aucun fichier à trier dans ce dossier.",
                     bg=C["bg"], fg=C["muted"],
                     font=("Courier New", 10)).pack(pady=30)
            self._status("Dossier vide.")
            return

        # En-têtes
        hdr = tk.Frame(self._inner, bg=C["border"])
        hdr.pack(fill="x", pady=(0, 2))
        for txt, w in [("", 3), ("Fichier", 38), ("Ext.", 9),
                       ("→ Destination", 28), ("Statut", 9)]:
            tk.Label(hdr, text=txt, width=w, bg=C["border"],
                     fg=C["muted"], font=("Courier New", 8, "bold"),
                     anchor="w").pack(side="left", padx=2)

        # Lignes
        for i, action in enumerate(actions):
            var = tk.BooleanVar(value=True)
            var.trace_add("write",
                          lambda *_, idx=i, v=var: self._on_toggle(idx, v))
            self._vars.append(var)

            bg = C["row_a"] if i % 2 == 0 else C["row_b"]
            row = tk.Frame(self._inner, bg=bg, pady=3)
            row.pack(fill="x")

            tk.Checkbutton(row, variable=var, bg=bg,
                           activebackground=bg, selectcolor=C["bg"],
                           fg=C["accent"], width=2).pack(side="left", padx=(4, 2))

            nom = action["nom"]
            nom_s = (nom[:42] + "…") if len(nom) > 42 else nom
            tk.Label(row, text=nom_s, width=38, bg=bg, fg=C["text"],
                     font=("Courier New", 9), anchor="w").pack(side="left", padx=2)

            tk.Label(row, text=action["ext"], width=9, bg=bg, fg=C["muted"],
                     font=("Courier New", 9), anchor="w").pack(side="left")

            emoji = EMOJI_CAT.get(action["categorie"].split("/")[0], "📁")
            tk.Label(row, text=f"{emoji} {action['categorie']}", width=28,
                     bg=bg,
                     fg=C["accent"] if action["connu"] else C["warning"],
                     font=("Courier New", 9), anchor="w").pack(side="left", padx=2)

            fg_s = C["success"] if action["connu"] else C["warning"]
            tk.Label(row, text="connu" if action["connu"] else "autre",
                     width=9, bg=bg, fg=fg_s,
                     font=("Courier New", 8), anchor="w").pack(side="left")

        self._update_count()
        self._btn_sim.config(state="normal")
        self._btn_exec.config(state="normal")
        self._nb.select(0)
        self._status(
            f"Simulation prête — {len(actions)} fichier(s) détecté(s). "
            "Décoche ce que tu veux laisser en place."
        )

    def _on_toggle(self, i, var):
        self._actions[i]["selected"] = var.get()
        self._update_count()

    def _update_count(self):
        coches = sum(1 for v in self._vars if v.get())
        self._lbl_count.config(
            text=f"{coches}/{len(self._vars)} sélectionné(s)"
        )

    def _tout_cocher(self):
        for v in self._vars: v.set(True)

    def _tout_decocher(self):
        for v in self._vars: v.set(False)

    def _executer(self):
        coches = [a for a in self._actions if a.get("selected")]
        if not coches:
            messagebox.showwarning("Rien à faire", "Aucun fichier sélectionné.")
            return
        if not messagebox.askyesno(
            "Confirmer le tri",
            f"Déplacer {len(coches)} fichier(s) vers leurs dossiers respectifs ?\n"
            "Cette action est difficile à annuler."
        ):
            return
        self._btn_exec.config(state="disabled")
        self._status("Tri en cours…", C["warning"])
        threading.Thread(target=lambda: self.after(
            0, lambda: self._afficher_rapport(executer(self._actions, self._dossier))
        ), daemon=True).start()

    def _afficher_rapport(self, log: list[str]):
        self._txt.config(state="normal")
        self._txt.delete("1.0", "end")
        for line in log:
            if "✅" in line:
                tag = "ok"
            elif "⏭" in line:
                tag = "skip"
            elif "⚠" in line:
                tag = "warn"
            elif any(c in line for c in ["─", "Pigeon", "✨", "📄", "Terminé", "Dossier"]):
                tag = "head"
            else:
                tag = ""
            self._txt.insert("end", line + "\n", tag)
        self._txt.config(state="disabled")
        self._nb.select(1)
        self._status("✨ Tri terminé ! Rapport dans l'onglet Rapport.", C["success"])


# ===========================================================
if __name__ == "__main__":
    PigeonApp().mainloop()
