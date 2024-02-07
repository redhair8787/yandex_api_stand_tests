import configuration
import requests
import data


#def get_docs():
    #return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)
#код ответа страницы
#response = get_docs()
#print(response.status_code)


#def get_logs():
    #return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH)
#обращение к логам

#response = get_logs()
#print(response.status_code)
#print(response.headers)


#def get_logs():
    #return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,
                        #params={"count": 20})
#обращение к логам и определенным параметрам

#response = get_logs()
#print(response.status_code)
#print(response.headers)


def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
#обращение к таблице в базе данных#

response = get_users_table()
print(response.status_code)


#запрос на создание пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки

response = post_new_user(data.user_body)
print(response.status_code)
print(response.json()) #чтобы тело ответа было выведено на экран в формате словаря.


#запрос на поиск наборов по продуктам Main.Products
#def post_products_kits(products_ids):
    #return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, json=products_ids,
                         #headers=data.headers)


#response = post_products_kits(data.product_ids);
#print(response.status_code)
#print(response.json())



