#!/usr/bin/env python
# coding: utf-8

# # ¡Hola Oscar!
# 
# Mi nombre es Ezequiel Ferrario, soy code reviewer en Tripleten y tengo el agrado de revisar el proyecto que entregaste.
# 
# Para simular la dinámica de un ambiente de trabajo, si veo algún error, en primer instancia solo los señalaré, dándote la oportunidad de encontrarlos y corregirlos por tu cuenta. En un trabajo real, el líder de tu equipo hará una dinámica similar. En caso de que no puedas resolver la tarea, te daré una información más precisa en la próxima revisión.
# 
# Encontrarás mis comentarios más abajo - **por favor, no los muevas, no los modifiques ni los borres**.
# 
# ¿Cómo lo voy a hacer? Voy a leer detenidamente cada una de las implementaciones que has llevado a cabo para cumplir con lo solicitado. Verás los comentarios de esta forma:
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Si todo está perfecto.
# </div>
# 
# 
# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Si tu código está bien pero se puede mejorar o hay algún detalle que le hace falta. Se aceptan uno o dos comentarios de este tipo en el borrador, pero si hay más, deberá hacer las correcciones. Es como una tarea de prueba al solicitar un trabajo: muchos pequeños errores pueden hacer que un candidato sea rechazado.
# </div>
# 
# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Si de pronto hace falta algo o existe algún problema con tu código o conclusiones.
# </div>
# 
# Puedes responderme de esta forma:
# 
# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
# 
# Hola, muchas gracias por tus comentarios y la revisión.        
# </div>
# 
# ¡Empecemos!

# ----------
# 
# <div class="alert alert-block alert-danger">
# <b>Comentario general #1</b> <a class="tocSkip"></a>
# 
# Oscar, has realizado un excelente trabajo aqui.
#     
#   Abarcaste muy bien todos los pasos y entendiste como manejarte a traves de funciones bucles e indices, denotando un muy buen manejo con los mismos.
# 
# Asi, tan solo resta un detalle por abarcar para finalizar este buen proyecto.
# 
# Espero tu correccion.
# 
# Saludos.</div>
# 
# 
# 
# -----------
# 
# <div class="alert alert-block alert-success">
# <b>Comentario general #2</b> <a class="tocSkip"></a>
# 
# Oscar, abarcaste de forma excelente el ultimo punto que restaba por lo que finalizas asi un gran proyecto.
#     
#  Por lo dicho anteriormente, el trabajo pasa a estar **aprobado**.
#     
#    Exitos en lo que viene, saludos.
# 
# </div>
# 
# 
# ---------

# 
# 
# Todavía desempeñándote como miembro del equipo analítico, en el primer proyecto hemos sentado las bases para la segunda fase. ¡Hemos llegado! Ahora aplicarás técnicas avanzadas para extraer datos significativos, atendiendo a las crecientes necesidades del cliente.

# Como sabes, las empresas recopilan y almacenan datos de una forma particular. Store 1 quiere almacenar toda la información de sus clientes en una tabla.
# 
# 
# | user_id | user_name | user_age | purchase_category | spending_per_category |
# | --- | --- | --- | --- | --- |
# | '32415' | 'mike', 'reed' | 32 | 'electronics', 'sport', 'books' | 894, 213, 173 |
# | '31980' | 'kate', 'morgan' | 24 | 'clothes', 'shoes' | 439, 390 |
# 
# En términos técnicos, una tabla es simplemente una lista anidada que contiene una sublista para cada usuario o usuaria.
# 
# Store 1 ha creado una tabla de este tipo para sus usuarios. Está almacenada en la variable "users". Cada sublista contiene el ID del usuario, nombre y apellido, edad, categorías favoritas y el importe gastado en cada categoría.

# -	**user_id:** el identificador único para cada usuario.
# -	**user_name:** el nombre de usuario.
# -	**user_age:** la edad del usuario.
# -	**fav_categories:** las categorías de artículos comprados por el usuario, como 'ELECTRONICS', 'SPORT', 'BOOKS', etc.
# -	**total_spendings:** la lista de enteros que indican la cantidad gastada en cada una de sus categorías favoritas.
# 

