from database.DB_connect import DBConnect


class DAO():
    @staticmethod
    def getAnni():
        cnx = DBConnect.get_connection()
        res = []
        if cnx is None:
            return res
        cursor = cnx.cursor()
        query = """SELECT DISTINCT YEAR(Date) FROM go_daily_sales ORDER BY YEAR(Date)"""
        cursor.execute(query)
        for row in cursor:
            res.append(row[0])
        cursor.close()
        cnx.close()
        return res # restituisce una lista di stringhe

    @staticmethod
    def getBrand():
        cnx = DBConnect.get_connection()
        res = []
        if cnx is None:
            return res
        cursor = cnx.cursor()
        query = """SELECT DISTINCT Product_brand FROM go_products ORDER BY Product_brand"""
        cursor.execute(query)
        for row in cursor:
            res.append(row[0])
        cursor.close()
        cnx.close()
        return res  # restituisce una lista di stringhe

    @staticmethod
    def getRetailer():
        cnx = DBConnect.get_connection()
        res = []
        if cnx is None:
            return res
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM go_retailers ORDER BY Retailer_name"""
        cursor.execute(query)
        for row in cursor:
            res.append(row)
        cursor.close()
        cnx.close()
        return res  # restituisce una lista di dizionari con i campi di Retailer

    @staticmethod
    def getVendite():
        cnx = DBConnect.get_connection()
        res = []
        if cnx is None:
            return res
        cursor = cnx.cursor(dictionary=True)
        query = """select gds.Date, gds.Product_number, gds.Unit_sale_price , gds.Quantity, year(gds.Date) as Year, gp.Product_brand, gds.Retailer_code
                    from go_daily_sales gds, go_products gp
                    where gds.Product_number = gp.Product_number"""
        cursor.execute(query)
        for row in cursor:
            res.append(row)
        cursor.close()
        cnx.close()
        return res

