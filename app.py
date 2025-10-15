import re
from typing import Dict, List

class GenerateurCadrage:
    def __init__(self):
        # Les catégories de cadrage fondamentales
        self.sections = {
            "Contexte": [
                "Quel est le contexte réel du projet ?",
                "Qui a initié la demande ?",
                "Quel problème cela est-il censé résoudre ?"
            ],
            "Objectifs": [
                "Quels sont les objectifs explicites ?",
                "Quels sont les objectifs implicites (non dits mais attendus) ?",
                "Y a-t-il un objectif prioritaire ?"
            ],
            "Moyens et contraintes": [
                "Quel est le budget disponible (ou à confirmer) ?",
                "Quel est le délai ?",
                "Quelles ressources humaines sont impliquées ?",
                "Y a-t-il des contraintes techniques, légales ou politiques connues ?"
            ],
            "Parties prenantes": [
                "Qui sont les acteurs directement impliqués ?",
                "Qui sont les acteurs indirectement impactés ?",
                "Qui décide réellement (autorité finale) ?",
                "Qui exécute (responsable opérationnel) ?"
            ],
            "Livrables et critères de succès": [
                "Quels sont les livrables attendus ?",
                "Quels critères permettront de dire que le projet est réussi ?",
                "Quels risques majeurs peuvent bloquer le succès ?"
            ]
        }

    def generer_template(self, phrase_projet: str) -> Dict:
        """
        Génère un template de cadrage dynamique à partir d'une phrase d'entrée floue.
        """
        # Essayer d'extraire automatiquement nom, action, et parties prenantes
        nom_projet = self._extraire_nom_projet(phrase_projet)
        action = self._extraire_action(phrase_projet)
        acteurs = self._extraire_acteurs(phrase_projet)

        # Générer le texte à trous
        texte_cadrage = self._generer_texte_cadrage(nom_projet, action, acteurs)
        json_cadrage = self._generer_json_structure(texte_cadrage)

        return {"texte": texte_cadrage, "structure": json_cadrage}

    def _extraire_nom_projet(self, texte: str) -> str:
        match = re.search(r"projet\s+([A-Za-z0-9\- ]+)", texte, re.IGNORECASE)
        return match.group(1).strip() if match else "Nom du projet à préciser"

    def _extraire_action(self, texte: str) -> str:
        match = re.search(r"faire\s+([A-Za-z0-9\- ]+)", texte, re.IGNORECASE)
        return match.group(1).strip() if match else "Objectif à clarifier"

    def _extraire_acteurs(self, texte: str) -> List[str]:
        acteurs = re.findall(r"avec\s+([A-Za-z0-9\- ,]+)", texte, re.IGNORECASE)
        if acteurs:
            return [a.strip() for a in acteurs[0].split(",")]
        return ["Parties prenantes à identifier"]

    def _generer_texte_cadrage(self, nom_projet: str, action: str, acteurs: List[str]) -> str:
        texte = f"""
=== CADRAGE AUTOMATIQUE ===

🧩 Projet : {nom_projet}
🎯 Objectif déclaré : {action}
👥 Parties mentionnées : {', '.join(acteurs)}

--- CONTEXTE ---
{self._texte_a_trous(self.sections['Contexte'])}

--- OBJECTIFS ---
{self._texte_a_trous(self.sections['Objectifs'])}

--- MOYENS ET CONTRAINTES ---
{self._texte_a_trous(self.sections['Moyens et contraintes'])}

--- PARTIES PRENANTES ---
{self._texte_a_trous(self.sections['Parties prenantes'])}

--- LIVRABLES ET CRITÈRES DE SUCCÈS ---
{self._texte_a_trous(self.sections['Livrables et critères de succès'])}

🧠 Pense-bête :
- Tout ce qui n’est pas clarifié maintenant deviendra un problème plus tard.
- Si tu ne sais pas “qui décide”, c’est toi par défaut.
"""
        return texte.strip()

    def _texte_a_trous(self, questions: List[str]) -> str:
        return "\n".join([f"• {q} → [_________________________]" for q in questions])

    def _generer_json_structure(self, texte: str) -> Dict:
        # Structure JSON réutilisable ou exportable vers interface
        structure = {}
        for section, questions in self.sections.items():
            structure[section] = [{"question": q, "réponse": ""} for q in questions]
        return structure


# --- UTILISATION ---
if __name__ == "__main__":
    generateur = GenerateurCadrage()
    
    phrase = "On m’a filé le projet Horizon où ils veulent faire un prototype rapide avec les équipes data et design. Je n’ai eu que ça comme info."
    
    resultat = generateur.generer_template(phrase)
    
    print(resultat["texte"])
