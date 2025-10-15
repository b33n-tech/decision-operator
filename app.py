import re
from typing import List, Dict, Set

class AnalyseurImplicites:
    def __init__(self):
        self.mots_ambigu = {
            'coordination': ['sans_autorite', 'responsabilite_cachee'],
            'collaboration': ['dependance_cachee', 'effort_asymetrique'],
            'opportunité': ['charge_cachee', 'urgence_artificielle'],
            'flexibilité': ['contournement_procedure', 'precedent_dangereux'],
            'confiance': ['decharge_responsabilite', 'attente_implicite']
        }
        
        self.mots_danger = {
            'simple': ['complexite_cachee'],
            'rapide': ['qualite_sacrifiee'],
            'temporaire': ['perennisation_cachee'],
            'standard': ['adaptation_necessaire'],
            'normal': ['procedure_contournee']
        }
        
        self.verbes_transfert = ['coordonner', 'faciliter', 'superviser', 'animer', 'relayer']
        
    def analyser_instruction(self, texte: str) -> Dict:
        texte_lower = texte.lower()
        
        resultats = {
            'implicites_detectes': [],
            'dependances_cachees': self._detecter_dependances(texte_lower),
            'transferts_responsabilite': self._detecter_transferts(texte_lower),
            'scenarios_risque': self._generer_scenarios_risque(texte_lower),
            'checklist_actions': self._generer_checklist(texte_lower),
            'questions_clarification': self._generer_questions(texte_lower)
        }
        
        # Détection des patterns d'ambiguïté
        resultats['implicites_detectes'].extend(self._scanner_mots_ambigu(texte_lower))
        resultats['implicites_detectes'].extend(self._scanner_mots_danger(texte_lower))
        
        return resultats
    
    def _detecter_dependances(self, texte: str) -> List[str]:
        dependances = []
        patterns = [
            (r'sous réserve de (.+?)', 'Dépendance conditionnelle détectée'),
            (r'en coordination avec (.+?)', 'Dépendance humaine externe'),
            (r'sur la base de (.+?)', 'Dépendance documentaire'),
            (r'après (.+?)', 'Séquence imposée'),
            (r'une fois que (.+?)', 'Prérequis caché')
        ]
        
        for pattern, message in patterns:
            matches = re.finditer(pattern, texte)
            for match in matches:
                dependances.append(f"{message} : '{match.group(1)}'")
        
        return dependances
    
    def _detecter_transferts(self, texte: str) -> List[str]:
        transferts = []
        
        for verbe in self.verbes_transfert:
            if verbe in texte:
                pattern = rf'{verbe}\s+(.+?)(?=\.|,|$)'
                matches = re.finditer(pattern, texte)
                for match in matches:
                    transferts.append(f"Transfert de charge : '{match.group(0)}' → Responsabilité sans autorité")
        
        return transferts
    
    def _scanner_mots_ambigu(self, texte: str) -> List[str]:
        implicites = []
        for mot, risques in self.mots_ambigu.items():
            if mot in texte:
                implicites.extend(risques)
        return list(set(implicites))
    
    def _scanner_mots_danger(self, texte: str) -> List[str]:
        dangers = []
        for mot, risques in self.mots_danger.items():
            if mot in texte:
                dangers.extend(risques)
        return list(set(dangers))
    
    def _generer_scenarios_risque(self, texte: str) -> List[str]:
        scenarios = ["SCÉNARIO RÉALISTE : Retards, non-réponses, blocages silencieux"]
        
        if any(mot in texte for mot in ['urgent', 'rapide', 'délai']):
            scenarios.append("SCÉNARIO URGENCE : Qualité sacrifiée, stress accru, erreurs probables")
        
        if any(mot in texte for mot in ['coordination', 'collaboration']):
            scenarios.append("SCÉNARIO COORDINATION : Attente passive, délais indéfinis, responsabilité diluée")
        
        return scenarios
    
    def _generer_checklist(self, texte: str) -> List[str]:
        checklist = [
            "☐ Identifier QUI a réellement l'autorité",
            "☐ Lister TOUTES les parties prenantes implicites", 
            "☐ Documenter par écrit les attendus exacts",
            "☐ Prévoir 30% de temps supplémentaire pour les blocages",
            "☐ Anticiper le scénario du pire acteur"
        ]
        
        if 'budget' in texte or 'coût' in texte:
            checklist.append("☐ Obtenir validation écrite des engagements financiers")
        
        return checklist
    
    def _generer_questions(self, texte: str) -> List[str]:
        questions = [
            "Qui a l'autorité réelle de décision ?",
            "Que se passe-t-il si une partie prenante ne répond pas ?",
            "Quel est le budget ALLOUÉ (pas estimé) ?",
            "Qui porte la responsabilité finale en cas d'échec ?"
        ]
        return questions

# UTILISATION
if __name__ == "__main__":
    analyseur = AnalyseurImplicites()
    
    instruction = """
    Nous avons une opportunité de coordonner le projet Innovation 
    en collaboration avec les équipes métier. C'est une action simple 
    et rapide qui nécessite votre flexibilité. Sous réserve de 
    l'accord de la direction, une fois que les équipes techniques 
    auront donné leur feu vert.
    """
    
    resultat = analyseur.analyser_instruction(instruction)
    
    print("=== ANALYSE IMPITOYABLE ===")
    for categorie, elements in resultat.items():
        print(f"\n{categorie.upper()}:")
        for element in elements:
            print(f"  • {element}")
