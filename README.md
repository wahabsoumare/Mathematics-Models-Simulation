# 🧪 Simulation des Modèles Épidémiologiques SIR et SIRS en Python

Ce projet simule deux modèles classiques d'évolution de maladies infectieuses :  
- **SIR** : Susceptibles – Infectés – Rétablis  
- **SIRS** : Susceptibles – Infectés – Rétablis – redevenus Susceptibles (avec perte d’immunité)

Ces modèles sont implémentés en Python et visualisés à l’aide de graphiques et animations avec `matplotlib`.

---

## 📁 Structure du projet

```
📂 SIR_Model/
├── sir_model.py         # Modèle SIR
├── sirs_model.py        # Modèle SIRS
├── requirements.txt     # Dépendances exactes du projet
├── README.md            # Documentation du projet
```

---

## 📦 Installation

### 1. Cloner le projet

```bash
git clone https://github.com/wahabsoumare/Mathematics-Models-Simulation
cd Mathematics-Models-Simulation
```

### 2. (Optionnel) Créer un environnement virtuel

```bash
python3 -m venv env
source ./env/bin/activate       # Linux/macOS
env\Scripts\activate        # Windows
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

```
matplotlib==3.9.0
numpy==1.26.4
scipy==1.13.1
```

---

## ▶️ Utilisation

### 🔹 Simulation du modèle SIR

```bash
python3 sir_model.py
```

#### Exemple de configuration :

```python
model = SIR(beta = 0.3, gamma = 0.1, N = 1000)
model.solve(I0 = 1, R0 = 0)
model.simulate()
```

---

### 🔹 Simulation du modèle SIRS

```bash
python3 sirs_model.py
```

#### Exemple de configuration :

```python
model = SIRS(beta = 0.3, gamma = 0.1, delta = 0.1, N = 1000)
model.solve()
model.simulate()
```


## 🎥 Résultat

- 📈 **Graphiques statiques** via `show_graph()`
- 🎞️ **Animations dynamiques** avec `matplotlib.animation.FuncAnimation`

---

## 🔧 Améliorations possibles

- Ajouter d'autres modèles (SEIR, SEIRS)
- Intégrer une interface graphique (Tkinter, Streamlit)
- Comparer avec des données réelles
- Faire une analyse de sensibilité sur les paramètres β, γ, δ

---

## 👨‍💻 Auteur

**Abdoul Wahab Soumare**  
Master 2 Bio-informatique et Biomathématiques – UCAD

---

## 📄 Licence

Projet open-source à usage académique, personnel ou éducatif.

---
