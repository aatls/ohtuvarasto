import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_lisaa_alle_0(self):
        self.varasto.lisaa_varastoon(-1)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ota_alle_0(self):
        self.varasto.lisaa_varastoon(5)

        self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_ota_yli_saldon(self):
        self.varasto.lisaa_varastoon(5)

        self.assertAlmostEqual(self.varasto.ota_varastosta(10), 5)

    def test_lisaa_yli_tilavuuden(self):
        self.varasto.lisaa_varastoon(20)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_tilavuus_ei_alita_nollaa(self):
        tyhja_varasto = Varasto(-2)

        self.assertAlmostEqual(tyhja_varasto.tilavuus, 0)

    def test_alkusaldo_ei_alita_nollaa(self):
        nega_varasto = Varasto(10, -5)

        self.assertAlmostEqual(nega_varasto.saldo, 0)

    def test_alkusaldo_ei_ylita_tilavuutta(self):
        ylitys_varasto = Varasto(10, 41)

        self.assertAlmostEqual(ylitys_varasto.saldo, 10)