# In[1]:


users = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
    ['32761', 'SAMANTHA SMITH', 29.0, ['CLOTHES', 'ELECTRONICS', 'BEAUTY'], [299, 679, 85]],
    ['32984', 'David White', 41.0, ['BOOKS', 'HOME', 'SPORT'], [234, 329, 243]],
    ['33001', 'emily brown', 26.0, ['BEAUTY', 'HOME', 'FOOD'], [213, 659, 79]],
    ['33767', ' Maria Garcia', 33.0, ['CLOTHES', 'FOOD', 'BEAUTY'], [499, 189, 63]],
    ['33912', 'JOSE MARTINEZ', 22.0, ['SPORT', 'ELECTRONICS', 'HOME'], [259, 549, 109]],
    ['34009', 'lisa wilson ', 35.0, ['HOME', 'BOOKS', 'CLOTHES'], [329, 189, 329]],
    ['34278', 'James Lee', 28.0, ['BEAUTY', 'CLOTHES', 'ELECTRONICS'], [189, 299, 579]],
]


# # Paso 1
# 
# En la última tarea de la primera parte de este proyecto escribiste código para:
# 
# 1. Eliminar todos los espacios iniciales y finales de los nombres, así como cualquier guion bajo.
# 2. Convertir todas las edades en números enteros.
# 3. Separar todos los nombres y apellidos en una sublista.
# 
# Hagámoslo ahora una función para que podamos usarla para fijar a cualquier cliente. Nombra a tu función `clean_user`. Debe recibir una lista con toda la información del cliente (user_info), así como dos enteros. Uno de ellos señala el índice del nombre del cliente y el otro es el índice de la edad del cliente en la lista. Debe devolver la lista limpia después de aplicar todos los cambios anteriores. Pruébala llamándola, pasándole la lista `test_user[]` y luego muéstrala en pantalla.
# 

# In[2]:


def clean_user(users_info,name_index,age_index):
    user_info=[]
    user_name_1=users_info[name_index].strip()
    user_name_1=user_name_1.replace('_',' ')
    user_age_1=int(users_info[age_index])
    user_name_1=user_name_1.split()
    user_info.append(users_info[0])
    user_info.append(user_name_1)
    user_info.append(user_age_1)
    user_info.append(users_info[3])
    user_info.append(users_info[4])
    return user_info

# Prueba la función
test_user = ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]]
name_index = 1
age_index = 2

print(clean_user(test_user,name_index,age_index))


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Muy bien.
# </div>
# 

# ********Pista********
# 
# Para implementar la función `clean_user`, efectúa los siguientes pasos:
# 
# 1. **Recortar y reemplazar:** utiliza `strip()` para eliminar espacios iniciales y finales del nombre del usuario y `replace('_', ' ')` para eliminar guiones bajos con espacios.
# 2. **Convertir la edad:** convierte la edad en entero utilizando la función `int()`.
# 3. **Separar el nombre:** utiliza el método `split()` para separar el nombre y el apellido, creando una sublista.
# 
# Asegúrate de modificar la lista `user_info` que aparece actualizando el nombre y la edad con los datos limpios antes de devolver la lista. Prueba tu función con un usuario de ejemplo para verificar que funciona correctamente.
# 

# # Paso 2
# 
# Observa que todas las categorías favoritas están almacenadas en mayúsculas. Llena una nueva lista llamada `fav_categories_low` con las mismas categorías, pero en minúsculas, iterando sobre los valores en la lista `fav_categories`, modificándolos y luego añade los nuevos valores a la lista `fav_categories_low`. Como siempre, muestra el resultado final.
# 

# In[3]:


fav_categories = ['ELECTRONICS', 'SPORT', 'BOOKS']
fav_categories_low = []

for category in fav_categories:
    fav_categories_low.append(category.lower())

