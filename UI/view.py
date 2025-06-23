import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self._menuAnno = None
        self._menuBrand = None
        self._menuRetailer = None
        self._btnTopVendite = None
        self._btnAnalizzaVendite = None
        self._txtOut = None


    def load_interface(self):
        self._title = ft.Text("Analizza Vendite", color="blue", size=24)
        self._menuAnno = ft.Dropdown(label="anno", hint_text="seleziona anno", width=200)
        self._menuBrand = ft.Dropdown(label="brand", hint_text="seleziona brand", width=200)
        self._menuRetailer = ft.Dropdown(label="retailer", hint_text="seleziona retailer", width=500)
        row1 = ft.Row([self._menuAnno, self._menuBrand, self._menuRetailer], alignment=ft.MainAxisAlignment.CENTER)
        self._btnTopVendite = ft.ElevatedButton(text="Top Vendite", on_click = self._controller.handleTopVendite)
        self._btnAnalizzaVendite = ft.ElevatedButton(text="Analizza Vendite", on_click = self._controller.handleAnalizzaVendite)
        row2 = ft.Row([self._btnTopVendite, self._btnAnalizzaVendite], alignment=ft.MainAxisAlignment.CENTER)
        self._txtOut = ft.ListView(expand=True)
        self._page.add(self._title, row1, row2, self._txtOut)
        self._page.update()
        self._controller.inserisciOpzioniAnno()
        self._controller.inserisciOpzioniBrand()
        self._controller.inserisciOpzioniRetailer()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
