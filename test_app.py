"""
Arquivo que testa a função de soma
"""

from app import soma

def test_soma():
    """
    Função que testa a função de soma
    """
    assert soma(2, 3) == 5