print(fav_categories_low)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Excelente.
# 
# </div>
# 

# ********Pista********
# 
# Crea un bucle `for` que itere sobre la lista `fav_categories`. Utiliza el método `lower()` para transformar cada categoría a minúsculas. Luego, utiliza el método `append()` para agregar los valores actualizados a la lista `fav_categories_low`.

# # Paso 3
# 
# Ahora hagamos lo mismo, pero para cada uno de los usuarios de la empresa. Llena una lista nueva llamada `users_categories_low` con los mismos usuarios, pero con sus categorías en minúsculas, iterando sobre los valores en la lista `users`, luego itera sobre los valores en `user_categories`, modificándolos, y después agrega los nuevos valores de usuarios a la lista `users_categories_low`. Como siempre, muestra el resultado final.
# 

# In[4]:


users = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
    ['32761', 'SAMANTHA SMITH', 29.0, ['CLOTHES', 'ELECTRONICS', 'BEAUTY'], [299, 679, 85]],
    ['32984', 'David White', 41.0, ['BOOKS', 'HOME', 'SPORT'], [234, 329, 243]],
    ['33001', 'emily brown', 26.0, ['BEAUTY', 'HOME', 'FOOD'], [213, 659, 79]],
    ['33767', ' Maria Garcia', 33.0, ['CLOTHES', 'FOOD', 'BEAUTY'], [499, 189, 63]],
    ['33912', 'JOSE MARTINEZ', 22.0, ['SPORT', 'ELECTRONICS', 'HOME'], [259, 549, 109]],
    ['34009', 'lisa wilson ', 35.0, ['HOME', 'BOOKS', 'CLOTHES'], [329, 189, 329]],
    ['34278', 'James Lee', 28.0, ['BEAUTY', 'CLOTHES', 'ELECTRONICS'], [189, 299, 579]],
]

for user in users:
    users_categories_low=[item.lower() for item in user[3]]
    user[3]=users_categories_low
    
print(users)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Muy bien pasando las categorias a minusculas.
# </div>
# 

# # ********Pista********
# 
# Crea un bucle `for` que itere sobre la lista `users`. Luego crea otro bucle `for` que itere sobre las categorías de usuarios para acceder al usuario y modificarlo. Utiliza el método `lower()` para transformar cada categoría a minúsculas. Luego, modifica al usuario eliminando la lista de categorías anteriores con `pop()` y con `insert()` inserta la nueva en su lugar. A continuación utiliza el método `append()` para agregar a los usuarios actualizados a la lista `users_categories_low`.

# # Paso 4
# 
# Ahora, completemos el código de nuestra función `clean_user` para limpiar la categoría:
# 1. Añade otro parámetro con el índice de categorías.
# 2. Pon todos los nombres en minúsculas antes de aplicar "strip" y "replace".
# 
# Después, crea un bucle y aplica tu función a toda la lista de usuarios, agregando tus resultados a la lista `users_clean`. Después muéstralo

# In[5]:


def clean_user (users_info, name_index,age_index,cat_index):
    user_info=[]
    user_name_1=user[(name_index)].lower()
    user_name_1=user_name_1.strip()
    user_name_1=user_name_1.replace("_"," ")
    user_age_1=int(user[age_index])
    user_name_1=user_name_1.split()
    categories_low=[]
    for category in users_info:
        user_cat_1=[item.lower() for item in user[cat_index]]
        user[cat_index]=user_cat_1
    user_info.append(user[0])
    user_info.append(user_name_1)
    user_info.append(user_age_1)
    user_info.append(user[3])
    user_info.append(user[4])
    return user_info


users = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
    ['32761', 'SAMANTHA SMITH', 29.0, ['CLOTHES', 'ELECTRONICS', 'BEAUTY'], [299, 679, 85]],
    ['32984', 'David White', 41.0, ['BOOKS', 'HOME', 'SPORT'], [234, 329, 243]],
    ['33001', 'emily brown', 26.0, ['BEAUTY', 'HOME', 'FOOD'], [213, 659, 79]],
    ['33767', ' Maria Garcia', 33.0, ['CLOTHES', 'FOOD', 'BEAUTY'], [499, 189, 63]],
    ['33912', 'JOSE MARTINEZ', 22.0, ['SPORT', 'ELECTRONICS', 'HOME'], [259, 549, 109]],
    ['34009', 'lisa wilson ', 35.0, ['HOME', 'BOOKS', 'CLOTHES'], [329, 189, 329]],
    ['34278', 'James Lee', 28.0, ['BEAUTY', 'CLOTHES', 'ELECTRONICS'], [189, 299, 579]],
]

name_index = 1
age_index = 2
cat_index = 3
users_cleaned = []

for user in users:
    user_cleaned=clean_user(users,name_index,age_index,cat_index)
    users_cleaned.append(user_cleaned)

print(users_cleaned)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Muy buena funcion, si quisieras reducirla podrias encadenar varios metodos en la misma linea.
# </div>
# 

# ********Pista********
# 
# Efectúa los siguientes pasos para implementar la función `clean_user`:
# 
# 1. **Copia y adapta:** copia el código de tu función anterior `clean_user`.
# 
# 2. **Pon el nombre en minúsculas:** antes de aplicar `split()` y `replace()`, aplica `lower()` al nombre del cliente.
# 
# 3. **Procesa las categorías:** agrega una sección nueva para gestionar las categorías. Pon cada categoría de la lista en minúsculas y almacénalas en una nueva lista.
# 
# 4. **Ejecuta tu código:** asegúrate de que la función `clean_user` actualice la lista `user_info` con el nombre, edad y categorías limpias. Haz un bucle en la lista `users` y llama a la función `clean_user`, pasando el usuario, `name_index`, `age_index` y `cat_index` para especificar los índices correctos para el nombre, la edad y las categorías, respectivamente.
# 
# 5. Guarda cada nuevo usuario limpio en la lista nueva `users_cleaned`.
# 
# Muestra en pantalla la lista `users_cleaned` para asegurarte de que tu código realiza las respectivas transformaciones.
# 

# # Paso 5
# 
# La empresa desea conocer sus ingresos totales y te pide que proporciones este valor.
# Para calcular los ingresos de la empresa, sigue estos pasos:
# 
# 1. Utiliza `for` para iterar sobre la lista `users`.
# 2. Extrae la lista de gastos de cada usuario y suma los valores.
# 3. Actualiza el valor de los ingresos con el total de cada usuario.
# 
# Así obtendrás los ingresos totales de la empresa que mostrarás en la pantalla al final.
# 

# In[6]:


users = [['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'], [894, 213, 173]],
         ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439, 390]],
         ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'], [459, 120, 99]],
         ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics', 'beauty'], [299, 679, 85]],
         ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234, 329, 243]],
         ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213, 659, 79]],
         ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'], [499, 189, 63]],
         ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'], [259, 549, 109]],
         ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'], [329, 189, 329]],
         ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'], [189, 299, 579]]]

revenue = 0

for user in users:
    spendings_list=user[4]
    total_spendings=sum(spendings_list)
    revenue += total_spendings
    
print(revenue)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Excelente.</div>
# 

# ********Pista********
# 
# Para extraer la lista de gastos realizados por un usuario, utiliza la indexación y asígnala a la variable `spendings_list`. Luego, utiliza la función integrada para calcular la suma de `spending_list`. Por último, actualiza el valor de `revenue` añadiéndole  `total_spendings` mediante la asignación aumentada.

# # Paso 6
# 
# La empresa quiere ofrecer descuentos a sus clientes leales. Los clientes que realizan compras por un importe total mayor a $1500 se consideran leales y recibirán un descuento.
# 
# Nuestro objetivo es crear un bucle `while` que compruebe el importe total gastado y se detenga al alcanzarlo. Para simular nuevas compras, la variable `new_purchase` genera un número entre 30 y 80 en cada iteración del bucle. Esto representa la cantidad de dinero gastada en una nueva compra y es lo que debes agregar al total.
# 
# Una vez que se alcance el importe objetivo y se termine el bucle `while`, se mostrará la cantidad final.
# 

