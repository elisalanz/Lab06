from database.DAO import DAO
from model.retailer import Retailer


class Model:
    def __init__(self):
        self._retailers = []

    def getAnni(self):
        return DAO.getAnni()

    def getBrand(self):
        return DAO.getBrand()

    def getRetailer(self):
        listaRetailer = DAO.getRetailer()
        for retailer in listaRetailer:
            self._retailers.append(Retailer(retailer["Retailer_code"], retailer["Retailer_name"], retailer["Type"], retailer["Country"]))
        return self._retailers # lista di oggetti Retailer

    def getTop5Vendite(self, anno, brand, codRetailer):
        vendite = DAO.getVendite()
        selezione = []
        for vendita in vendite:
            if vendita["Retailer_code"] == int(codRetailer) and vendita["Year"] == int(anno) and vendita["Product_brand"] == brand:
                vendita["Ricavo"] = vendita["Quantity"] * vendita["Unit_sale_price"]
                selezione.append(vendita)
        selezione.sort(key=lambda x: x["Ricavo"], reverse=True)
        return selezione[0:min(5, len(selezione))]

    def getInformazioniVendite(self, anno, brand, codRetailer):
        vendite = DAO.getVendite()
        for vendita in vendite:
            vendita["Ricavo"] = vendita["Quantity"] * vendita["Unit_sale_price"]
        for vendita in vendite:
            if (anno is not None and vendita["Year"] != int(anno)) or (brand is not None and vendita["Product_brand"] != brand) or (codRetailer is not None and vendita["Retailer_code"] != int(codRetailer)):
                vendite.remove(vendita)
        numVendite = len(vendite)
        giroAffari = 0
        setRetailer = set()
        setProdotti = set()
        for vendita in vendite:
            setRetailer.add(vendita["Retailer_code"])
            setProdotti.add(vendita["Product_number"])
            giroAffari += vendita["Ricavo"]
        numRetailer = len(setRetailer)
        numProdotti = len(setProdotti)
        return (giroAffari, numVendite, numRetailer, numProdotti)









