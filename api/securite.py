"""Gestion des cles d'API et des roles (TP2)."""
import os
import secrets
from pathlib import Path
from typing import Annotated, Callable

from fastapi import Depends, HTTPException, Security
from fastapi.security import APIKeyHeader

EN_TETE = APIKeyHeader(name="X-API-Key", auto_error=False)
LONGUEUR_MIN = 16
ROLES = {"client", "admin"}
NON_AUTHENTIFIE = {"WWW-Authenticate": "ApiKey"}


def _charger_dotenv() -> None:
    """Lit .env a la racine du projet, s'il existe, et definit les variables."""
    racine = Path(__file__).resolve().parents[1]
    env_file = racine / ".env"
    if not env_file.exists():
        return
    for ligne in env_file.read_text(encoding="utf-8").splitlines():
        ligne = ligne.strip()
        if not ligne or ligne.startswith("#") or "=" not in ligne:
            continue
        cle, _, valeur = ligne.partition("=")
        cle = cle.strip()
        valeur = valeur.strip().strip('"').strip("'")
        if cle and cle not in os.environ:
            os.environ[cle] = valeur


# Charge .env au moment de l'import du module
_charger_dotenv()


def charger_cles(brut: str | None = None) -> dict[str, str]:
    """Liste API_KEYS. Sans cle configuree, personne n'entre : on ferme par defaut."""
    brut = os.environ.get("API_KEYS", "") if brut is None else brut
    cles: dict[str, str] = {}
    for entree in filter(None, (morceau.strip() for morceau in brut.split(","))):
        cle, _, role = entree.rpartition(":")
        if role not in ROLES:
            raise ValueError(f"role inconnu dans API_KEYS : {role!r} (attendu : client ou admin)")
        if len(cle) < LONGUEUR_MIN:
            raise ValueError(f"cle trop courte dans API_KEYS ({len(cle)} caracteres, minimum {LONGUEUR_MIN})")
        cles[cle] = role
    return cles


def identifier(cle: Annotated[str | None, Security(EN_TETE)]) -> str:
    """Authentification : renvoie le role de l'appelant, ou leve une 401."""
    if not cle:
        raise HTTPException(401, "Cle d'API manquante : en-tete X-API-Key", headers=NON_AUTHENTIFIE)
    for connue, role in charger_cles().items():
        if secrets.compare_digest(cle.encode(), connue.encode()):
            return role
    raise HTTPException(401, "Cle d'API invalide", headers=NON_AUTHENTIFIE)


def exiger(*autorises: str) -> Callable[[str], str]:
    """Autorisation : fabrique une dependance qui n'accepte que les roles donnes."""
    def verifier(role: Annotated[str, Depends(identifier)]) -> str:
        if role not in autorises:
            raise HTTPException(403, f"Acces refuse au role « {role} »")
        return role
    return verifier