# In[12]:


from random import randint

total_amount_spent = 1280
target_amount = 1500

while total_amount_spent<target_amount:
    new_purchase = randint(30, 80)
    total_amount_spent += new_purchase

print(total_amount_spent)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Perfecto.
# 
# </div>
# 

# ********Pista********
# 
# En el bucle `while`, debes comparar `total_amount_spent` (importe total gastado) con `target_amount` (importe objetivo). Durante cada iteración del bucle, actualiza la variable `total_amount_spent` agregándole el valor `new_purchase`.

# # Paso 7
# 
# Recorre la lista de usuarios que te hemos proporcionado y muestra los nombres de los clientes menores de 30 años.
# 

# In[8]:


users = [['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'], [894, 213, 173]],
         ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439, 390]],
         ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'], [459, 120, 99]],
         ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics', 'beauty'], [299, 679, 85]],
         ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234, 329, 243]],
         ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213, 659, 79]],
         ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'], [499, 189, 63]],
         ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'], [259, 549, 109]],
         ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'], [329, 189, 329]],
         ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'], [189, 299, 579]]]


for user in users:
    if user[2]<30:
        print(user[1])


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Buena extraccion.</div>
# 

# ********Pista********
# 
# Utiliza el bucle for para iterar sobre cada fila de la tabla. Utiliza `if` dentro de un bucle `for` para imprimir el nombre de usuario o usuaria. El campo `age` tiene el índice 2

# # Paso 8
# 
# Mostremos en pantalla los nombres de los usuarios menores de 30 años que acumulan un gasto total superior a 1000 dólares.
# 

# In[9]:


users = [['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'], [894, 213, 173]],
         ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439, 390]],
         ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'], [459, 120, 99]],
         ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics', 'beauty'], [299, 679, 85]],
         ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234, 329, 243]],
         ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213, 659, 79]],
         ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'], [499, 189, 63]],
         ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'], [259, 549, 109]],
         ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'], [329, 189, 329]],
         ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'], [189, 299, 579]]]

for user in users:
    if user[2]<30 and sum(user[4])>1000:
        print(user[1])


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Muy bien utilizada las expresiones anidadas.
# </div>
# 

# ********Pista********
# 
# Utiliza el bucle for para iterar sobre cada fila de la tabla. Utiliza `if` dentro de un bucle `for` para imprimir el nombre de usuario o usuaria. El campo `age` tiene el índice 2. Utiliza la función `sum` para sumar los gastos y luego comprueba si es mayor de 1000 dólares.

# # Paso 9
# 
# Ahora vamos a mostrar el nombre y la edad de todos los usuarios y todas las usuarias que han comprado ropa ("clothes"). Imprime el nombre y la edad en la misma declaración print.
# 

# In[10]:


users = [['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'], [894, 213, 173]],
         ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439, 390]],
         ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'], [459, 120, 99]],
         ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics', 'beauty'], [299, 679, 85]],
         ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234, 329, 243]],
         ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213, 659, 79]],
         ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'], [499, 189, 63]],
         ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'], [259, 549, 109]],
         ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'], [329, 189, 329]],
         ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'], [189, 299, 579]]]

users_filtered=[]
for user in users:
    for category in users:
        user_filtered=[]
        if 'clothes' in user[3]:
            user_filtered.append(user[1])
            user_filtered.append(user[2])
    users_filtered.append(user_filtered)
            

print(users_filtered)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Perfecto. Como consejo podrias crear un f-string para que el resultado sea mas estetico.
# 
# Algo asi como '*Nombre: Kate, edad 24 años.*'</div>

# ********Pista********
# 
# Utiliza el bucle for para iterar sobre cada fila de la tabla. A continuación, utiliza otro bucle para comprobar si este usuario ha comprado ropa ("clothes") y, en caso afirmativo, muestra el nombre y la edad dentro de la misma declaración print, separándolos por comas: `print(firstname, age)`.

