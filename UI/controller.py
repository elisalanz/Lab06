import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def inserisciOpzioniAnno(self):
        for anno in self._model.getAnni():
            self._view._menuAnno.options.append(ft.dropdown.Option(text=anno))
        self._view.update_page()

    def inserisciOpzioniBrand(self):
        for brand in self._model.getBrand():
            self._view._menuBrand.options.append(ft.dropdown.Option(text=brand))
        self._view.update_page()

    def inserisciOpzioniRetailer(self):
        for retailer in self._model.getRetailer():
            self._view._menuRetailer.options.append(ft.dropdown.Option(key=retailer.code, text=retailer.name, data=retailer, on_click=self.read_retailer))
        self._view.update_page()

    def read_retailer(self, e):
        self._retailer = e.control.data
        return self._retailer.code

    def handleTopVendite(self, e):
        anno = self._view._menuAnno.value
        brand = self._view._menuBrand.value
        retailer = self._view._menuRetailer.value
        if anno is None or brand is None or retailer is None:
            self._view.create_alert("Completare tutti i campi!")
            return
        top5Vendite = self._model.getTop5Vendite(anno, brand, retailer)
        if len(top5Vendite) == 0:
            self._view.create_alert("Nessuna vendita")
            self._view._menuAnno.value = None
            self._view._menuBrand.value = None
            self._view._menuRetailer.value = None
            self._view.update_page()
            return
        for vendita in top5Vendite:
            self._view._txtOut.controls.append(ft.Text(f"Data: {str(vendita['Date'])}; Ricavo: {vendita['Ricavo']}; Retailer: {vendita['Retailer_code']}; Product: {vendita['Product_number']}"))
        self._view._menuAnno.value = None
        self._view._menuBrand.value = None
        self._view._menuRetailer.value = None
        self._view.update_page()
        self._view._txtOut.controls.clear()

    def handleAnalizzaVendite(self, e):
        anno = self._view._menuAnno.value
        brand = self._view._menuBrand.value
        retailer = self._view._menuRetailer.value
        (giroAffari, numVendite, numRetailer, numProdotti) = self._model.getInformazioniVendite(anno, brand, retailer)
        self._view._txtOut.controls.append(ft.Text(f"Statistiche vendite:\nGiro d'affari: {giroAffari}\nNumero vendite: {numVendite}\nNumero retailers coinvolti: {numRetailer}\nNumero prodotti coinvolti: {numProdotti}"))
        self._view._menuAnno.value = None
        self._view._menuBrand.value = None
        self._view._menuRetailer.value = None
        self._view.update_page()
        self._view._txtOut.controls.clear()


