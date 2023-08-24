from common.basePage import BasePage


class ProductListPage(BasePage):
    # 获取列表中第一个商品名称
    def get_firstproductname(self):
        return self.get_element_text(self.first_product)

    # 获取列表所有的商品名称（第一页）
    def get_productnames(self):
        return self.get_element_texts(self.all_products)

    # 获取列表第一个商品的品牌
    def get_firstproductbrand(self):
        return self.get_element_text(self.first_product_brand)

    #
    def get_productbrands(self):
        return self.get_element_texts(self.product_brands)

    def get_search_productname(self, input_productname):
        self.input_text(self.product_name_search_input,input_productname)
        self.click_element(self.search_button)

    def get_search_productbrand(self, input_productbrand):
        self.input_text(self.product_brand_search_select, input_productbrand)
        self.click_element(self.search_button)