# # Paso 10
# 
# La dirección requiere de una función que proporcione información sobre los clientes, incluyendo sus nombres, edades y gasto total, filtrada por categorías específicas. Con base en fragmentos de código anteriores, crearemos una función llamada `get_client_by_cat` con las siguientes especificaciones:
# 
# 1. **Parámetros:**
#    - **users:** una lista con los datos de los usuarios.
#    - **id_index:** el índice donde está almacenado el ID del cliente en la lista de usuarios.
#    - **name_index:** el índice donde está almacenado el nombre del cliente en la lista de usuarios.
#    - **age_index:** el índice donde la edad del cliente está almacenada en la lista de usuarios.
#    - **category_index:** el índice donde las categorías de compras del cliente están listadas.
#    - **amounts_index:** el índice donde las cantidades gastadas en cada categoría están almacenadas.
#    - **filter_category:** un string que representa el nombre de la categoría para filtrar clientes.
# 
# 2. **Salida:**
#    - La función devuelve una lista de sublistas. Cada sublista contiene:
#      - El número ID del cliente.
#      - Una sublista con el nombre y apellido del cliente.
#      - La edad del cliente.
#      - Un entero que representa la cantidad total gastada por el cliente.
# 
# Por ejemplo, si llamas a la función con los siguientes parámetros:
# 
# 
# ```python
# get_client_by_cat([
#     ['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'], [894, 213, 173]]
# ], 0, 1, 2, 3, 4, 'books')
# ```
# 
# La salida será:
# 
# ```python
# [['32415', ['mike', 'reed'], 32, 1280]]
# ```
# 
# Esta salida muestra que el cliente con el ID '32415', llamado Mike Reed, de 32 años, gastó un total de 1280 en la categoría 'books' y otras compras.
# 
# Después de hacer tu función, llámala pasándole nuestra lista de usuarios, los índices adecuados y la categoría 'home' y muestra en pantalla la lista que resulta.
# 
# 

# In[1]:


id_index=0
name_index=1
age_index=2
category_index=3
amounts_index=4
filter_category='home'


def get_client_by_cat(users_data,id_index,name_index,age_index,category_index,amounts_index,filter_category):
    users_filtered=[]
    for user in users:
        user_filtered=[]
        if filter_category in user[3]:
            total_amount_spent=sum(user[4])
            user_filtered.append(user[0])
            user_filtered.append(user[1])
            user_filtered.append(user[2])
            user_filtered.append(user[3])
            user_filtered.append(total_amount_spent)
        users_filtered.append(user_filtered)
    return users_filtered

# La lista de usuarios
users = [
    ['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'], [894, 213, 173]],
    ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439, 390]],
    ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'], [459, 120, 99]],
    ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics', 'beauty'], [299, 679, 85]],
    ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234, 329, 243]],
    ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213, 659, 79]],
    ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'], [499, 189, 63]],
    ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'], [259, 549, 109]],
    ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'], [329, 189, 329]],
    ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'], [189, 299, 579]]
]

# Llama a la función con la categoría 'home'
result = get_client_by_cat(users,id_index,name_index,age_index,category_index,amounts_index,filter_category)

# Muestra en pantalla la lista que resulta
print(result)


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Esta perfecta la funcion, solo restaria extraer tambien las **categorias**.</div>
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido, excelente.</div>
# 

# In[ ]:


# Hola, corregido (no sé dar el formato de cuadro azul como respuesta de estudiante).


# ********Pista********
# 
# Utiliza un bucle for para iterar sobre cada usuario en la lista. Para cada usuario, verifica que la categoría deseada ("filter_category") esté en su lista de categorías de compras. Si se encuentra la categoría, calcula la cantidad total gastada sumando las cantidades en la lista correspondiente. Después, crea una sublista con el ID, nombre (como una lista de nombres y apellidos), edad y cantidad total gastada del usuario. Añade esta sublista a la lista final que resulta.
