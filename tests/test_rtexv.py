import copy
import importlib.machinery
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
_l = importlib.machinery.SourceFileLoader('rtexv', str(RAIZ / 'bin' / 'rtexv'))
_s = importlib.util.spec_from_loader('rtexv', _l)
rtexv = importlib.util.module_from_spec(_s)
_l.exec_module(rtexv)


def base():
    return json.loads((RAIZ / 'exemplos' / 'cirurgia-raio-x' / 'roteiro.json').read_text(encoding='utf-8'))


class Checar(unittest.TestCase):
    def test_exemplos_publicados_passam(self):
        pastas = sorted((RAIZ / 'exemplos').glob('*/roteiro.json'))
        self.assertEqual(len(pastas), 3)
        for p in pastas:
            self.assertEqual(rtexv.checar(json.loads(p.read_text(encoding='utf-8')))[0], [], p)

    def test_limite_de_blocos(self):
        r = base()
        r['blocos'] = r['blocos'][:3] + r['blocos'][-1:]
        self.assertTrue(any('blocos' in e for e in rtexv.checar(r)[0]))

    def test_fala_longa_demais(self):
        r = base()
        r['blocos'][1]['fala'] += ' palavra' * 400
        self.assertTrue(any('caracteres' in e for e in rtexv.checar(r)[0]))

    def test_exige_gancho_virada_e_destino(self):
        for campo, texto in (('gancho', 'Gancho'), ('virada', 'Virada')):
            r = copy.deepcopy(base())
            for b in r['blocos']:
                if campo in b['capitulo'].lower():
                    b['capitulo'] = 'Outro'
            self.assertTrue(any(texto in e for e in rtexv.checar(r)[0]), campo)
        self.assertTrue(any('outro.site' in e for e in rtexv.checar(base(), 'outro.site')[0]))

    def test_destino_falado_por_extenso(self):
        r = base()
        r['blocos'][-1]['fala'] = 'No ARCKHÉ ponto club você aprende de graça. O que acha?'
        self.assertFalse(any('citar' in e for e in rtexv.checar(r)[0]))

    def test_roteiro_quebrado_nao_estoura(self):
        self.assertTrue(rtexv.checar({})[0])
        self.assertTrue(rtexv.checar({'blocos': [{'capitulo': 'Gancho'}]})[0])


class Comandos(unittest.TestCase):
    def test_novo_nao_sobrescreve(self):
        with tempfile.TemporaryDirectory() as t:
            p = f'{t}/a/roteiro.json'
            self.assertEqual(rtexv.main(['novo', p]), 0)
            self.assertEqual(rtexv.main(['novo', p]), 2)

    def test_checar_devolve_codigo(self):
        ok = str(RAIZ / 'exemplos' / 'ia-sem-internet' / 'roteiro.json')
        self.assertEqual(rtexv.main(['checar', ok]), 0)
        self.assertEqual(rtexv.main(['checar', str(RAIZ / 'modelo' / 'roteiro.json')]), 1)
        self.assertEqual(rtexv.main(['checar', '/nao/existe.json']), 2)


if __name__ == '__main__':
    unittest.main()
